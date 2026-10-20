# Demo script — Walkthrough (Block 3, ~13 min)

Live demo in the pi harness, **inside the chair's repository**
(`marketing-research/`). No AGENTS.md contract, no fallback video, no
recording: reliability comes from **testing the approach agentically** —
the exact exercise is run end-to-end with the agent before the lecture
(see [`test-protocol.md`](test-protocol.md)).

## Pre-flight (before the lecture, ~5 min)

- [ ] Room: **Licher Straße 68, Raum 45** (FB02) — arrive 14:15–14:30 and set up during Prof. Haas's part
- [ ] Beamer/port: test HDMI adapter + cable in the room before the break
- [ ] Network works **in the lecture hall** — test hall Wi-Fi, not office Wi-Fi, incl. `opencode.ai` DNS (fix: `test-protocol.md` §2b)
- [ ] `pi` starts, model selected (fast model is fine — speed beats depth)
- [ ] Browser tool (BrowserMCP/MCP) connects — open one company page once
- [ ] **Repo root open in the editor:** `leads/leads.yaml` + `leads/validate_leads.py` in view
- [ ] **Agentic test runs done:** ≥ 2 timed T1 runs of the exact exercise, validator passing (log in `test-protocol.md`)

## Kickoff prompt (paste after walking through the repo, slide 13)

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

Small scope on purpose: 2 leads, one industry — the demo must finish.

## Narration beats

| Minute | What happens | What you say |
|---|---|---|
| 0–2 | Show the repo (slide 14): `papers.yaml`, validators, `leads/` | "This is the contract — not a document the agent may ignore, but the repo itself: schema, rubric, executable validator. Done means: the validator passes. And look at the sources — company sites, press, registries. **Whose evidence?**" |
| 2–3 | Paste kickoff prompt, agent plans | "Watch the plan — it maps one-to-one onto the six boxes from the pipeline slide." |
| 3–8 | Agent browses, extracts, scores | Narrate each tick: source → fit signal → score → URL. Point at the pipeline boxes. |
| ~3.5 | **BrowserMCP intermezzo** | The agent opens a real browser. "Why a real browser and not an API? LinkedIn, consent walls, logged-in portals block plain HTTP — a search API gets a 403. So it drives a real browser — login, accept consent, read the page. A browser as one more tool." Point at the protected page it just logged into. |
| ~6 | **Deliberate stumble** | If the agent over-claims, stop it: "Which URL says that?" — let it correct itself. **This is the loop.** |
| 8–11 | Agent writes `leads/leads.yaml`, runs the validator | "It verifies its own citations and the score math — the validator checks both. That is step five: verify." At the stumble, ask two students: "What would you check here?" |
| 11–13 | Final table → slide 16 (three questions) | "Now we judge it: checked? citable? repeatable?" |

## Timing guard — debug live, no safety net

- Hard stop at minute 11 for the final table — if the demo runs long, cut the
  second lead and finish with one.
- **If something breaks: debug it live and say so.** A workflow failing and
  getting fixed in front of the room *is* the lesson — that is the loop working.
  The approach is trustworthy because it was tested agentically beforehand,
  not because a video stands by.
- Hard stop at 16:00 absolute: the course's Übung follows in the same room.
- Bank questions: "Hold that for Q&A — we have 10 minutes at the end."
