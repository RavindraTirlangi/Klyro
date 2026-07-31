from unittest import mock

import requests

from klyro.model_provider import ModelDiscoveryError, ModelProviderService


def test_model_provider_caches_discovery_results():
    service = ModelProviderService()
    service.identify = mock.Mock(return_value=("openai", None))
    service._list_litellm = mock.Mock(return_value=["openai/gpt-test"])

    first = service.list_models("openai/gpt-test")
    second = service.list_models("openai/gpt-test")

    assert first == second
    service._list_litellm.assert_called_once()


def test_model_provider_refresh_bypasses_cache():
    service = ModelProviderService()
    service.identify = mock.Mock(return_value=("openai", None))
    service._list_litellm = mock.Mock(return_value=["openai/gpt-test"])

    service.list_models("openai/gpt-test")
    service.list_models("openai/gpt-test", force_refresh=True)

    assert service._list_litellm.call_count == 2


def test_model_provider_offline_completion_uses_current_dynamic_model():
    service = ModelProviderService()
    service.identify = mock.Mock(return_value=("ollama", "http://localhost:11434"))

    provider, names = service.list_models("ollama/local-model", allow_network=False)

    assert provider == "ollama"
    assert names == ["ollama/local-model"]


@mock.patch("klyro.model_provider.requests.get")
def test_ollama_connection_error_is_actionable(mock_get):
    mock_get.side_effect = requests.ConnectionError("refused")
    service = ModelProviderService()

    try:
        service.list_models("ollama/local-model")
    except ModelDiscoveryError as err:
        assert "not running" in str(err)
        assert "localhost:11434" in str(err)
    else:
        raise AssertionError("Expected model discovery to fail")


def test_search_is_case_insensitive_and_provider_scoped():
    service = ModelProviderService()
    service.list_models = mock.Mock(
        return_value=("openrouter", ["openrouter/DeepSeek/R1", "openrouter/google/gemma"])
    )

    provider, matches = service.search_models("openrouter/DeepSeek/R1", "deepseek")

    assert provider == "openrouter"
    assert matches == ["openrouter/DeepSeek/R1"]
