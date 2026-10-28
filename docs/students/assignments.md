# 📝 Guided Assignments — Using the Corpus for Coursework

> Ready-to-run tasks for seminars, Bachelor/Master theses, or self-study.
> Each task is sized for **one sitting (2–4 hours)** and produces a
> citable, verifiable deliverable. All tools and data are in this repo.

Pick a task, follow the steps, and cite the **original papers** (never this corpus).

---

## Task 1 — "What is actually happening in [category]?" (2 h)

**Goal:** produce a 1-page briefing on one marketing category.

1. Open the [starter reading list](starter_reading_list.md) and read the *Review* paper for your category.
2. Run:
   ```bash
   python3 tools/topic_planner.py --top 10
   python3 tools/trend_scanner.py --months 12
   ```
3. Read the category section of [docs/research/literature_review.md](../research/literature_review.md).
4. Write 1 page: (a) what the category covers, (b) 3 hottest sub-topics, (c) 1 research gap (use the *Gap/angle* line from [topic_briefs.md](topic_briefs.md)).
5. **Deliverable:** 1-page briefing + 5 cited papers (with URLs).

## Task 2 — "Find the evidence for a claim" (2–3 h)

**Goal:** turn a marketing claim into an evidence-based mini-review.

1. Pick a claim, e.g. *"Generative AI improves marketing content quality."*
2. Run:
   ```bash
   python3 tools/brief_generator.py "generative AI marketing" --papers 10
   python3 tools/brief_generator.py "generative AI marketing" --as-doc
   ```
3. Open the generated brief in `docs/topics/`. Read the abstracts of the top 5 papers.
4. Open the full papers via their URLs. Note: method, sample, finding, limitation.
5. Write 1–2 pages: claim → evidence (for/against) → what is *not* yet known.
6. **Deliverable:** mini-review + evidence table (paper · method · finding · limitation).

## Task 3 — "Spot a research gap" (3–4 h)

**Goal:** identify and justify one under-researched topic.

1. Read [paper/gaps_deep_dive.md](../../paper/gaps_deep_dive.md) — the ranked gap list.
2. Open the [interactive browser](../index.html), filter to the thinnest cell (e.g. `b2b/measurement`).
3. Read 3–5 papers in that cell. Ask: what is missing? (method, context, population, theory?)
4. Frame a research question and a rough method.
5. **Deliverable:** 1-page gap memo (gap · why it matters · proposed RQ · method sketch).

## Task 4 — "Build a mini-corpus" (3–4 h, advanced)

**Goal:** experience the pipeline hands-on.

1. Clone the repo, install deps (`pip install -r requirements.txt`).
2. Add 3 real papers to `papers.yaml` (follow the checklist in [AGENTS.md](../../AGENTS.md)).
3. Run the full pipeline:
   ```bash
   python3 scripts/validate_papers.py && \
   python3 scripts/generate_readme.py && \
   python3 scripts/standard_stats.py && \
   python3 scripts/analysis/generate_reports.py
   ```
4. Confirm validation passes and your papers appear in `PAPERS.md`.
5. **Deliverable:** a 1-paragraph note on what broke / what was confusing — this is the most useful feedback for the maintainers.

## Task 5 — "Data lens" (2 h, analytics track)

**Goal:** use the corpus as a dataset.

1. Load `docs/papers.json` in Python:
   ```python
   import json
   d = json.load(open('docs/papers.json'))['papers']
   from collections import Counter
   print(Counter(p['category'] for p in d))
   ```
2. Answer 3 questions with code: (a) which category grew fastest 2024→2026? (b) which subcategory is thinnest? (c) top 5 venues by paper count?
3. **Deliverable:** a short notebook/script + 3 charts or tables.

---

## Grading rubric (suggested)

| Criterion | Weight | What "good" looks like |
|---|---|---|
| Evidence quality | 40% | Claims trace to specific, opened-and-read papers with URLs |
| Synthesis | 30% | Not a list — a coherent argument with your own framing |
| Gap/angle | 20% | A genuine, defensible opening, not "more research is needed" |
| Reproducibility | 10% | Commands + sources documented so a peer can re-run |

## Tips

- **Start with reviews, then empirical.** Reviews give you the map; empirical papers give you the evidence.
- **Verify before you cite.** Open the original paper; some entries are light on abstract detail.
- **Prefer the thinnest cells** for thesis topics — less saturated, more novel.
- **The corpus is a starting point, not a bibliography.** Quality varies; the curated [starter reading list](starter_reading_list.md) is the shortcut.
