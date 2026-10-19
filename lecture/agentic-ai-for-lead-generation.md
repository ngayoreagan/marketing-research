---
marp: true
theme: default
paginate: true
header: '![h:56](img/jlu-logo.png)'
footer: 'Marketing Chair · Agentic AI for Lead Generation · Tobias Weiß'
style: |
  /* JLU Gießen look: white background, JLU blue #165A97 */
  :root { --jlu-blue: #165A97; --jlu-light: #e8eff6; --jlu-green: #E5F0CF; --ink: #212529; --muted: #6c757d; }
  section {
    background-color: #ffffff;
    color: var(--ink);
    font-family: Verdana, 'Segoe UI', Helvetica, Arial, sans-serif;
    padding: 96px 64px 72px;
    border-top: 10px solid var(--jlu-blue);
  }
  section header { position: absolute; top: 18px; left: 64px; right: auto; }
  section header img { display: block; }
  section footer { color: var(--muted); font-size: 15px; left: 64px; right: 120px; }
  section::after { color: var(--jlu-blue); font-weight: 700; font-size: 18px; right: 64px; }
  section.smaller table { font-size: 18px; }
  section.smaller table th, section.smaller table td { padding: 4px 8px; }
  h1, h2, h3 { color: var(--jlu-blue); font-weight: 700; }
  h2 { border-bottom: 3px solid var(--jlu-green); padding-bottom: 6px; }
  strong { color: var(--jlu-blue); }
  table { margin: 0 auto; font-size: 20px; border-collapse: collapse; }
  table th, table td {
    background-color: #ffffff; padding: 5px 10px;
    border: 1px solid #dee2e6; color: var(--ink);
  }
  table thead th { background-color: var(--jlu-blue); color: #ffffff; border: 1px solid var(--jlu-blue); }
  table tbody tr:nth-child(even) td { background-color: #f4f7fa; }
  pre {
    background: #f8f9fa; border: 1px solid #dee2e6; border-left: 4px solid var(--jlu-blue);
    border-radius: 4px; color: var(--ink); font-size: 18px; padding: 12px;
  }
  code { background: #f1f3f5; color: var(--ink); }
  blockquote {
    background: var(--jlu-light); border-left: 5px solid var(--jlu-blue); color: var(--ink);
    font-style: normal; font-size: 22px; margin: 16px 0; padding: 6px 18px;
  }
  a { color: var(--jlu-blue); }
  ul { font-size: 24px; }
  li { margin: 6px 0; }
  li::marker { color: var(--jlu-blue); }
  section.lead { justify-content: center; border-top-width: 10px; }
  section.lead h1 { font-size: 54px; }
  section.lead h2 { border-bottom: none; color: var(--ink); font-weight: 400; }
---

<!-- _class: lead -->

# Agentic AI for Lead Generation

## Partner companies for the Marketing Chair

Tobias Weiß · Guest Lecture · Marketing Chair

Thursday, 22 October 2026 · 15:15–16:00
within "Advanced Issues in Marketing and Sales" (Prof. Haas)

45 minutes · BWL Master students · WS 2026/27 edition

<!-- notes:
⏱ ~45 s · READ ALOUD

Good afternoon — and thank you for having me. Here's what this
session is about: agentic AI — what it is, and how you run it so
that its work is trustworthy. And everything we do today maps onto
one real task: helping this chair find and qualify B2B partner
companies. The shortlist the agent produces is evidence for our
Bachelor course Sales Strategy and Execution next summer. So
nothing here is an exercise — it's the start of a deliverable.
Let's get going.
-->

---

## Why this session exists

- The chair partners with companies: funding, data, cases
- Finding + qualifying partners is manual, slow, unscalable
- Agentic AI can research, score and rank prospects
- **Demo output = evidence for "Sales Strategy and Execution" (SS 2027)**

> Nobody wins from another lecture about chatbots.

<!-- notes:
⏱ ~45 s · READ ALOUD

[If preceding talker, bridge first:] You just heard about modern
marketing and sales in a digital world — agentic AI is the tooling
that puts exactly that into practice.

Here's the job we're solving. This chair partners with companies —
for funding, for data, for teaching cases. Finding and qualifying
those partners is manual work: slow, and it doesn't scale. Agentic
AI can research companies, score them, and rank them. And let me be
straight with you: nobody needs another lecture about chatbots.
What you need is to recognise — and judge — an agentic workflow,
and to read the contract that drives it. The demo we watch produces
a ranked list of partners, every claim with a source. That list is
the dataset our Bachelor students build on next year.
[jot: the "ranked list" is the handoff artefact — the
"output as input" promise. Protect it; it returns on slides 16/18.]
-->

---

## What you will be able to do

| By the end… | You can… |
|---|---|
| **Understand** | Explain what "agentic" means, and why it is not a chatbot |
| **Operate** | Read how a harness (pi) gives an AI tools, rules and a task |
| **Assess** | Judge an agentic output: checked? citable? repeatable? |
| **Apply** | Reuse the loop from the demo (contract → run → verify) for partner sourcing |
| **Context** | Say which context an agent can't know — and why that keeps you in charge |

> Model = brain. Harness = hands. Workflow = muscles. **Context = memory — the part only you can supply.**

<!-- notes:
⏱ ~30 s · READ ALOUD

Here's the promise of the next forty-five minutes, in four rows.
You'll be able to explain what agentic actually means — and why it
is not a clever chatbot. You'll be able to read how a harness gives
an AI tools, rules, and a task. You'll be able to judge an agentic
output — checked? citable? repeatable? And you'll be able to reuse
the loop you see today: contract, run, verify. One headline before
we start: model is the brain, harness is the hands, workflow is the
muscles — and context is the memory. That part is yours.
[Not read — colour:] Row 5 is the thread of the whole talk:
intelligence is distributed — generation (model), execution
(harness), context (you).
-->

---

<!-- _class: smaller -->

## Roadmap — 35 min + 10 min Q&A

| Block | Content | Time |
|---|---|---|
| 1 · Foundations | agentic ≠ chat · model · harness · loop | ~8 min |
| 2 · Method | contracts · the lead-gen loop · sector decision · evidence | ~7 min |
| 3 · Walkthrough | live demo: contract → agent → verify | ~13 min |
| 4 · Reflection | providers · take-aways · resources | ~5 min |
| 5 · Q&A | your questions · discussion | 10 min |

> The walkthrough is the heart — theory is fuel for it. **10 minutes are reserved for your questions.**

<!-- notes:
⏱ ~15 s · READ ALOUD

That's the map for the next thirty-five minutes: foundations first,
then the method, then the live walkthrough — that is the heart —
and a short reflection at the end. Ten minutes are reserved for your
questions. So if one comes to you mid-talk: write it down, we'll
get to it.
[Not read:] The notes sum to ~32 min; the gap to 35 is deliberate
buffer for transitions and demo hiccups. Q&A is fixed at 10 min —
bank questions with "hold that for Q&A".
-->

---

## Agentic ≠ chat

![w:1200](img/chat-vs-agent.svg)

> "Agentic" is a working environment — not a better chat.

<!-- notes:
⏱ ~2.5 min · READ ALOUD

Let's clear up the most common confusion first. On the left — that's
chat. Question in, answer out. No tools, no files, no actions: just
a conversation. On the right — that's an agent: a goal, a plan,
tools, and verification, running inside a harness that grants it
access to the world — a browser, files, APIs. The amber loop in the
middle is where the actual work happens. And here is the key point:
agentic is not a smarter ChatGPT. It's a difference in kind, not in
size. The model can touch the world, and it can check its own work.
Keep this image in your head — it's the whole lecture in one
picture.
-->

---

## The parts: model · harness · loop

![h:270](img/model-harness-loop.svg)

**Harnesses (2026):** pi, OpenCode, Claude Code — same model, different results. The harness decides.

*(Disclosure: pi is my own project.)*

<!-- notes:
⏱ ~2.5 min · READ ALOUD

Three parts. The model — you know this one, it's the brain. The
harness — that's the piece this lecture adds: an executable
environment, permissions, memory — the hands and the workspace.
And the loop — that's what makes it agentic: it plans, it acts, it
checks, it corrects itself. Two honest asides. First: there's a
fourth ingredient that is deliberately not on this diagram —
context, the criteria and judgement the loop cannot invent for
itself. That's yours, and it comes back in two slides. Second, full
disclosure: pi, the harness you'll see in the demo, is my own
project. I use it mainly because it has a small memory footprint.
OpenCode and Claude Code are solid alternatives. Same model,
different results — the harness decides.
[Not read:] If asked later — pi default is memory footprint, not
"my software is better"; keep it honest, students test this.
-->

---

<!-- _class: smaller -->

## Why now — the evidence inside the research corpus

The chair's open corpus (marketing-research, public on GitHub): **13,096 papers — 7,771 published in 2026 alone**

| Signal | Count |
|---|---|
| Papers mentioning **agentic AI** | 91 |
| Papers on **lead generation** | 27 |
| **Both** (agentic × lead-gen) | **0** |
| Papers on **context-aware** marketing | 22 |

> Context-aware marketing exists. Agentic lead generation doesn't. Nobody connects the two yet.

<!-- notes:
⏱ ~1.5 min · READ ALOUD

Why now? Let me show you the evidence — from this chair's own open
research corpus, public on GitHub. Thirteen thousand and ninety-six
marketing papers. Seven thousand seven hundred and seventy-one of
them published in 2026 alone. Ninety-one papers mention agentic AI.
Twenty-seven papers are about lead generation. And the intersection
— papers that do both? Zero. Literally zero. Twenty-two papers are
context-aware — but they all stay in attribution and
personalisation; none of them touch agentic work. So the triple
intersection is empty. Nobody is doing this yet — and that empty
cell is this chair's to fill.
[Not read — honesty note if probed:] Counts come from keyword search
over title/abstract of our own corpus — a heuristic, not a citation
index — but conservative; the gap is real and wide.
-->

---

## How to talk to the machine: prompts vs contracts

![h:360](img/contract-vs-prompt.svg)

> Prompt = asks a chat · Contract = runs an agent · **Context = what the machine can't know**

<!-- notes:
⏱ ~2 min · READ ALOUD

This is the central mental model of the whole lecture — it's the
slide I hope you remember. A prompt? That's how you ask a chat: a
question, in one go, and that's it. A contract? That's how you run
an agent. It lives in the repository, it's versioned, and it says
what 'done' means. And then the third piece, please take it
seriously: context. The contract is a container for context — the
chair's criteria, the sources we trust, our judgement, the history
of partnerships. Without that container, the agent is a brilliant
generalist with no idea what 'good' means here. A prompt turns an
idea-generator into a conversation. A contract turns it into a
reproducible research pipeline.
-->

---

## A lead-generation loop as an agentic workflow

![w:1200](img/leadgen-pipeline.svg)

> Six steps — the agent executes 2–5, you own definition and evaluation. **Those two boxes are where context lives.**

<!-- notes:
⏱ ~3 min · READ ALOUD

Now let's make it concrete — a lead-generation loop as an agentic
workflow. Read it left to right. [point to each box as you say it]
DEFINE — that's you; that's the blue box: what does a good partner
look like for this chair? SOURCE — where do we hunt? QUALIFY —
does this company actually fit? RECORD — capture every claim with
its source. VERIFY — check those sources really say what we think
they say. And OUTPUT — a ranked list, judged by a human. The agent
runs the middle four steps. You own the first and the last — and
you already know why from the slide before: those two boxes are
where the context lives. Notice the amber line along the bottom —
that's what you learn on a run, feeding back to tighten the
contract for the next run. The agent stays inside the loop. The
human stays in charge.
[Not read:] DEFINE injects context (criteria, sector, guard rails);
EVALUATE judges with context (the three questions). Next slide makes
DEFINE concrete — the sector choice, still human work.
-->

---

<!-- _class: smaller -->

## Define the hunt: scoring the sector

Lead generation starts with a **human** decision: *which sector do we hunt?*

| Criterion (1–5) | Mech. & plant engineering | Optics / photonics | Grocery retail |
|---|---|---|---|
| Chair research fit — sales management | 5 | 5 | 2 |
| Course fit — "Sales Strategy and Execution" | 5 | 5 | 2 |
| Regional employers (Mittelhessen) | 5 | 5 | 3 |
| Lead-gen relevance — B2B, long cycles | 5 | 4 | 2 |
| Demo data availability | 4 | 4 | 5 |
| **Total** | **24** | **23** | **14** |

> Hard guard: sector is out if chair fit < 4 **or** lead-gen relevance < 4 — grocery retail (our first default) fails. **Decision: German mechanical & plant engineering.**

<!-- notes:
⏱ ~45 s · READ ALOUD

Before the agent does anything, a human decides where to hunt.
Look at this table: five criteria, scored one to five, and one hard
guard. Our first default — grocery retail — fails the guard,
because lead generation there is a consumer, demand-gen game, not a
sales-strategy one. Optics came close. But mechanical and plant
engineering wins on every axis. So that's the sector you're about
to see in the demo. And notice what just happened: the AI did not
choose the sector. We did. Choosing target segments is a core
sales-strategy decision — one we can teach in the Bachelor course.
[Not read:] This is the DEFINE box made concrete; guards the claim
the walkthrough is human-steered, not agent-chosen.
-->

---

## Now: a live walkthrough

Task: build the **partner-candidate shortlist** — top 10 B2B companies (live today: 2 of them) with:

- Fit signal per company vs. the chair's partnership goals
- Named source URL per claim (citable, verifiable)
- Ranked output — evidence base for the Bachelor course "Sales Strategy and Execution"

I run this live in a harness — what you see is what the agent does.

<!-- notes:
⏱ ~30 s · READ ALOUD

So — the live walkthrough. The task: build the partner-candidate
shortlist, top ten B2B companies. Live today, we'll do two of them
— the method is what matters, not the count. Each company gets a
fit signal in one sentence, every claim carries a source URL, and
the output is ranked. That shortlist is evidence for the Bachelor
course next year. There's no hands-on today — this is a
walkthrough. I run it in the harness live, and what you see is what
the agent does. Watch what happens — and watch what doesn't happen
on screen. Let's go.
-->

---

<!-- _class: smaller -->

## Walkthrough · Step 1 — The contract

```text
AGENTS.md / brief (what the agent reads at start)
Goal:      shortlist of 10 B2B partner candidates for the chair
Criteria:  industry fit, innovation agenda, university links
Sources:   company sites, press, funding registries
Output:    ranked list, every claim with a URL
Rules:     no invented facts; if unsure, mark as unverified
```

> Done means: verified, cited, repeatable.

<!-- notes:
⏱ ~2 min · READ ALOUD

Step one: the contract. This is the file the agent reads every time
it starts — and it's in this repository, you can open it yourself.
Look at what a contract actually contains: a goal, criteria,
sources, an output format, and rules. Now, the natural instinct is
to think you prompt an AI by typing a question. You don't. You
start by writing rules. And one critical-literacy point before we
go on — because it really matters: every source this contract
lists is self-reported by the companies themselves. A URL proves a
claim exists; it does not prove the claim is true. So the standing
question for everything we do today is: whose evidence is this?
[Not read:] The live file is lecture/demo/AGENTS.md; full kickoff
prompt + narration: lecture/demo/demo-script.md.
-->

---

<!-- _class: smaller -->

## Walkthrough · Step 2 — The agent at work

Watch the six-step loop run live:

- **only watch** — no magic, every tick is visible in the terminal
- agent **opens the browser** (MCP), reads real company pages
- scores against **the contract** → markdown table with **URLs**
- **iterates**: pause, correct, re-check — that is the loop

> Nothing happens off-screen — the loop is fully visible.

<!-- notes:
⏱ ~8 min live action — spoken play-by-play, in this order:

[agent starts] "I'm introducing the agent the way I'd introduce a
new colleague: here's the contract, here's the task — show me your
plan first."

[it plans] "Watch the plan — it maps one to one onto those six boxes
from the pipeline slide."

[it opens the browser] "There it is — it can touch the world, that's
what agentic means. It's reading the companies' own pages. Right
now it is absorbing our context — the criteria it could not invent
for itself."

[it scores] "Now it scores each company against the contract — fit
signal, one sentence, with the source right next to it."

[on a mistake — pause, then:] "Hold on. Did you see that? It
over-claimed. Stop. Which URL actually says that?" [let it
correct itself] "That pause-and-correct — that is the loop in
action."

[it re-checks citations] "Now it's re-checking its own citations —
do those URLs actually resolve? That's step five: verify."

[final table] "And there's the shortlist — ranked, cited, done.
Let's judge it with the three questions."
[Not read:] Steps: (1) open browser via MCP, search prospects;
(2) read real pages, extract fit signals; (3) score vs contract;
(4) write markdown table with URLs; (5) re-check citations;
(6) ranked list. Speed beats completeness — cut company two if
running long. Demo runs on real public data via cloud API — never
paste private/customer data. Fallback: no network → play
fallback-demo.mp4 and narrate the same beats over it (see
demo/demo-script.md).
-->

---

## Walkthrough · Step 3 — The three questions

1. **Checked?** Did the agent verify its output, not just generate it?
2. **Citable?** Does every claim have a URL that resolves — and actually supports it?
3. **Repeatable?** Same contract → same method → a result you can re-run and audit?

*The 1–5 scores are a transparent heuristic — each criterion with evidence — not a measurement.*

> All three guard one thing: **context** — invented context (Checked) · untraceable context (Citable) · lost context (Repeatable).

> The final slide of the walkthrough: apply them to the live result.

<!-- notes:
⏱ ~2 min · READ ALOUD

The last step of the walkthrough: judge the output with three
questions. Checked — did the agent verify its output, or did it
just generate it? Citable — does every claim carry a URL that
resolves, and actually supports the sentence? Repeatable — re-run
the same contract and you get the same method: a result you can
audit. And here is what all three are really guarding: context.
Checked guards against invented context. Citable guards against
untraceable context. Repeatable guards against lost context. If the
output passes, it's a deliverable. If not — it's a draft. And that
is the same discipline you'd apply to a prospect's claims before
you sign anything. Verify before you trust.
[Not read:] Repeatability is process-level, not byte-identical
output — models are stochastic, the method is re-runnable. Sales
connection: you verify a prospect's claims before signing.
-->

---

<!-- _class: lead -->

## What you just saw

1. A contract (rules) — not a prompt
2. An agent doing the loop: plan → act → check → correct
3. A verifiable artefact — the ranked shortlist
4. **Context — supplied by you, enforced by the contract, checked by the loop**

**That is the method** — reusable for any partner-sourcing task.

<!-- notes:
⏱ ~1 min · READ ALOUD

So — what did you actually just see? Three things. A contract:
rules, not a prompt. An agent doing a loop: plan, act, check,
correct. And a verifiable artefact: a ranked shortlist, every claim
with a source. And one more thing — the thread of the whole hour.
Context. Supplied by you. Enforced by the contract. Checked by the
loop. That's the method — and it's reusable for any
partner-sourcing task. The result is what a demo produces. The
method is what you take home.
[Not read:] Point to resources slide for how to start trying it
yourself.
-->

---

## What the chair gets out of it

- A reproducible partner-sourcing method (not a one-off search)
- A ranked, sourced shortlist — usable immediately
- Students who can run agentic workflows (a real skill for the CV)
- Evidence base for the **Bachelor course "Sales Strategy and Execution"** (SS 2027)

> The lecture is not the output. The shortlist is.

<!-- notes:
⏱ ~1.5 min · READ ALOUD

Fair question: what does the chair get out of this? Four things.
First, a reproducible partner-sourcing method — not a one-off
search. Second, a ranked, sourced shortlist — usable immediately.
Third, students who can run agentic workflows — and I mean that
seriously as a CV skill; that's what companies are hiring for right
now. And fourth, an evidence base for the Bachelor course Sales
Strategy and Execution next summer. One honest note on the side:
everything here is open and reusable — you can take this method
into internships and theses. The lecture is not the output. The
shortlist is.
-->

---

<!-- _class: smaller -->

## Key AI providers — what you can use as a student

| Provider / offer | What you get | Where |
|---|---|---|
| **JLU HRZ API-Service** ⭐ | LLMs for all JLU members: free local Qwen models (256K–1M ctx) + commercial, works with OpenCode / Claude Code | [uni-giessen.de → HRZ → KI → API-Service](https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service) · access via **ki@uni-giessen.de** |
| **Google AI student plan** | 1 year Google AI **Plus** free · Gemini, higher limits, 400 GB | [one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75) — verify via SheerID (student status) |
| **OpenRouter** | one API key → many models (OpenAI, Anthropic, Google, open) · free models + pay-as-you-go | [openrouter.ai](https://openrouter.ai) |
| **Harnesses** | the tools from today's demo — **OpenCode**, pi *(full disclosure: pi is my own project)* — work with any key above | [opencode.ai](https://opencode.ai) · [pi.dev](https://pi.dev) |
| **Local models (Ollama)** | free, run on your own laptop, no account, private | [ollama.com](https://ollama.com) |

> Start with **HRZ API**: free for JLU members · Google deal expires **Dec 31, 2026**.

<!-- notes:
⏱ ~1.25 min · READ ALOUD

So what can you use, as a student, starting tomorrow? Best option
first: the JLU HRZ API-Service. Free LLMs for every university
member — locally hosted Qwen models with up to a million tokens of
context, plus the commercial models on top. You get access by
emailing ki@uni-giessen.de, and it works with OpenCode out of the
box. Google gives students a year of Google AI Plus for free —
verify with your university email by the end of December. OpenRouter
is one key for many models, free tiers included. Ollama runs
locally — free and private. And the harnesses, OpenCode and pi,
are what you've seen today. If you take one thing from this slide:
start with HRZ.
[Not read — for questions:] Google deal redeem by Dec 31 2026,
SheerID verification; OpenCode via LiteLLM provider block
(baseURL api.hrz.uni-giessen.de) or Claude Code via
ANTHROPIC_BASE_URL.
-->

---

## Take-aways

1. Agentic = working environment, not a chatbot
2. Harness = model + tools + rules = accountable AI work
3. Contract first: define "done" before you start
4. Verify, cite, repeat — the three questions
5. **Context beats compute — the right context contract beats a bigger model**

> Next summer semester: the chair decides what this evidence feeds into
> the Bachelor course "Sales Strategy and Execution".

<!-- notes:
⏱ ~1 min · READ ALOUD

Let me leave you with five lines. Agentic is a working environment,
not a chatbot. A harness is a model plus tools plus rules — that is
what makes AI work accountable. Contract first: define 'done'
before you start. Verify, cite, repeat — the three questions. And
the line I want you to take home: context beats compute. A small
model with your context beats a big model with none. Next summer,
this shortlist becomes the Bachelor course's input — and the chair
decides what it feeds.
[Not read:] Take-away 5 is the portable one-liner; it reframes the
lecture beyond today's demo.
-->

---

## Resources

- **JLU HRZ API-Service** (free LLMs for JLU members) — [uni-giessen.de → HRZ → KI → API-Service](https://www.uni-giessen.de/de/fbz/svc/hrz/svc/services/ki/api-service) · [model overview](https://api.hrz.uni-giessen.de/ui/model_hub_table/)
- **HRZ access one-pager** (student quick start, 1 page) — [`hrz-access-one-pager.md`](hrz-access-one-pager.md)
- **pi** — [pi.dev](https://pi.dev) · docs: [pi.dev/docs](https://pi.dev/docs) *(full disclosure: my own project)* · **OpenCode** — [opencode.ai](https://opencode.ai) · **OpenRouter** (one key, many models) — [openrouter.ai](https://openrouter.ai)
- **Google AI student plan** — [one.google.com/ai-student](https://one.google.com/ai-student?g1_landing_page=75) (1 year free for students)
- **marketing-research** (chair corpus, public) — [github.com/tobias-weiss-ai-xr/marketing-research](https://github.com/tobias-weiss-ai-xr/marketing-research)
- **skeleton-research** (forkable corpus skeleton) — [github.com/tobias-weiss-ai-xr/skeleton-research](https://github.com/tobias-weiss-ai-xr/skeleton-research)
- **This deck** — [`lecture/`](.) in this corpus repo (English, 45 min)

<!-- notes:
⏱ ~30 s · OPTIONAL read — the list stays up on screen either way.

"Everything on this slide is public and reusable — the links are in
the deck. Two are worth starting with: the HRZ API-Service, and the
research corpus itself, which is what today's evidence came from.
Fork it — it's a skeleton you can grow into your own corpus."

[If you only say one sentence:] "All links are in the deck — the
corpus and the one-pager are where I'd start."
[Not read:] Lead with HRZ API-Service (free, university-provided).
Google link repeats the providers slide so it survives sharing.
marketing-research = evidence base of the "why now" slides;
skeleton-research = forkable starter for a student's own curated
corpus; hrz-access-one-pager.md = student quick start.
-->

---

<!-- _class: lead -->

# Thank you!

## Questions?

Tobias Weiß · guest lecture · Marketing Chair

Agentic AI for Lead Generation · 22 Oct 2026 · 45 min

<!-- notes:
⏱ 10 min Q&A — closing words first, then moderation.

[Closing, ~15 s · READ ALOUD:] "Thank you for listening — and for
the questions you've banked. Let's hear them, one at a time."

[Each answer — keep it short, one idea, then ask the next person.]
Prepared answers you're likely to reach for:

- Model choice — the demo runs on **big pickle**; the harness is
  model-agnostic — pi switches model with Ctrl+L. Cost is why we
  pick cheap models with tight contracts, not size.
- "Is this just a fancy search engine?" — search returns matches;
  this returns judgements, because the contract carries the chair's
  context and every judgement is source-traceable. Context is the
difference — and it's yours, not the model's.
- "Is the output reproducible?" — same contract, same method:
auditable, re-runnable; never promised byte-identical, models are
stochastic.
- Data privacy — local models (Ollama, HRZ Qwen) if it matters;
  today's demo is public data only.
- "What does qualified mean?" — defined in the contract: fit
  signal, innovation agenda, university links, each with evidence.
- Trying it themselves — resources slide; start with HRZ API.

[Hard stop at 16:00 — the course's Übung starts in this room right
after; the ten minutes belong to the students, never overrun.]
-->
