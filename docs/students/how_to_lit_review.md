# 📖 How to Do a Literature Review With This Corpus

> A step-by-step workflow for turning ~15,000 papers into a focused, cited,
> defensible literature review. Written for marketing students; no coding required
> for steps 1–4.

---

## Step 0 — Define your question

Write one sentence: *"This review asks whether X affects Y in context Z."*
Everything below serves that sentence. If you can't write it, you're not ready to search.

## Step 1 — Get the map (15 min, no code)

1. Read the category section of [docs/research/literature_review.md](../research/literature_review.md) for your topic's category.
2. Read the relevant [topic brief](topic_briefs.md) — it gives you the key questions, starter papers, and an open gap.
3. Skim the [starter reading list](starter_reading_list.md) for your category and pick 2–3 *Review* papers.

**Output:** a short list of 3–5 seed papers + 1–2 candidate gaps.

## Step 2 — Build your seed set (30–60 min)

1. Open the [interactive browser](../index.html).
2. Filter to your category + **Review** lens. Sort by date (newest first). Skim 10 titles; open 3.
3. For each seed paper, note: authors, year, method, main finding, limitation.
4. Run:
   ```bash
   python3 tools/brief_generator.py "your topic keywords" --papers 8
   ```
   This gives a formatted, citable starter brief. Read the abstracts; add the strong ones to your seed set.

**Output:** a seed set of 8–12 papers, each with a note.

## Step 3 — Snowball (60–90 min)

From each seed paper, follow:
- **Backward:** its reference list (papers it cites) — you'll find the classics.
- **Forward:** "cited by" on Google Scholar / Semantic Scholar — you'll find the recent work.

Add papers that directly address your question. Stop when new papers stop changing your answer.

## Step 4 — Structure the review (60 min)

A standard structure that works for marketing:

1. **Introduction** — question, scope, why it matters (1 paragraph).
2. **Conceptual background** — define the key constructs (1–2 pages; cite reviews).
3. **Evidence** — what the empirical studies find, grouped by method or moderator (2–4 pages).
4. **Gaps & future research** — what is unanswered (1 page; use [paper/gaps_deep_dive.md](../../paper/gaps_deep_dive.md)).
5. **Conclusion** — your take, with boundaries.

## Step 5 — Quality checks before submission

- [ ] Every claim traces to a paper you opened and read (not just the abstract).
- [ ] You cite the **original paper**, never this corpus.
- [ ] You note limitations of the evidence (small samples, single context, dated).
- [ ] You distinguish "what is known" from "what you believe."
- [ ] Your reference list has no duplicates and all URLs resolve.

## Common pitfalls

- **Treating volume as quality.** ~15,000 papers includes low-signal entries. The *Review* lens + curated reports are your quality shortcut.
- **Citing without reading.** Abstracts mislead. Always open the source.
- **"More research is needed" as a gap.** A real gap names *what* is missing (method, population, theory, context) and *why* it matters.
- **Ignoring the thinnest cells.** The least-covered topics (e.g. `b2b/measurement`) are where novel theses live.
- **Overclaiming from one study.** One paper ≠ a finding; look for replication or meta-analytic support.

## Tools that help

| Tool | Use |
|---|---|
| `tools/brief_generator.py "topic" --papers 8` | formatted starter brief |
| `tools/topic_planner.py --top 10` | hottest topics in the corpus |
| `tools/trend_scanner.py --months 12` | keyword bursts + growing cells |
| `tools/landscape_analyzer.py --json` | full landscape (JSON) |
| [docs/index.html](../index.html) | searchable, filterable browser |
| [docs/research/literature_review.md](../research/literature_review.md) | corpus synthesis |

## Further reading in this repo

- [FOR_STUDENTS.md](../../FOR_STUDENTS.md) — full onboarding path
- [starter_reading_list.md](starter_reading_list.md) — hand-picked papers per category
- [topic_briefs.md](topic_briefs.md) — one-page framing per category
- [assignments.md](assignments.md) — guided tasks with rubrics
- [paper/gaps_deep_dive.md](../../paper/gaps_deep_dive.md) — ranked research gaps
- [paper/g4_situational_awareness_framework.md](../../paper/g4_situational_awareness_framework.md) — AI-marketing framework (example of a forward-looking angle)
