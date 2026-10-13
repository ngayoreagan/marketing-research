# Demo Test & Preparation Protocol

Prep ladder for the walkthrough block (slides 11–14, ~13 min). Run the
levels in order; T2 on 22 Oct is the pre-flight checklist itself.

---

## 1. Test levels

| Level | What | Where | When |
|---|---|---|---|
| **T0 — Contract rehearsal** | Read AGENTS.md aloud, walk the six pipeline boxes, rehearse narration (incl. sector-choice beat) + stumble placement. No tech needed. | anywhere | now |
| **T1 — Home dry run** | Full run in pi with BrowserMCP: same kickoff prompt, 2 companies (mechanical engineering: market leader + Mittelstand specialist). Log per-phase times. | home office | 2–3× this week |
| **T2 — Dress rehearsal** | Exact room conditions: Licher Straße 68, Raum 45, beamer, JLU network, zoom/font sizes. | the lecture room | 22 Oct, 14:15–14:30 |

## 2. Environment checklist

- [ ] pi starts; model = **big pickle**; first response fast
- [ ] **Ctrl+L model switch** practiced (fallback model when big pickle is slow)
- [ ] BrowserMCP server starts and opens **one real company page**; text extraction works
- [ ] Network tested **in the target network** (JLU/eduroam, not home) — no captive portal
- [ ] The 2–3 target company URLs + funding registry resolve (no 404 traps)
- [ ] Beamer resolution known (16:9 vs 4:3); browser zoom 125–150 %; terminal font readable from row 20
- [ ] HDMI adapter + cable packed

## 3. Timing log

| Phase (demo-script rows) | Target | T1 | T2 |
|---|---|---|---|
| 0–2 min — read AGENTS.md aloud | 2 min |  |  |
| 2–3 min — kickoff prompt + plan | 1 min |  |  |
| 3–8 min — browse / extract / score | 5 min |  |  |
| ~6 min — deliberate stumble + student question | ~1 min |  |  |
| 8–11 min — write table, re-check URLs | 3 min |  |  |
| 11–13 min — final table + three questions | 2 min |  |  |
| **Total** | **≤ 13 min** (agent run ≤ 8 min) |  |  |

## 4. Cut points (if behind)

- Minute 11 reached and not at the table → **drop second company**, go straight to writing the table
- Agent run exceeds 8 min → **one company only**, then table
- Tech failure unresolved after 2 min → **tier 2 now** (fallback-demo.mp4), announce honestly: *"untouched recording of the same contract run"*

## 5. Stumble rehearsal

- Position: mid-extraction (~minute 6) — a claim that lacks a URL
- Cue: *"What would you check here?"* → ask **two** students, let them say it
- Correction: let the agent re-check the claim, then continue
- Practice in pi: **interrupt + edit the task input** — your steering hand must be smooth

## 6. Three questions on the real output (slide 14)

1. **Checked?** — every claim carries evidence
2. **Citable?** — URLs resolve **and** support the sentence
3. **Repeatable?** — same contract → same method → auditable, re-runnable result
(process-level, never byte-identical with a stochastic model)

## 7. Deliverables before 22 Oct

- [ ] 3 full runs: 1 discovery + 2 timed (timing log above)
- [ ] `fallback-demo.mp4` recorded (ffmpeg sheet) + `fallback-session.md` transcript saved
- [ ] Q&A bank: 6 likely questions answered in < 60 s each
- [ ] HDMI adapter + cable packed
- [ ] This protocol printed / on phone

## 8. Fallback ladder (one line)

**live → fallback-demo.mp4 → transcript** — the three questions land either way.

---

## Kickoff prompt (copy block)

> Read AGENTS.md in this folder and follow it. Build the shortlist for 2
> companies from the German mechanical and plant engineering sector
> (e.g. a global market leader and a Mittelstand specialist). Show your
> plan first, then work step by step.