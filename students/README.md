# Student exercise — Ingest & rate partner-candidate leads

You just saw the loop live. Now run it yourself: **find and rate real
partner candidates for the Marketing Chair.** Best submissions join the
chair's actual shortlist for "Sales Strategy and Execution" (SS 2027).

## The task

1. **Fork & clone** this repository.
2. **Ingest 3 leads** — real B2B companies that could partner with the
   chair — into [`leads.yaml`](leads.yaml), following the schema at the
   top of that file.
3. **Score & rank** them with the published rubric (below and in
   `leads.yaml`). Gates first, then the weighted-sum formula.
4. **Validate**: `python3 students/validate_leads.py` must pass.
5. **Submit a pull request.** The chair reviews it like a paper.

## The six boxes — who does what

| Pipeline step | In this exercise |
|---|---|
| DEFINE | fixed: the rubric below (you may *propose* weight changes in your PR — with reasons) |
| SOURCE | you (or your agent): find real companies, read their own pages, press, registries |
| QUALIFY | score each criterion 0–5, with evidence |
| RECORD | every claim gets a source URL that resolves **and** supports the sentence |
| VERIFY | the validator + a human: `validate_leads.py` passing is necessary, not sufficient |
| OUTPUT | ranked table — the chair judges with: checked? citable? repeatable? |

## The rubric

Five criteria, each an integer **0–5**. Gates are hard: a lead that
fails any gate gets `status: rejected` — it stays in the file, it is
never silently dropped.

| Gate (must pass) | Criterion | A **5** looks like | A **1** looks like |
|---|---|---|---|
| B2B business model | **fit** — chair research fit | funds or does sales-management research; teaching-case potential | pure B2C, no research affinity |
| region reachable (day trip from Gießen) | **region** — Mittelhessen reach | HQ or major site in Hessen / day-trip distance | overseas only |
| ≥ 1 verified source | **size** — employer scale | ≥ 1,000 employees (stable partner) | < 20 |
| | **evidence** — source quality | ≥ 2 independent sources, each verified | only the company's own marketing |
| | **timing** — live signals | public signal now: expansion, new unit, sales hiring | no activity signals |

## Rating formulas — pick one, defend it

| Formula | Rule | Trade-off |
|---|---|---|
| **Weighted sum** *(default)* | `L = Σ wᵢ·sᵢ` with weights fit .35 · region .25 · size .15 · evidence .15 · timing .10 | transparent and easy to defend — but compensatory: a 5 on fit can hide a 0 on evidence |
| Geometric mean | `L = Π sᵢ^wᵢ` | non-compensatory: one zero sinks the lead — harsh, harder to communicate |
| Gated weighted sum *(implemented)* | hard gates first, then weighted sum on survivors | matches how the chair decides · gate thresholds are judgement calls — say yours |

Worked example: fit 5 · region 3 · size 4 · evidence 4 · timing 2 →
`L = .35·5 + .25·3 + .15·4 + .15·4 + .10·2 = 3.90`.
The weights live in `leads.yaml` under `rubric:` — **published context,
not vibes**. Changing them is allowed, but must be argued in the PR.

## Integrity rules

- No invented facts. If you cannot verify it, the claim is not written —
  or the lead is `status: unverified`.
- Every source URL must resolve **and** support the sentence it sits on.
  Remember the standing question: companies' own pages are self-reported —
  *whose evidence is this?*
- Rejected leads are kept and marked, never deleted.
- Your agent may do the reading and the typing. **You** own DEFINE and
  VERIFY — the scores are yours to defend.

## Definition of done

A submission is **done** when: the validator passes, every claim has a
working source URL, the scores follow the published formula, and you can
answer *checked? citable? repeatable?* with yes. Otherwise it is a draft.
