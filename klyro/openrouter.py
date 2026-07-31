"""
OpenRouter model metadata caching and lookup.

This module keeps a local cached copy of the OpenRouter model list
(downloaded from ``https://openrouter.ai/api/v1/models``) and exposes a
helper class that returns metadata for a given model in a format compatible
with litellm’s ``get_model_info``.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict

import requests


class OpenRouterRequestError(Exception):
    pass


def _cost_per_token(val: str | None) -> float | None:
    """Convert a price string (USD per token) to a float."""
    if val in (None, "", "0"):
        return 0.0 if val == "0" else None
    try:
        return float(val)
    except Exception:  # noqa: BLE001
        return None


class OpenRouterModelManager:
    MODELS_URL = "https://openrouter.ai/api/v1/models"
    CACHE_TTL = 60 * 60 * 24  # 24 h

    def __init__(self) -> None:
        self.cache_dir = Path.home() / ".klyro" / "caches"
        self.cache_file = self.cache_dir / "openrouter_models.json"
        self.content: Dict | None = None
        self.verify_ssl: bool = True
        self._cache_loaded = False

    # ------------------------------------------------------------------ #
    # Public API                                                         #
    # ------------------------------------------------------------------ #
    def set_verify_ssl(self, verify_ssl: bool) -> None:
        """Enable/disable SSL verification for API requests."""
        self.verify_ssl = verify_ssl

    def get_model_info(self, model: str) -> Dict:
        """
        Return metadata for *model* or an empty ``dict`` when unknown.

        ``model`` should use the klyro naming convention, e.g.
        ``openrouter/nousresearch/deephermes-3-mistral-24b-preview:free``.
        """
        self._ensure_content()
        if not self.content or "data" not in self.content:
            return {}

        route = self._strip_prefix(model)

        # Consider both the exact id and id without any “:suffix”.
        candidates = {route}
        if ":" in route:
            candidates.add(route.split(":", 1)[0])

        record = next((item for item in self.content["data"] if item.get("id") in candidates), None)
        if not record:
            return {}

        context_len = (
            record.get("top_provider", {}).get("context_length")
            or record.get("context_length")
            or None
        )

        pricing = record.get("pricing", {})
        return {
            "max_input_tokens": context_len,
            "max_tokens": context_len,
            "max_output_tokens": context_len,
            "input_cost_per_token": _cost_per_token(pricing.get("prompt")),
            "output_cost_per_token": _cost_per_token(pricing.get("completion")),
            "litellm_provider": "openrouter",
        }

    def get_model_names(self, api_key: str | None = None) -> list[str]:
        """Return OpenRouter text models, filtered for the user when authenticated."""
        content = None
        if api_key:
            try:
                response = requests.get(
                    f"{self.MODELS_URL}/user",
                    headers={"Authorization": f"Bearer {api_key}"},
                    params={"output_modalities": "text"},
                    timeout=10,
                    verify=self.verify_ssl,
                )
                response.raise_for_status()
                content = response.json()
            except requests.Timeout as err:
                raise OpenRouterRequestError("OpenRouter model discovery timed out.") from err
            except requests.HTTPError as err:
                status = err.response.status_code if err.response is not None else "unknown"
                if status == 401:
                    message = "OpenRouter rejected the API key."
                else:
                    message = f"OpenRouter model discovery failed with HTTP {status}."
                raise OpenRouterRequestError(message) from err
            except requests.RequestException as err:
                raise OpenRouterRequestError(f"Unable to reach OpenRouter: {err}") from err
        else:
            self._ensure_content()
            content = self.content

        if not content:
            return []

        names = []
        for item in content.get("data", []):
            model_id = item.get("id")
            output_modalities = item.get("architecture", {}).get("output_modalities", [])
            if model_id and (not output_modalities or "text" in output_modalities):
                names.append(f"openrouter/{model_id}")
        return sorted(set(names))

    # ------------------------------------------------------------------ #
    # Internal helpers                                                   #
    # ------------------------------------------------------------------ #
    def _strip_prefix(self, model: str) -> str:
        return model[len("openrouter/") :] if model.startswith("openrouter/") else model

    def _ensure_content(self) -> None:
        self._load_cache()
        if not self.content:
            self._update_cache()

    def _load_cache(self) -> None:
        if self._cache_loaded:
            return
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            if self.cache_file.exists():
                cache_age = time.time() - self.cache_file.stat().st_mtime
                if cache_age < self.CACHE_TTL:
                    try:
                        self.content = json.loads(self.cache_file.read_text())
                    except json.JSONDecodeError:
                        self.content = None
        except OSError:
            # Cache directory might be unwritable; ignore.
            pass

        self._cache_loaded = True

    def _update_cache(self) -> None:
        try:
            response = requests.get(self.MODELS_URL, timeout=10, verify=self.verify_ssl)
            if response.status_code == 200:
                self.content = response.json()
                try:
                    self.cache_file.write_text(json.dumps(self.content, indent=2))
                except OSError:
                    pass  # Non-fatal if we can’t write the cache
        except Exception as ex:  # noqa: BLE001
            print(f"Failed to fetch OpenRouter model list: {ex}")
            try:
                self.cache_file.write_text("{}")
            except OSError:
                pass
