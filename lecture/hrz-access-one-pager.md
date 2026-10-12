# HRZ API-Service — Student Access Quick Start (JLU Gießen)

One page. Free LLM access for JLU members — no credit card, no personal data.

## What it is

The HRZ (Hochschulrechenzentrum) operates an **API-Service** that gives every
JLU member free access to LLMs: open Qwen models with 256K–1M token context
plus selected commercial models. You can plug these models into agentic
harnesses (OpenCode, Claude Code, pi, …) and run your own workflows.

## How to get access (individual, not bulk)

1. Send a short request email to **ki@uni-giessen.de** — state that you are a
   student at JLU Gießen and want access to the HRZ API-Service.
2. You will receive your personal API endpoint/credentials.
3. Use the model overview to pick a model:
   **<https://api.hrz.uni-giessen.de/ui/model_hub_table/>**

Access is free and issued individually. There is no group/chair registration.

## How to use it in a harness

Point your harness at the HRZ endpoint, e.g. via a LiteLLM provider
(`baseURL: https://api.hrz.uni-giessen.de`) or by setting
`ANTHROPIC_BASE_URL` for Claude Code–compatible clients. The exact
configuration depends on your harness — the HRZ docs or the model hub page
show the current values.

## Rules of thumb

- **Never paste private or customer data** into a commercial/cloud harness.
  For sensitive data use a local model (e.g. Ollama) instead.
- Treat the API as a **research tool**: outputs are stochastic, always
  verify claims against sources.
- The service is for **JLU members** — do not share your credentials.

## Alternatives if you need more

| Option | What | Cost |
|---|---|---|
| **Google AI student plan** | 1 year Google AI Plus free for students (verified via SheerID) — [one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75) | free for 1 year |
| **OpenRouter** | one key, many models — [openrouter.ai](https://openrouter.ai) | pay-as-you-go |
| **Ollama** | local, private, offline — [ollama.com](https://ollama.com) | free |

## Links

- HRZ API-Service: <https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service>
- Model overview: <https://api.hrz.uni-giessen.de/ui/model_hub_table/>
- Access request: **ki@uni-giessen.de**