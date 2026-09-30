from dify_plugin import OAICompatLargeLanguageModel

from models.llm.llm import DEFAULT_ENDPOINT, APIRouteLargeLanguageModel


def test_credentials_use_the_fixed_endpoint_and_provider_key():
    credentials = {
        "api_key": "test-api-route-key",
        "endpoint_url": "https://other.example/v1",
    }

    prepared = APIRouteLargeLanguageModel._credentials_with_defaults(credentials)

    assert prepared["endpoint_url"] == DEFAULT_ENDPOINT
    assert prepared["openai_api_key"] == "test-api-route-key"
    assert prepared["mode"] == "chat"
    assert prepared["function_calling_type"] == "tool_call"
    assert prepared["stream_function_calling"] == "supported"
    assert credentials["endpoint_url"] == "https://other.example/v1"


def test_invoke_passes_prepared_credentials_to_openai_compatible_transport(monkeypatch):
    captured = {}
    expected = object()

    def fake_invoke(self, model, credentials, *args):
        captured["model"] = model
        captured["credentials"] = credentials
        return expected

    monkeypatch.setattr(OAICompatLargeLanguageModel, "_invoke", fake_invoke)
    provider = APIRouteLargeLanguageModel(model_schemas=[])

    result = provider._invoke("gpt-5.5", {"api_key": "test-key"}, [], {}, stream=False)

    assert result is expected
    assert captured["model"] == "gpt-5.5"
    assert captured["credentials"]["openai_api_key"] == "test-key"
    assert captured["credentials"]["endpoint_url"] == DEFAULT_ENDPOINT
