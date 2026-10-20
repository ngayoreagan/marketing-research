# Agentic Test Protocol — the walkthrough is only as good as its test runs

No fallback video, no recording. **The approach must prove itself
agentically**: the exact exercise the audience will see is run end-to-end
with the agent, repeatedly, before the lecture. A run counts as passed
only when `python3 leads/validate_leads.py` exits 0 on the produced
`leads/leads.yaml`.

---

## 1. Test levels

| Level | What | Where | When |
|---|---|---|---|
| **T0 — Brief rehearsal** | Read `leads/README.md` + `leads.yaml` aloud, walk the six pipeline boxes, rehearse narration (incl. sector-choice beat) + stumble placement. No tech needed. | anywhere | now |
| **T1 — Agentic test runs** | Full runs in pi with BrowserMCP: exact kickoff prompt from `demo-script.md`, 2 leads (mechanical engineering: market leader + Mittelstand specialist), ends with the validator passing. Log per-phase times + failures + fixes. | home office | 2–3× this week |
| **T2 — Dress rehearsal** | One full agentic run under exact room conditions: Licher Straße 68, Raum 45, beamer, JLU network, zoom/font sizes. | the lecture room | 22 Oct, 14:15–14:30 |

## 2. Environment checklist

- [ ] pi starts; model = **big pickle**; first response fast
- [ ] **Ctrl+L model switch** practiced (faster model when big pickle is slow)
- [ ] BrowserMCP server starts and opens **one real company page**; text extraction works
- [ ] Network tested **in the target network** (JLU/eduroam, not home) — no captive portal
- [ ] `opencode.ai` resolves in the hall network (`nslookup opencode.ai`) — if not → DNS fix box below
- [ ] The 2–3 target company URLs + funding registry resolve (no 404 traps)
- [ ] `leads/leads.yaml` fresh (template state, `leads: []`) after every test run
- [ ] Beamer resolution known (16:9 vs 4:3); browser zoom 125–150 %; terminal font readable from row 20
- [ ] HDMI adapter + cable packed

## 2b. DNS fix (if the hall network can't resolve `opencode.ai`)

1. **Resolver:** Wi-Fi adapter → DNS `1.1.1.1` + `8.8.8.8`; reconnect, retry.
2. **Hosts entry** (admin): `dig +short opencode.ai @1.1.1.1` → append
   `<IP> opencode.ai` to `/etc/hosts` (Linux/macOS) or
   `C:\Windows\System32\drivers\etc\hosts` (Windows).
   Verified 19 Oct 2026: `172.65.90.20` (Cloudflare anycast, `.20`–`.23`) — re-verify.
3. **Still failing** → firewall, not DNS → phone hotspot for the demo machine.

## 3. Timing log (fill per T1/T2 run)

| Phase (demo-script rows) | Target | T1 run 1 | T1 run 2 | T2 |
|---|---|---|---|---|
| 0–2 min — walk the repo | 2 min | — | | |
| 2–3 min — kickoff prompt + plan | 1 min | — | | |
| 3–8 min — browse / extract / score | 5 min | — | | |
| ~6 min — deliberate stumble + student question | ~1 min | — | | |
| 8–11 min — write leads.yaml, run validator | 3 min | — | | |
| 11–13 min — final table + three questions | 2 min | — | | |
| **Validator exit code at end** | **0** | **0** | | |
| **Total** | **≤ 13 min** (agent run ≤ 8 min) | **12:00** | | |

**T1 run 1 — 20 Oct 2026 · opencode v2.0.29 · model `litellm/glm-5-turbo` · headless `opencode run`**

- Result: **passed.** 2 leads ingested (Qlar Group, ex-Schenck Process, Darmstadt · SCHUNK SE & Co. KG, Lauffen), validator exit 0, score math exact (both 4.45), **8/8 source URLs resolve** (curl-checked).
- Over the 8-min agent target — browsing + cross-checks ate the time. Keep the minute-11 cut point; rehearse with the single-lead fallback.
- Stumbles handled autonomously (better than scripted): WebSearch cancelled (no provider configured) → pivoted to direct page fetches; 404 on schenckprocess.com (Qlar rebrand) → found qlar.com; SCHUNK/Schunk-Group **disambiguation trap avoided unprompted**.
- Honest evidence discounting: `evidence: 3` because only one independent source each (Wikipedia citing WirtschaftsWoche) — agent flagged where a second source would lift the score.
- Headless quirk: `opencode run` exited 1 despite a completed task (cancelled web-search calls) — judge by output + validator, not exit code alone.
- Per-phase timings not measurable headless — fill from T2 (human watches the clock).
- Archive: post-run state in `demo_walked/` (leads.yaml with the 2 leads); `leads/` restored to template (`leads: []`).

## 4. Cut points (if behind)

- Minute 11 reached and not at the table → **drop second lead**, finish with one
- Agent run exceeds 8 min → **one lead only**, then the table
- Validator fails at minute 11 → **show the failure and fix the top error live**;
  a visible fix lands better than a hidden failure. Never skip the validator —
  it is the proof that the contract is executable.

## 5. Stumble rehearsal

- Position: mid-extraction (~minute 6) — a claim that lacks a URL
- Cue: *"What would you check here?"* → ask **two** students, let them say it
- Correction: let the agent re-check the claim, then continue
- Practice in pi: **interrupt + edit the task input** — your steering hand must be smooth

## 6. Three questions on the real output (slide 16)

1. **Checked?** — every claim carries evidence
2. **Citable?** — URLs resolve **and** support the sentence
3. **Repeatable?** — same repo, same rubric → auditable, re-runnable result
   (process-level, never byte-identical with a stochastic model)

## 7. Deliverables before 22 Oct

- [ ] ≥ 2 logged agentic T1 runs: timing + failures + fixes, validator exit 0 each
- [ ] T2 dress rehearsal completed in the room, validator exit 0
- [ ] Q&A bank: 6 likely questions answered in < 60 s each
- [ ] HDMI adapter + cable packed
- [ ] This protocol printed / on phone

---

## Kickoff prompt (copy block — identical to demo-script.md)

```text
Work in this repository. Read leads/README.md and leads/leads.yaml.
Task: ingest 2 partner-candidate leads for the chair — German mechanical
and plant engineering, one global market leader, one Mittelstand
specialist. Follow the six-step loop: source real pages, qualify against
the rubric (gates first, then the weighted sum), record every claim with
a source URL. Add both leads to leads/leads.yaml, then run
python3 leads/validate_leads.py and fix what fails. Show your plan
first, then work step by step.
```
