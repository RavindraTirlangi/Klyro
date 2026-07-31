"""Provider-aware model discovery used by slash commands and completion."""

import os
import time

import requests

from klyro.llm import litellm
from klyro.openrouter import OpenRouterModelManager, OpenRouterRequestError


class ModelDiscoveryError(Exception):
    pass


class ModelProviderService:
    CACHE_TTL = 5 * 60

    def __init__(self, verify_ssl=True):
        self.verify_ssl = verify_ssl
        self.cache = {}

    def identify(self, model_name):
        try:
            _, provider, _, api_base = litellm.get_llm_provider(model_name)
            return provider, api_base
        except Exception as err:
            if "/" in model_name:
                return model_name.split("/", 1)[0], None
            raise ModelDiscoveryError(f"Unable to identify the provider for {model_name}: {err}")

    def list_models(self, current_name, allow_network=True, force_refresh=False):
        provider, api_base = self.identify(current_name)
        cache_key = (provider, api_base)
        cached = self.cache.get(cache_key)
        if cached and not force_refresh and time.time() - cached["time"] < self.CACHE_TTL:
            return provider, cached["models"]

        if not allow_network and provider in {"ollama", "openrouter"}:
            return provider, cached["models"] if cached else [current_name]

        if provider == "ollama":
            discovered = self._list_ollama(api_base)
        elif provider == "openrouter":
            discovered = self._list_openrouter()
        else:
            discovered = self._list_litellm(provider, current_name)

        if current_name not in discovered:
            discovered.append(current_name)
        discovered = sorted(set(discovered))
        self.cache[cache_key] = {"time": time.time(), "models": discovered}
        return provider, discovered

    def search_models(self, current_name, query):
        provider, available = self.list_models(current_name)
        query = query.casefold()
        return provider, [name for name in available if query in name.casefold()]

    def invalidate(self):
        self.cache.clear()

    def _list_ollama(self, api_base):
        host = (os.environ.get("OLLAMA_HOST") or api_base or "http://localhost:11434").rstrip("/")
        try:
            response = requests.get(
                f"{host}/api/tags",
                timeout=2,
                verify=self.verify_ssl,
            )
            response.raise_for_status()
        except requests.Timeout as err:
            raise ModelDiscoveryError(f"Ollama timed out at {host}.") from err
        except requests.ConnectionError as err:
            raise ModelDiscoveryError(f"Ollama is not running at {host}.") from err
        except requests.RequestException as err:
            raise ModelDiscoveryError(f"Ollama model discovery failed: {err}") from err

        return [
            f"ollama/{item['name']}"
            for item in response.json().get("models", [])
            if item.get("name")
        ]

    def _list_openrouter(self):
        manager = OpenRouterModelManager()
        manager.set_verify_ssl(self.verify_ssl)
        try:
            return manager.get_model_names(api_key=os.environ.get("OPENROUTER_API_KEY"))
        except OpenRouterRequestError as err:
            raise ModelDiscoveryError(str(err)) from err

    def _list_litellm(self, provider, current_name):
        discovered = []
        current_uses_prefix = current_name.startswith(f"{provider}/")
        for candidate in litellm.models_by_provider.get(provider, set()):
            info = litellm.model_cost.get(candidate, {})
            mode = info.get("mode")
            if mode and mode not in {"chat", "completion", "responses"}:
                continue
            if current_uses_prefix and not candidate.startswith(f"{provider}/"):
                candidate = f"{provider}/{candidate}"
            discovered.append(candidate)
        return discovered
