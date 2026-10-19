<h1 align="center">
  <strong>Marketing Research Corpus</strong>
</h1>
<h3 align="center">~14,000 papers · AI & generative marketing, digital & performance, social & creator, privacy-first data, analytics/MMM, B2B/ABM — browsable, reported, and tooled for teaching</h3>

> 🎓 **Are you a marketing student?** Start with **[FOR_STUDENTS.md](FOR_STUDENTS.md)** — a short, non-technical onboarding path to browsing papers, reading the reports, and using the tools for coursework.

> 🎤 **Teaching:** Guest lecture *Agentic AI for Lead Generation* (45 min, EN, marketing chair) — see [`lecture/`](lecture/README.md).

<p align="center">
  <img src="https://raw.githubusercontent.com/tobias-weiss-ai-xr/marketing-research/main/assets/visualizations/category_distribution.png" alt="Teaser" width="600" />
</p>

---

## 🧭 Navigate

| If you want to… | Go here |
|-----------------|---------|
| 🎓 **Onboard fast (students)** | **[FOR_STUDENTS.md](FOR_STUDENTS.md)** — value path + curated reading paths |
| 📚 **Curated starter papers** | [docs/students/starter_reading_list.md](docs/students/starter_reading_list.md) — hand-picked high-quality papers per category |
| 🧭 **Per-topic briefs** | [docs/students/topic_briefs.md](docs/students/topic_briefs.md) — one-page framing + thesis gaps per category |
| 🔎 **Search & filter papers** | [docs/index.html](docs/index.html) — interactive browser |
| 📚 **Read the full paper list** | [PAPERS.md](PAPERS.md) — every entry grouped by category & year |
| 📊 **Read the corpus synthesis** | [docs/research/literature_review.md](docs/research/literature_review.md) · [trends.md](docs/research/trends.md) · [concept_map.md](docs/research/concept_map.md) |
| 🧭 **Generate topics/trends/briefs** | `tools/topic_planner.py` · `trend_scanner.py` · `landscape_analyzer.py` · `brief_generator.py` |
| 📄 **Deep-dive research papers** | `paper/` — gap analysis, AI-marketing & B2B frameworks, CAM simulation |
| 🎤 **Guest-lecture materials** | [lecture/](lecture/README.md) |

## 🚀 Quick Start (developers / the curious)

```bash
# 1. Clone
git clone https://github.com/tobias-weiss-ai-xr/marketing-research.git
cd marketing-research

# 2. Install dependencies
pip install -r requirements.txt

# 3. Validate + generate
python3 scripts/validate_papers.py
python3 scripts/generate_readme.py
python3 scripts/standard_stats.py
python3 scripts/analysis/generate_reports.py
```

## ⚙️ What's inside

| Capability | How |
|------------|-----|
| 📄 **Curated corpus** | `papers.yaml` is the source of truth — one structured entry per paper |
| 🔍 **Literature review report** | `scripts/analysis/generate_reports.py` → `docs/research/literature_review.md` + `trends.md` |
| 📊 **Statistics & trends** | `scripts/standard_stats.py` → `statistics.json` (momentum, gaps, bursts, venues, authors) |
| 🧭 **Topic planning** | `tools/topic_planner.py`, `tools/trend_scanner.py`, `tools/landscape_analyzer.py`, `tools/brief_generator.py` |
| 🖥️ **GitHub Pages browser** | `docs/index.html` — searchable, filterable paper browser |
| 🧾 **Auto-generated README** | `scripts/generate_readme.py` renders the paper list grouped by taxonomy |
| ✅ **Auto-validation** | `scripts/validate_papers.py` checks schema, duplicates, URL normalization, LaTeX artifacts |
| 🔎 **New paper discovery** | `scripts/fetch/fetch_new_papers.py` (arXiv), `fetch_other_sources.py` (dblp/crossref/europepmc), `fetch_openalex_bulk.py` |
| 🐙 **GitHub / 🦊 GitLab / 🏠 Codeberg discovery** | `scripts/fetch/fetch_*_repos.py` (optional, config-driven via taxonomy.yaml) |
| 🤖 **Agentic workflow** | `AGENTS.md` + `config/taxonomy.yaml` make this repo agent-friendly by design |

## 📖 How it works

```
config/taxonomy.yaml ──► papers.yaml ──► validate_papers.py
                          │   ▲              │
                          ▼   └── fetch_* ───┘
                   generate_readme.py ──► README.md (auto), PAPERS.md, docs/papers.json
                          │
                          ▼
                  standard_stats.py ──► statistics.json, assets/graph_analysis.json
                          │
                          ▼
              analysis/generate_reports.py ──► docs/research/*.md
```

- **Do not edit generated outputs by hand** — `README.md`, `PAPERS.md`,
  `docs/papers.json`, `statistics.json`, and `docs/research/*.md` are rebuilt
  from `papers.yaml` and the scripts above. `papers.yaml` is the single source
  of truth for the corpus.
- The **taxonomy lives in one place** (`config/taxonomy.yaml`); every script reads it via `scripts/research_config.py`.
- **CI (validate.yml)** runs on every push/PR and weekly to discover new papers.

## 🧪 Local pipeline (all in one)

```bash
# Full pipeline (validate → README → stats → reports)
python3 scripts/validate_papers.py && \
python3 scripts/generate_readme.py && \
python3 scripts/standard_stats.py && \
python3 scripts/analysis/generate_reports.py
```

## 🤖 Agentic workflow (AGENTS.md)

This repo is designed to be driven by coding agents (OpenCode, Claude Code, …):

- **Spec-style guardrails** in `AGENTS.md` — agents know the pipeline, never edit generated outputs, always re-validate.
- **One config file** to change → one re-run to verify (low context cost for agents).
- **Auto-validation** gives agents an objective pass/fail signal.
- **Weekly discovery** keeps the corpus fresh without human babysitting.

## 📊 Corpus Statistics

**14,052 papers** across **11 categories**.
Sources: **arXiv** 1040 (7%) · **DOI** 11903 (85%) · **Other** 1109 (8%).
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/marketing-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-
| AI & Marketing | **2938** | 1732 | ████████████ |
| Surveys, Trends & Meta-Studies | **2068** | 1645 | ████████░░░░ |
| Social Media & Creator Marketing | **1571** | 1060 | ██████░░░░░░ |
| Consumer Behavior & Psychology | **1533** | 1031 | ██████░░░░░░ |
| Digital & Performance Marketing | **1501** | 1010 | ██████░░░░░░ |
| Brand Strategy & Management | **1456** | 1025 | ██████░░░░░░ |
| Customer Experience, Omnichannel & Retail | **1116** | 731 | █████░░░░░░░ |
| Analytics, Attribution & Measurement | **581** | 354 | ██░░░░░░░░░░ |
| Content & Storytelling | **491** | 266 | ██░░░░░░░░░░ |
| Data, Privacy & Cookieless Advertising | **449** | 215 | ██░░░░░░░░░░ |
| B2B & Account-Based Marketing | **348** | 179 | █░░░░░░░░░░░ |

## 📚 Paper list

All **14052 papers** (grouped by category, subcategory and year) live in **[PAPERS.md](PAPERS.md)** — kept out of this README to keep it readable.

Browsable alternatives:

- [PAPERS.md](PAPERS.md) — full list, same grouping as before
- [docs/index.html](docs/index.html) — interactive paper browser
- [docs/papers.json](docs/papers.json) — machine-readable


## 📖 Citation

If you use this corpus in your work, please cite:

```bibtex
@software{marketing_research,
  author = {Tobias Weiss},
  title = {Marketing Research Corpus},
  year = {2026},
  url = {https://github.com/tobias-weiss-ai-xr/marketing-research},
}
```

## 📄 License

MIT — see [LICENSE](LICENSE).
