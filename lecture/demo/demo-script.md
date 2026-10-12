# Demo script — Walkthrough (Block 3, ~13 min)

Live demo in the pi harness. The contract is [`AGENTS.md`](AGENTS.md) in this
folder; the target result looks like [`shortlist-template.md`](shortlist-template.md).

## Pre-flight (before the lecture, ~5 min)

- [ ] Room: **Licher Straße 68, Raum 45** (FB02) — arrive 14:15–14:30 and set up during Prof. Haas's part
- [ ] Beamer/port: test HDMI adapter + cable in the room before the break
- [ ] Network works **in the lecture hall** — test hall Wi-Fi, not office Wi-Fi
- [ ] `pi` starts, model selected (fast model is fine — speed beats depth)
- [ ] Browser tool (BrowserMCP/MCP) connects — open one company page once
- [ ] This folder open in the editor: `lecture/demo/`
- [ ] **Fallback artefacts ready:** `fallback-session.md` (transcript) + `fallback-demo.mp4` (recording), both in this folder

## Kickoff prompt (paste after showing AGENTS.md)

```text
Read AGENTS.md in this folder and follow it. Build the shortlist for
2 companies from the German grocery retail sector (e.g. a discounter
and a wholesaler). Show your plan first, then work step by step.
```

Small scope on purpose: 2 companies, one industry — the demo must finish.

## Narration beats

| Minute | What happens | What you say |
|---|---|---|
| 0–2 | Show `AGENTS.md` (slide 11) | "This is the contract — the agent reads this at every start. Done means: verified, cited, repeatable. And look at the sources — company sites, press, registries. Those are the companies' own reports. **Whose evidence?**" |
| 2–3 | Paste kickoff prompt, agent plans | "Watch the plan — it maps to the six boxes from the pipeline slide." |
| 3–8 | Agent browses, extracts, scores | Narrate each tick: source → fit signal → score → URL. Point at the pipeline boxes. |
| ~6 | **Deliberate stumble** | If the agent invents or over-claims, stop it: "Which URL says that?" — let it correct itself. **This is the loop.** |
| 8–11 | Agent writes the table, re-checks URLs | "It verifies its own citations — that is step 5. Each URL must resolve **and** support the sentence." At the stumble, ask two students: "What would you check here?" before the agent corrects itself. |
| 11–13 | Final table → slide 13 (three questions) | "Now we judge it: checked? citable? repeatable?" |

## Timing guard

- Hard stop at minute 11 for the final table — if the demo runs long, cut the
  second company and show the table with one.
- Hard stop at 16:00 absolute: the course's Übung follows in the same room.
- Bank questions: "Hold that for Q&A — we have 10 minutes at the end."

## Fallback — three tiers (if the live demo fails)

1. **Play the recording.** Run `fallback-demo.mp4` (same contract, same run,
   recorded at home, ~8–10 min) and narrate over it: "I'm showing the
   untouched recording of the same contract run." Pause at the stumble and
   ask the students the same question — the loop still lands.
2. **Walk the transcript.** No video either → show `AGENTS.md`, open
   `fallback-session.md` and the final shortlist table, walk the audience
   through what the agent did at each pipeline box.
3. **Apply the three questions either way.** Judge the saved result
   (checked? citable? repeatable?) — the method lands regardless.
