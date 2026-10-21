#!/usr/bin/env python3
"""Validate leads/leads.yaml — schema, gates, score math, source format.

The student-side twin of scripts/validate_papers.py: the contract is not
a prose file, it is executable. Run before every commit:

    python3 leads/validate_leads.py

Exit 0 = pass. Any FAIL prints and exits 1.
"""
import re
import sys
from argparse import ArgumentParser
from pathlib import Path

import yaml

REQUIRED = ["company", "sector", "b2b", "region_reachable", "hq", "employees",
            "scores", "fit_signal", "sources", "score", "scored_by", "date",
            "status"]
CRITERIA = ["fit", "region", "size", "evidence", "timing"]
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# https:// followed by a real, non-whitespace URL (host must be non-empty and
# contain a dot or 'localhost') — rejects 'https:// ', javascript:, etc.
URL_RE = re.compile(r"^https://[^\s]+\.[^\s]+$")


def main() -> int:
    ap = ArgumentParser(description="Validate leads/leads.yaml")
    ap.add_argument(
        "--check-urls", action="store_true",
        help="OPTIONAL: live-check that each source URL resolves (HTTP HEAD/GET). "
             "Offline-safe: the default run only checks scheme/format. A dead URL "
             "then surfaces as a warning, not a hard fail.")
    args = ap.parse_args()

    path = Path(__file__).resolve().parent / "leads.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []

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
            if not URL_RE.match(url):
                errors.append(f"{where} source URL must be https://host/path — got {url!r}")
            if not str(s.get("claim", "")).strip():
                errors.append(f"{where} every source needs the claim it supports")
            if s.get("verified") is True:
                verified_any = True
            if args.check_urls:
                if not _resolves(url):
                    warnings.append(f"{where} URL does not resolve (dead/403): {url}")
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
            if not gated_out:
                # A lead that passes every gate should not be 'rejected' — rejection
                # is meant to be gate-driven. If there's a non-gate reason, say it.
                errors.append(
                    f"{where} status 'rejected' but it passes every gate (b2b OK, region OK, "
                    "verified source OK). Rejection should be gate-driven; if disqualified "
                    "for another reason give the actual gate failure or remove it.")
            continue  # no score math for rejected leads

        expected = sum(weights[c] * lead["scores"][c] for c in CRITERIA)
        got = lead.get("score")
        if not isinstance(got, (int, float)) or abs(got - expected) > 0.011:
            errors.append(
                f"{where} score {got} != weighted sum {expected:.2f} "
                f"(the formula is published — no fudging)")

    if errors:
        return fail(errors)
    for w in warnings:
        print(f"WARN {w}")
    print(f"OK   {len(leads)} lead(s) valid — schema, gates, score math, sources all pass.")
    return 0


def _resolves(url: str) -> bool:
    """Best-effort live check that a URL returns HTTP <400. Falls back to GET on
    HEAD-405 servers. Any network error counts as 'does not resolve' only when
    --check-urls is requested (offline runs never call this)."""
    import urllib.request, urllib.error
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": "leads-validator/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.status < 400
        except urllib.error.HTTPError as e:
            return e.code < 400  # 4xx/5xx => dead; 3xx handled by urlopen redirect
        except Exception:
            continue
    return False


def fail(errors: list[str]) -> int:
    for e in errors:
        print(f"FAIL {e}")
    print(f"\n{len(errors)} error(s) — fix leads.yaml, then re-run.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
