#!/usr/bin/env python3
"""Validate students/leads.yaml — schema, gates, score math, source format.

The student-side twin of scripts/validate_papers.py: the contract is not
a prose file, it is executable. Run before every commit:

    python3 students/validate_leads.py

Exit 0 = pass. Any FAIL prints and exits 1.
"""
import re
import sys
from pathlib import Path

import yaml

REQUIRED = ["company", "sector", "b2b", "region_reachable", "hq", "employees",
            "scores", "fit_signal", "sources", "score", "scored_by", "date",
            "status"]
CRITERIA = ["fit", "region", "size", "evidence", "timing"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def main() -> int:
    path = Path(__file__).resolve().parent / "leads.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    errors: list[str] = []

    rubric = data.get("rubric") or {}
    weights = rubric.get("weights") or {}
    if set(weights) != set(CRITERIA):
        errors.append(f"rubric.weights must define exactly {CRITERIA}, got {sorted(weights)}")
    if abs(sum(weights.values()) - 1.0) > 1e-9:
        errors.append(f"rubric.weights must sum to 1.0, got {sum(weights.values()):.4f}")

    leads = data.get("leads") or []
    if not leads:
        print("OK   schema valid — but `leads:` is empty. Ingest your leads, then re-run.")
        return 0 if not errors else fail(errors)

    seen: set[str] = set()
    for i, lead in enumerate(leads, 1):
        name = lead.get("company") or f"lead #{i}"
        where = f"[{name}]"
        if name in seen:
            errors.append(f"{where} duplicate company name")
        seen.add(name)

        for field in REQUIRED:
            if field not in lead:
                errors.append(f"{where} missing required field '{field}'")
        if errors and any(where in e for e in errors):
            continue  # schema incomplete; deeper checks would crash

        for crit in CRITERIA:
            v = (lead.get("scores") or {}).get(crit)
            if not isinstance(v, int) or not 0 <= v <= 5:
                errors.append(f"{where} score '{crit}' must be an integer 0-5, got {v!r}")

        if not isinstance(lead.get("b2b"), bool) or not isinstance(lead.get("region_reachable"), bool):
            errors.append(f"{where} b2b / region_reachable must be booleans")
        if not isinstance(lead.get("employees"), int) or lead.get("employees", 0) < 1:
            errors.append(f"{where} employees must be a positive integer")

        sources = lead.get("sources") or []
        verified_any = False
        for s in sources:
            url = str(s.get("url", ""))
            if not url.startswith("https://"):
                errors.append(f"{where} source URL must be https:// — {url!r}")
            if not str(s.get("claim", "")).strip():
                errors.append(f"{where} every source needs the claim it supports")
            if s.get("verified") is True:
                verified_any = True
        if not sources:
            errors.append(f"{where} at least one source is required")

        if not DATE_RE.match(str(lead.get("date", ""))):
            errors.append(f"{where} date must be YYYY-MM-DD")

        status = lead.get("status")
        if status not in ("verified", "unverified", "rejected"):
            errors.append(f"{where} status must be verified|unverified|rejected, got {status!r}")

        # gates decide status — a gated-out lead must be 'rejected', not dropped
        gated_out = (lead.get("b2b") is not True or lead.get("region_reachable") is not True
                     or not verified_any)
        if gated_out and status != "rejected":
            errors.append(f"{where} fails a gate -> status must be 'rejected' (never drop, never score)")
            continue
        if status == "rejected":
            continue  # no score math for rejected leads

        expected = sum(weights[c] * lead["scores"][c] for c in CRITERIA)
        got = lead.get("score")
        if not isinstance(got, (int, float)) or abs(got - expected) > 0.011:
            errors.append(
                f"{where} score {got} != weighted sum {expected:.2f} "
                f"(the formula is published — no fudging)")

    if errors:
        return fail(errors)
    print(f"OK   {len(leads)} lead(s) valid — schema, gates, score math, sources all pass.")
    return 0


def fail(errors: list[str]) -> int:
    for e in errors:
        print(f"FAIL {e}")
    print(f"\n{len(errors)} error(s) — fix leads.yaml, then re-run.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
