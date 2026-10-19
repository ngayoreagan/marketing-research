# AGENTS.md — Partner-Candidate Shortlist for the Marketing Chair

## Goal

Build a **ranked shortlist of 2 B2B partner-candidate companies** from the
**German mechanical & plant engineering sector** — one global market leader,
one Mittelstand specialist. Client: the marketing chair at Justus-Liebig
Universität Gießen (research co-operations, teaching cases, funded projects).

## Scope — fixed by the human, do not re-decide

- **Sector:** mechanical and plant engineering (Maschinenbau / Anlagenbau)
- **Geography:** Germany; preference for Hessen / Mittelhessen employers
- **Why:** strongest fit to the chair's research (sales management, B2B, long
  sales cycles) and to the Bachelor course "Sales Strategy and Execution"
- If a shortlisted company turns out to be a poor fit, **replace the company** —
  do not switch the sector or the geography.

## Work steps (execute in this order)

1. **Plan** — restate your reading of the contract and outline the source plan
   before you act.
2. **Source** — per company: official site/newsroom, press coverage, funding
   registers, university press releases. Prefer third-party evidence over
   self-reported claims.
3. **Qualify** — score each criterion 1–5 with evidence (rubric below).
4. **Record** — one row per company; every claim linked to its source page.
5. **Verify** — check each URL resolves *and* supports its sentence; fix or
   flag anything that does not.
6. **Output** — the ranked table (format below).

## Criteria (each 1–5; total = sum, max 15)

| Criterion | A 5 looks like | A 1 looks like |
|---|---|---|
| **Industry fit** | core business is industrial B2B machinery sales; clear sales-management relevance | consumer or service business; no machinery link |
| **Innovation agenda** | dated press or careers evidence of AI / IoT / digitalisation within the last 12 months | no public digitalisation signal |
| **University links** | named co-operation, funded chair, doctoral programme, or guest lectures | none found |

Scoring rules:

- Every score needs at least one source; a score without a source is
  `unverified`.
- If sources contradict each other, flag the contradiction in the fit-signal
  cell — do not average.

## Sources

- Official company website and newsroom
- Press coverage (news search)
- Funding registers and university press releases
- **Reminder:** company sources are **self-reported** — they claim, they don't
  prove. Ask: *whose evidence?*

## Output format

- Markdown table: `Rank | Company | Fit signal (1 sentence) | Score | Source URL(s)`
- Sorted by total score, best first.
- Fit signal names the concrete evidence (feature, programme, partnership) —
  not a generic slogan.
- Score column shows `X/15`.
- Source column uses named links with the page as anchor text, e.g.
  `[newsroom](https://…)`.
- Rows you could not verify are written `unverified` — never dropped, never
  invented.

## Rules — definition of done

- **(Checked)** No invented facts; verify claims against sources, then re-check
  citations before finishing.
- **(Citable)** Every claim carries a URL that resolves *and* supports the
  sentence. A URL proves a claim exists, not that it is true.
- **(Repeatable)** Context you do not have — chair history, current
  partnerships, strategic priorities — is marked `unverified`, never guessed,
  so the next run can start from the same honest state.
- If a step fails or blocks, stop and report it — visibility beats a
  finished-looking table.

## Deliverable

One markdown table, ranked, every cell traceable to a URL, ready for a human
judge to check the three questions: **checked? citable? repeatable?**
