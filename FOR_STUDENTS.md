# 🎓 For Marketing Students — Getting Real Value Out of This Repo

> A short onboarding path. If you only read one thing in this repo, read this.

This repository is a **curated, living collection of ~14,000 marketing research
papers** — plus the reports, tools, and teaching materials built on top of it.
It is designed so that a marketing student can go from "what is this?" to
"here is my evidence-based answer to a real marketing question" in one sitting.

**You do not need to be technical to use most of it.** Two of the three entry
points below are click-and-browse. The command-line tools are optional power-ups
for coursework and for anyone curious about how such a corpus is built.

---

## 1. What this repo is (in one picture)

```
papers.yaml ──► (auto-built) ──► reports + tools + browser
  source of truth                |
  14,000 papers                  ├─ 📊 docs/research/  literature review, trends, concept map
  11 marketing categories        ├─ 🔎 docs/index.html searchable paper browser
  6 research lenses              ├─ 🧭 tools/          topic/trend/gap/brief generators
                                 └─ 📚 PAPERS.md      full paper list, grouped & by year
```

The **paper database** is the heart. Everything else helps you find, understand,
and cite the right papers for a question.

---

## 2. Three ways in (pick one)

### 🅰️ The searchable browser — *easiest, no setup*
Open **[docs/index.html](docs/index.html)** in any browser. Search by keyword,
filter by category (e.g. *AI & Marketing*) and lens (e.g. *Empirical Studies*),
click through to the original paper. This is the fastest way to start.

### 🅱️ The curated reports — *read like a literature review*
Read the auto-generated synthesis of the whole corpus:

| Report | What it answers |
|---|---|
| [docs/research/literature_review.md](docs/research/literature_review.md) | What are the 11 marketing categories, how big is each, what's the recent momentum, where are the research gaps? |
| [docs/research/trends.md](docs/research/trends.md) | Which topics are bursting right now (last 12 months)? |
| [docs/research/concept_map.md](docs/research/concept_map.md) | How do the big concepts connect (e.g. *AI & Marketing* ↔ *framework*)? |

### 🅲 The command-line tools — *power for coursework & the curious*
Requires Python (see [README → Quick Start](README.md#-quick-start)). Four tools
turn the corpus into ready-made outputs:

```bash
# 1. What are the hottest marketing topics right now? → docs/topics/ARTICLE_TOPICS.md
python3 tools/topic_planner.py --top 10

# 2. Keyword bursts + fastest-growing areas in the last 12 months
python3 tools/trend_scanner.py --months 12

# 3. Where are the research gaps (thin cells)? → landscape report
python3 tools/landscape_analyzer.py --json

# 4. Build a ready-made brief for any topic (great starting point for an essay)
python3 tools/brief_generator.py "generative AI marketing" --papers 8
python3 tools/brief_generator.py "social media influencer" --as-doc
```

---

## 3. The 11 marketing categories

Every paper is tagged with **one category** (the domain) and **one lens** (the
research aspect: *Empirical, Framework/Model, Review, Case Study, Theory,
Measurement*). That two-tag system is why you can slice the corpus so precisely.

| Category | Focus | Recent momentum |
|---|---|---|
| **AI & Marketing** | generative AI, marketing automation, lead scoring, chatbots | 🔥 very high |
| **Digital & Performance Marketing** | programmatic, performance, campaign effectiveness | 🔥 high |
| **Social Media & Creator Marketing** | influencer, social commerce, UGC, creator economy | 🔥 high |
| **Content & Storytelling** | content marketing, brand narrative | 📈 growing |
| **Consumer Behavior & Psychology** | online purchase intent, engagement, personalization | 🔥 high |
| **Brand Strategy & Management** | brand equity, loyalty, purpose | 🔥 high |
| **Analytics, Attribution & Measurement** | MMM, attribution, marketing analytics | 📈 growing |
| **Data, Privacy & Cookieless Advertising** | cookieless, first-party data, privacy trade-offs | 📈 growing |
| **Customer Experience, Omnichannel & Retail** | omnichannel, customer journey, retail media | 📈 growing |
| **B2B & Account-Based Marketing** | account-based, buyer journey, B2B contextual | 📈 smaller, fast-rising |
| **Surveys, Trends & Meta-Studies** | literature reviews, meta-analyses, bibliometrics | 🔥 very high |

*Momentum reflects the last-12-months burst in the corpus (see trends report).*

---

## 4. Curated reading path: pick a topic, start here

**Fastest start:** open the
**[curated starter reading list](docs/students/starter_reading_list.md)** —
a hand-picked, high-quality set of papers for each of the 11 categories
(from reputable journals, all real and linkable). Read the *Review* first for
an overview, then the *Empirical* papers for evidence.

For a one-page framing of each category (what it's about, the questions it
answers, where to start, and the open gap worth a thesis), read the
**[topic briefs](docs/students/topic_briefs.md)**.

For any coursework or research question, a reliable method:

1. **Open the [browser](docs/index.html)** and filter to your category + lens
   (start with *Review* for an overview, then *Empirical* for evidence).
2. **Read the relevant generated report** to situate your topic.
3. **Run `brief_generator`** to get a formatted, citable starting brief.
4. **Check the hand-authored `paper/` documents** for the most developed
   thinking on a topic (see below) — especially the research-gap analyses.

### Deep-dive hand-authored papers (`paper/`)

Beyond the auto-generated reports, several hand-authored documents explore the
**open research questions** the corpus exposes. These are the most thought-through
pieces in the repo and are a goldmine for thesis/framing inspiration:

| Document | What it is |
|---|---|
| [paper/gaps_deep_dive.md](paper/gaps_deep_dive.md) | Ranks the biggest research gaps in the corpus across 8 criteria — a ready-made "what is unanswered" map |
| [paper/g4_situational_awareness_framework.md](paper/g4_situational_awareness_framework.md) | A proposed framework: *Context-Aware Agentic Marketing (CAM)* — how AI agents could get marketing "situational awareness" |
| [paper/g6_b2b_contextual_intelligence.md](paper/g6_b2b_contextual_intelligence.md) | A proposed framework for B2B marketing: firmographic, buying-situation, and journey-stage context |
| [paper/g6_haas_integration.md](paper/g6_haas_integration.md) | B2B framework anchored to real, verified scholarship (also a great example of *not* fabricating citations) |
| [paper/cam_sim.py](paper/cam_sim.py) | A Python **simulation benchmark** that models the CAM framework — see how a conceptual framework becomes testable |

### Example: "Is AI really changing marketing?"

1. Browser → category **AI & Marketing**, lens **Review** → skim 5–10 recent reviews.
2. Read [docs/research/literature_review.md](docs/research/literature_review.md#ai--marketing) for the category summary.
3. Run `python3 tools/brief_generator.py "generative AI marketing" --papers 8`.
4. Read the [CAM framework](paper/g4_situational_awareness_framework.md) for a forward-looking angle.

---

## 5. Honest notes on reading this corpus (important!)

- **Volume ≠ quality.** ~14,000 papers includes many low-signal entries (auto-ingested
  conference/journal dumps). The *lens* filter (especially **Review**) and the
  curated reports are your quality shortcut.
- **Prefer reviews for your literature-review sections.** For evidence claims, go
  to **Empirical** papers. For "what could be", read the `paper/` frameworks.
- **Verify before you cite.** The repo links to the original paper — always open
  and read the source. Some entries are light on abstract detail.
- **Gaps are research opportunities.** The thinnest cells (e.g. `b2b/measurement`)
  are where the most interesting, less-saturated thesis topics tend to live.
- **Some corpus signals look odd** (e.g. the "world model"/"teaming" keyword bursts)
  because auto-classification can catch tangentially-related papers. Always ground
  claims in the papers themselves, not just the numbers.

---

## 6. Citing papers from this corpus

Cite the **original paper**, not this repo. Each entry in [PAPERS.md](PAPERS.md)
or the [browser](docs/index.html) links to the source (`[paper](url)`). For the
corpus itself as a resource, use the `@software` citation in the
[README → Citation](README.md#-citation) section.

---

## 7. The guest-lecture materials (`lecture/`)

If you're here from the marketing chair's **Agentic AI for Lead Generation**
guest lecture, the slides and demo live in [lecture/](lecture/README.md):
- Slides (Markdown/HTML/PDF/PPTX) — `lecture/agentic-ai-for-lead-generation.*`
- The **live demo kit** — how an AI agent builds a ranked partner-company
  shortlist: contract ([`lecture/demo/demo-script.md`](lecture/demo/demo-script.md)),
  target format ([`lecture/demo/shortlist-template.md`](lecture/demo/shortlist-template.md)),
  and the full walkthrough script.
- The "why now" claim of the lecture is backed by this corpus's trends report.

---

## 8. Want to go deeper?

- **Guided assignments** with rubrics: [docs/students/assignments.md](docs/students/assignments.md) (5 tasks, 2–4 h each)
- **How to write a literature review** with this corpus: [docs/students/how_to_lit_review.md](docs/students/how_to_lit_review.md)
- Full paper list (every entry, grouped & by year): **[PAPERS.md](PAPERS.md)**
- How the corpus is built and kept fresh: [README.md](README.md) and `AGENTS.md`
- The data is machine-readable in `docs/papers.json` (great for a data/analytics
  course or a bit of Python).
- Tools can output JSON (`--json`) for further analysis.

> **Tip:** The fastest way to impress in a methods seminar is to show the pipeline
> itself — take one topic, run `topic_planner` + `brief_generator`, and explain
> how ~14,000 papers become a focused, cited answer.
