# Agentic AI for Lead Generation — Guest Lecture (45 min, EN)

English guest lecture for **BWL Master students** in "Advanced Issues
in Marketing and Sales" (guest slot: Thursday, 22 Oct 2026, 15:15–16:00):
how **agentic AI** finds, qualifies and ranks partner companies for the chair —
delivered as a **live walkthrough** in an AI harness. The ranked partner
shortlist produced in the demo becomes **evidence the Bachelor course
"Sales Strategy and Execution" may take up next summer semester**.

## Files

| File | What |
|---|---|
| [`agentic-ai-for-lead-generation.md`](agentic-ai-for-lead-generation.md) | Deck source (Marp, 23 slides, JLU design: white background, JLU blue, speaker notes with timing) |
| [`agentic-ai-for-lead-generation.html`](agentic-ai-for-lead-generation.html) | Rendered deck (open in browser) |
| [`agentic-ai-for-lead-generation.pdf`](agentic-ai-for-lead-generation.pdf) | PDF for sharing / printing |
| [`agentic-ai-for-lead-generation.pptx`](agentic-ai-for-lead-generation.pptx) | PowerPoint export |
| [`img/`](img/) | Custom SVG diagrams (light, JLU colours) + JLU logo + repo QR code (`qr-repo.png`, decodes to the GitHub URL shown on slide 9) used by the slides |
| [`demo/`](demo/) | Demo kit for the live walkthrough: kickoff prompt + narration (`demo-script.md`), agentic test protocol (`test-protocol.md`), `shortlist-template.md` target format, sector-choice playbook (`branchenauswahl-playbook.md`) |
| [`../leads/`](../leads/) | **Lead exercise — ingest + rate leads for the chair**: brief (`README.md`), schema + rubric (`leads.yaml`), executable validator (`validate_leads.py`). Restored to a clean template between runs |
| [`../leads_walked/`](../leads_walked/) | **T1 agentic test-run archive** — the walked state from the opencode T1 run (2 verified leads, validator output), kept as the auditable record |

## Structure (35 min + 10 min Q&A)

| Block | Content | Time |
|---|---|---|
| 1 · Foundations | agentic ≠ chat · model · harness · loop · git & the repo | ~9 min |
| 2 · Method | contracts · the lead-gen loop · rating formulas · evidence | ~8 min |
| 3 · Walkthrough | live demo: repo → agent at work → validator → the three questions | ~13 min |
| 4 · Reflection | AI providers for students · take-aways · resources | ~5 min |
| 5 · Q&A | your questions · discussion | 10 min |

## Rebuild

Requires [Marp CLI](https://github.com/marp-team/marp-cli) (`npx @marp-team/marp-cli` works too):

```bash
# HTML (speaker notes included as HTML comments)
npx @marp-team/marp-cli --allow-local-files \
  lecture/agentic-ai-for-lead-generation.md -o lecture/agentic-ai-for-lead-generation.html

# PDF / PPTX
npx @marp-team/marp-cli --allow-local-files --pdf  lecture/agentic-ai-for-lead-generation.md -o lecture/agentic-ai-for-lead-generation.pdf
npx @marp-team/marp-cli --allow-local-files --pptx lecture/agentic-ai-for-lead-generation.md -o lecture/agentic-ai-for-lead-generation.pptx
```

## Student resources (from the deck)

- **JLU HRZ API-Service** — free LLM endpoints for JLU members ([uni-giessen.de → HRZ → KI → API-Service](https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service), access: ki@uni-giessen.de)
- **Google AI student plan** — 1 year free ([one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75))
- **OpenRouter** · **OpenCode** · **pi** · **Ollama** — see the providers slide
- This research corpus ([README](../README.md)) is the evidence base for the "why now" slide
