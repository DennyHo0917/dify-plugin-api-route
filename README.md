# API Route plugin for Dify

This plugin connects [API Route](https://www.api-route.com/) to Dify as an OpenAI-compatible chat model provider. It uses one fixed endpoint: `https://global.api-route.com/v1`.

## Requirements

- An API Route account and API key.
- HTTPS access from your Dify instance to `global.api-route.com`.

## Setup

1. Install the plugin in Dify.
2. Open **Settings → Model Provider → API Route** and add a model.
3. Enter an exact model ID from the [current model catalog](https://www.api-route.com/pricing), such as `gpt-5.5`.
4. Enter your API key. Set context size, tool calling and vision support to match the chosen model.

Select the configured model in a Dify app, workflow or agent node. This plugin supports chat models. Use a separate provider for embeddings.

## Privacy and source

The plugin sends requests only to API Route; see [PRIVACY.md](PRIVACY.md) and the [API Route privacy policy](https://www.api-route.com/privacy-policy). Source: https://github.com/DennyHo0917/dify-plugin-api-route.
