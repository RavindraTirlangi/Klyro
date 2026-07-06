---
parent: Connecting to LLMs
nav_order: 550
---

# Vertex AI

Klyro can connect to models provided by Google Vertex AI.
You will need to install the
[gcloud CLI](https://cloud.google.com/sdk/docs/install) and [login](https://cloud.google.com/sdk/docs/initializing) with a GCP account
or service account with permission to use the Vertex AI API.

With your chosen login method, the gcloud CLI should automatically set the
`GOOGLE_APPLICATION_CREDENTIALS` environment variable which points to the credentials file.

First, install klyro:

{% include install.md %}

To configure Klyro to use the Vertex AI API, you need to set `VERTEXAI_PROJECT` (the GCP project ID)
and `VERTEXAI_LOCATION` (the GCP region) [environment variables for Klyro](/docs/config/dotenv.html).

Note that Claude on Vertex AI is only available in certain GCP regions, 
check [the model card](https://console.cloud.google.com/vertex-ai/publishers/anthropic/model-garden/claude-3-5-sonnet) 
for your model to see which regions are supported.

Example `.env` file:

```
VERTEXAI_PROJECT=my-project
VERTEXAI_LOCATION=us-east5
```

Start working with klyro and Vertex AI on your codebase:

```
# Change directory into your codebase
cd /to/your/project

klyro --model vertex_ai/claude-3-5-sonnet@20240620
```

Or you can use the [YAML config](/docs/config/klyro_conf.html) to set the model to any of the 
models supported by Vertex AI.

Example `.klyro.conf.yml` file:

```yaml
model: vertex_ai/claude-3-5-sonnet@20240620
```
