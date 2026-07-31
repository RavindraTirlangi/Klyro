import pytest


PROVIDER_ENV_VARS = {
    "ANTHROPIC_API_KEY",
    "AWS_ACCESS_KEY_ID",
    "AWS_PROFILE",
    "AZURE_OPENAI_API_KEY",
    "COHERE_API_KEY",
    "DEEPSEEK_API_KEY",
    "GEMINI_API_KEY",
    "GOOGLE_API_KEY",
    "GROQ_API_KEY",
    "MISTRAL_API_KEY",
    "OLLAMA_HOST",
    "OPENAI_API_KEY",
    "OPENROUTER_API_KEY",
    "XAI_API_KEY",
}


@pytest.fixture(autouse=True)
def isolate_external_provider_environment(monkeypatch, request):
    """Keep tests independent from credentials and services on the developer machine."""
    for name in PROVIDER_ENV_VARS:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("KLYRO_ANALYTICS", "false")

    # Unit tests must not discover the developer's real project/home .env files.
    # The dedicated loader test calls its imported function directly and is
    # intentionally excluded so it continues to exercise the real loader.
    dotenv_tests = {
        "test_env_file_override",
        "test_env_file_flag_sets_automatic_variable",
        "test_default_env_file_sets_automatic_variable",
        "test_false_vals_in_env_file",
        "test_true_vals_in_env_file",
        "test_verbose_mode_lists_env_vars",
        "test_load_dotenv_files_override",
    }
    if request.node.name not in dotenv_tests:
        monkeypatch.setattr("klyro.main.load_dotenv_files", lambda *args, **kwargs: [])
