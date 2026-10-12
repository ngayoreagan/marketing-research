#!/usr/bin/env python3
"""Generate README.md and docs/papers.json from papers.yaml.

Generic for any *-research corpus: categories/subcategories and their display
names come from config/taxonomy.yaml (via research_config).

Usage:
    python3 scripts/generate_readme.py
    python3 scripts/generate_readme.py --check   # CI: fail if out of date
"""

STATS_ONLY = False  # Set True to skip full paper list generation
import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

import research_config


def _twelve_months_ago(now):
    y, m = now.year, now.month - 12
    while m <= 0:
        y -= 1
        m += 12
    return (y, m)


def _date_in(datestring, lo, end):
    if not datestring:
        return False
    try:
        y, m = int(datestring[:4]), int(datestring[5:7])
        return (y, m) >= lo and (y, m) < end
    except (ValueError, AttributeError):
        return False


def render_stats_section(papers, cfg):
    """Render the Corpus Statistics section from papers.yaml (not cached)."""
    total = len(papers)
    arxiv_n = sum(1 for p in papers if "arxiv" in p.get("url", ""))
    doi_n = sum(1 for p in papers
                if "doi.org" in p.get("url", "") or p.get("url", "").startswith("10."))
    other_n = total - arxiv_n - doi_n

    def pct(n):
        return round(n / total * 100) if total else 0

    cur_lo = _twelve_months_ago(datetime.now(timezone.utc))

    def is_recent(p):
        return _date_in(p.get("date", ""), cur_lo, (9999, 1))

    cat_count = Counter(p.get("category", "unknown") for p in papers)
    cat_recent = Counter(p.get("category", "unknown") for p in papers if is_recent(p))
    cats = [c for c in research_config.get_categories(cfg) if c["id"] in cat_count]
    cats.sort(key=lambda c: -cat_count[c["id"]])
    max_n = max((cat_count[c["id"]] for c in cats), default=0)

    lines = [
        "## 📊 Corpus Statistics",
        "",
        f"**{total:,} papers** across **{len(cats)} categories**.",
        (
            f"Sources: **arXiv** {arxiv_n} ({pct(arxiv_n)}%) · **DOI** {doi_n} ({pct(doi_n)}%) · "
            f"**Other** {other_n} ({pct(other_n)}%)."
        ),
        (
            "Full paper list: [GitHub Pages site]"
            "(https://tobias-weiss-ai-xr.github.io/marketing-research)."
        ),
        "",
        "### Top categories",
        "",
        "| Category | Papers | Recent | |",
        "|----------|--------|--------|-",
    ]
    for c in cats:
        n = cat_count[c["id"]]
        r = cat_recent[c["id"]]
        filled = round(n / max_n * 12) if max_n else 0
        bar = "█" * filled + "░" * (12 - filled)
        name = c.get("display", c["id"])
        lines.append(f"| {name} | **{n}** | {r} | {bar} |")
    return "\n".join(lines)


def render_paper_list(papers, cfg):
    lines = ["## 📚 Paper list", ""]

    cats = research_config.get_categories(cfg)
    subs = research_config.get_subcategories(cfg)

    # Emoji TOC
    for cat in cats:
        cat_display = cat.get("display", cat["id"])
        cat_anchor = cat_display.lower().replace(" ", "-")
        lines.append(f"- [📚 {cat_display}](#{cat_anchor})")
        for sub in subs:
            group = [p for p in papers if p["category"] == cat["id"] and p["subcategory"] == sub["id"]]
            if not group:
                continue
            sub_display = sub.get("display", sub["id"])
            sub_anchor = sub_display.lower().replace(" ", "-")
            lines.append(f"  - [{sub_display}](#{sub_anchor})")
    lines.append("")

    for cat in cats:
        cat_display = cat.get("display", cat["id"])
        lines.append(f"### {cat_display}")
        lines.append("")

        for sub in subs:
            group = [p for p in papers if p["category"] == cat["id"] and p["subcategory"] == sub["id"]]
            if not group:
                continue

            sub_display = sub.get("display", sub["id"])
            lines.append(f"#### {sub_display}")
            lines.append("")

            # Group by year
            year_groups = defaultdict(list)
            for p in group:
                year = p["date"][:4]
                year_groups[year].append(p)

            for year in sorted(year_groups.keys(), reverse=True):
                lines.append(f"##### {year}")
                lines.append("")

                sorted_papers = sorted(year_groups[year], key=lambda p: p["date"], reverse=True)
                for p in sorted_papers:
                    y = p["date"][:4]
                    title = p["title"]
                    url = p["url"]
                    venue = p.get("venue", "")
                    code_url = p.get("code_url", "")
                    project_url = p.get("project_url", "")

                    entry = f"- [{y}] **{title}**"
                    if venue:
                        entry += f" *{venue}*"
                    entry += f" [[paper]({url})]"
                    if code_url:
                        entry += f" [[code]({code_url})]"
                    if project_url:
                        entry += f" [[project]({project_url})]"
                    lines.append(entry)

                lines.append("")

            lines.append("[⬆ Back to top](#paper-list)")
            lines.append("")

    return "\n".join(lines)


def generate_readme(papers, readme_path, cfg, check_mode=False):
    readme_text = readme_path.read_text(encoding="utf-8")

    start_marker = "## 📚 Paper list"  # (paper list replaced with stats)
    end_marker = "## 📖 Citation"  # (paper list replaced with stats)

    start_idx = readme_text.find(start_marker)
    end_idx = readme_text.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(
            "Error: Could not find paper list or citation section in README.md",
            file=sys.stderr,
        )
        sys.exit(1)

    stats_start_idx = readme_text.find("## 📊 Corpus Statistics")
    if stats_start_idx == -1:
        stats_start_idx = start_idx
    head = readme_text[:stats_start_idx]

    # Refresh the Corpus Statistics section too — it previously went stale
    # (7,521 vs 13,096) because it sat in the preserved prefix.
    before = head + render_stats_section(papers, cfg) + "\n\n"
    after = readme_text[end_idx:]

    # Full list lives in PAPERS.md (README would be >2 MB otherwise);
    # README keeps only a pointer.
    papers_md_path = readme_path.parent / "PAPERS.md"
    papers_md_path.write_text(
        "# 📚 Paper list\n\n"
        f"{len(papers)} papers · generated from `papers.yaml` — do not edit by hand.\n\n"
        + render_paper_list(papers, cfg)[len("## 📚 Paper list\n") :]
        + "\n",
        encoding="utf-8",
    )
    print(f"Generated {papers_md_path}")

    n = len(papers)
    generated_list = (
        f"## 📚 Paper list\n\n"
        f"All **{n} papers** (grouped by category, subcategory and year) live in "
        f"**[PAPERS.md](PAPERS.md)** — kept out of this README to keep it readable.\n\n"
        "Browsable alternatives:\n\n"
        "- [PAPERS.md](PAPERS.md) — full list, same grouping as before\n"
        "- [docs/index.html](docs/index.html) — interactive paper browser\n"
        "- [docs/papers.json](docs/papers.json) — machine-readable\n\n"
    )
    new_readme = before + generated_list + "\n" + after

    if check_mode:
        if new_readme == readme_text:
            print("README.md is up-to-date.")
            sys.exit(0)
        else:
            print(
                "README.md is out-of-date. Run generate_readme.py without --check to update.",
                file=sys.stderr,
            )
            sys.exit(1)

    readme_path.write_text(new_readme, encoding="utf-8")
    print(f"Generated {readme_path}")


def generate_json(papers, json_path):
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(
        json.dumps({"papers": papers}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Generated {json_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate README.md and papers.json from papers.yaml"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check if README is up-to-date (exit 1 if not)",
    )
    parser.add_argument(
        "--skip-json", action="store_true", help="Skip generating papers.json"
    )
    parser.add_argument(
        "--skip-readme", action="store_true", help="Skip regenerating README.md (write papers.json only)"
    )
    args = parser.parse_args()

    base = Path(__file__).parent.parent
    papers_yaml = base / "papers.yaml"
    readme_path = base / "README.md"
    json_path = base / "docs" / "papers.json"

    papers = research_config.load_papers(papers_yaml)
    cfg = research_config.load_config()

    if not args.skip_readme:
        generate_readme(papers, readme_path, cfg, check_mode=args.check)

    if not args.check and not args.skip_json:
        generate_json(papers, json_path)


if __name__ == "__main__":
    main()
