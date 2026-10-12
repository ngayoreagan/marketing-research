<h1 align="center">
  <strong>Marketing Research Corpus</strong>
</h1>
<h3 align="center">Latest marketing trends: AI & generative marketing, digital/performance, social & creator, privacy-first data, analytics/MMM, B2B/ABM</h3>

### 🔗 Links

- **GitHub**: https://github.com/tobias-weiss-ai-xr/marketing-research
- **License**: https://github.com/tobias-weiss-ai-xr/marketing-research/blob/main/LICENSE
- **CI**: https://github.com/tobias-weiss-ai-xr/marketing-research/actions/workflows/validate.yml
- **AI Literacy**: https://github.com/tobias-weiss-ai-xr/ai-literacy-research


> 📢 **Marketing research corpus:** AI & generative marketing, digital & performance,
> social media & creator economy, content marketing, consumer behavior, brand,
> analytics, privacy-first data, CX & retail, B2B/ABM — analyzed with the same
> pipeline as the other `*-research` corpus repos.

> 🎓 **Teaching:** Guest lecture *Agentic AI for Lead Generation* (45 min, EN, marketing chair) — see [`lecture/`](lecture/README.md).

<p align="center">
  <img src="https://raw.githubusercontent.com/tobias-weiss-ai-xr/marketing-research/main/assets/visualizations/category_distribution.png" alt="Teaser" width="600" />
</p>

---

## What you get

| Capability | How |
|------------|-----|
| 📄 **Curated corpus** | `papers.yaml` is the source of truth — one structured entry per paper |
| ✅ **Auto-validation** | `scripts/validate_papers.py` checks schema, duplicates, URL normalization, LaTeX artifacts |
| 🧾 **Auto-generated README** | `scripts/generate_readme.py` renders the paper list grouped by your taxonomy |
| 📊 **Statistics & trends** | `scripts/standard_stats.py` → `statistics.json` (momentum, gaps, bursts, venues, authors) |
| 🔍 **Literature review report** | `scripts/analysis/generate_reports.py` → `docs/research/literature_review.md` + `trends.md` |
| 🧭 **Topic planning** | `tools/topic_planner.py`, `tools/trend_scanner.py`, `tools/landscape_analyzer.py`, `tools/brief_generator.py` |
| 🔎 **New paper discovery** | `scripts/fetch/fetch_new_papers.py` (arXiv), `fetch_other_sources.py` (dblp/crossref/europepmc), `fetch_openalex_bulk.py` |
| 🐙 **GitHub repos discovery** | `scripts/fetch/fetch_github_repos.py` (optional, config-driven via `github_queries` in taxonomy.yaml) |
| 🦊 **GitLab projects discovery** | `scripts/fetch/fetch_gitlab_repos.py` (optional, config-driven via `gitlab_queries` in taxonomy.yaml) |
| 🏠 **Codeberg repos discovery** | `scripts/fetch/fetch_codeberg_repos.py` (optional, config-driven via `codeberg_queries` in taxonomy.yaml) |
| 🖥️ **GitHub Pages site** | `docs/index.html` — searchable, filterable paper browser |
| 🤖 **Agentic workflow** | `AGENTS.md` + `config/taxonomy.yaml` make this repo agent-friendly by design |

## 🚀 Quick Start

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

## 📖 How it works

```
config/taxonomy.yaml ──► papers.yaml ──► validate_papers.py
                          │   ▲              │
                          ▼   └── fetch_* ───┘
                   generate_readme.py ──► README.md (auto)
                          │
                          ▼
                  standard_stats.py ──► statistics.json, docs/papers.json
                          │
                          ▼
              analysis/generate_reports.py ──► docs/research/*.md
```

- **Never edit README.md directly** — it is generated from `papers.yaml`.
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

- **Spec-style guardrails** in `AGENTS.md` — agents know the pipeline, never edit README, always re-validate.
- **One config file** to change → one re-run to verify (low context cost for agents).
- **Auto-validation** gives agents an objective pass/fail signal.
- **Weekly discovery** keeps the corpus fresh without human babysitting.

## 📊 Corpus Statistics

**13,765 papers** across **11 categories**.
Sources: **arXiv** 787 (6%) · **DOI** 11871 (86%) · **Other** 1107 (8%).
Full paper list: [GitHub Pages site](https://tobias-weiss-ai-xr.github.io/marketing-research).

### Top categories

| Category | Papers | Recent | |
|----------|--------|--------|-
| AI & Marketing | **2682** | 1496 | ████████████ |
| Surveys, Trends & Meta-Studies | **2068** | 1645 | █████████░░░ |
| Social Media & Creator Marketing | **1567** | 1056 | ███████░░░░░ |
| Consumer Behavior & Psychology | **1523** | 1021 | ███████░░░░░ |
| Digital & Performance Marketing | **1486** | 995 | ███████░░░░░ |
| Brand Strategy & Management | **1456** | 1025 | ███████░░░░░ |
| Customer Experience, Omnichannel & Retail | **1116** | 731 | █████░░░░░░░ |
| Analytics, Attribution & Measurement | **581** | 354 | ███░░░░░░░░░ |
| Content & Storytelling | **491** | 266 | ██░░░░░░░░░░ |
| Data, Privacy & Cookieless Advertising | **448** | 214 | ██░░░░░░░░░░ |
| B2B & Account-Based Marketing | **347** | 178 | ██░░░░░░░░░░ |

## 📚 Paper list

All **13765 papers** (grouped by category, subcategory and year) live in **[PAPERS.md](PAPERS.md)** — kept out of this README to keep it readable.

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
