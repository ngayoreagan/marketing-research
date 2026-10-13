# Lead-Gen-Programm — Design-Spec

**Datum:** 2026-10-13
**Status:** Design (vor Umsetzung)
**Bezug:** Gastvorlesung „Advanced Issues in Marketing and Sales" (Prof. Dr. Alexander Haas,
Professur Marketing & Verkaufsmanagement, JLU Gießen) — 22.10.2026, 15:15–16:00
**Quelldateien:** `lecture/demo/AGENTS.md` (Contract), `lecture/demo/demo-script.md`,
`lecture/demo/branchenauswahl-playbook.md`, `lecture/agentic-ai-for-lead-generation.md` (Deck),
`paper/g6_haas_integration.md`, `paper/cam_sim.py`, `AGENTS.md` (Repo-Regeln)

---

## 1. Kontext & Ziel

Die Gastvorlesung ist eine **Einzelveranstaltung** (Lecture + Live-Demo „agentic Lead-Gen",
Sektor Maschinen-/Anlagenbau). Aus ihr wachsen zwei Horizonte:

- **Horizont 2026 (sofort):** Anschlussaufgabe für die **Master-Studierenden** — sie suchen
  **Leads für den Chair**.
- **Horizont 2027 (Paper-Programm):** ein **Working Paper**, das die Bachelor-/Master-Arbeiten
  thematisch bündelt.

**Paper-Territorium:** *Agentic operationalization of value opportunity recognition in B2B
lead generation.* Der Gap (Deck Slide 7: agentic AI ∩ lead generation = 0) ist die Motivation,
Layer-0 „Value Context" (`paper/g6_haas_integration.md`) der theoretische Rahmen. Ziel ist ein
**Working Paper zuerst** (kein Journal- oder Timeline-Druck).

---

## 2. Horizont 2026 — Anschlussaufgabe „Leads für den Chair"

**Zielgröße (Definition):** *Praxis-/Interview-Partner* = M+E-Unternehmen mit

1. einem **benannten Ansprechpartner**,
2. einer **verifizierten URL**,
3. erkennbarem **Bezug zur Chair-Forschung** (Vertriebsmanagement / Value-based Selling /
   B2B-Lead-Gen).

| Aspekt | Festlegung |
|---|---|
| Zielgruppe | Master-Studierende des Kurses; **Einzelarbeit** |
| Umfang | **8–12** URL-verifizierte Leads pro Studierendem |
| Format (Pflicht) | Contract-Tabelle `\| Rank \| Company \| Fit signal \| Score \| Source URL(s) \|` **+** Kontaktzeile (Name / Rolle / LinkedIn) **+** 1 Satz Interview-/Value-Hypothese |
| Kriterien | identisch zur Demo: Industry fit / Innovation agenda / University links (je 1–5) |
| Tool | frei — agentische Pipeline (pi / HRZ-LLM) **oder** manuell; Contract-Format + URL-Verifikation sind Pflicht |
| Bewertung | Contract-Rubrik (transparent) + Verifikations-Gate |
| Verifikationsregel | jede Zelle auf eine URL zurückführbar; Unverifiziertes darf bleiben, muss aber markiert werden („no invented facts") |
| Abgabe | zentrales **Lead-Register** (CSV/YAML), dedupliziert von der Betreuung |

**Ansätze**
- **A — Shortlist-Format (empfohlen):** Contract-Tabelle + Kontaktzeile. Schlank, direkt
  anschlussfähig an die Demo.
- **B — Lead-Dossier (optional):** zusätzlich Kontext, Value-Hypothese, 3 Interview-Fragen;
  zugleich Vorarbeit für H4.
- **C — Kohorten-Split (verworfen):** Klasse teilt die M+E-Landkarte nach Teilsektor; senkt
  Redundanz, erschwert aber die Einzelbewertung.

---

## 3. Kopplung 2026 → 2027

Das **Lead-Register 2026 ist das Firmenpanel** des Paper-Programms 2027:

- **H1** (Vignetten-Reliabilität) nutzt die Firmen als Vignetten.
- **H3** (Signal→Fenster) verknüpft öffentliche Signale mit den Firmen.
- **H4** (Wertdimensionen) rekrutiert die Forced-Choice-Teilnehmer aus dem Kontaktfeld.

Didaktischer Mehrwert: Die Studierenden machen 2026 selbst Lead-Gen — und ihr verifizierter
Output wird 2027 zum Datensatz.

---

## 4. Horizont 2027 — das Paper-Programm

### 4.1 Theoretischer Rahmen

- **Layer-Struktur:** L0 Value Context (filtert Relevanz von allem darunter) → L1 Firmographic
  → L2 Buying-Situation → L3 Journey-Stage → L4 Real-Time Signals → value-aligned
  **action selection**. CAM-Sim-Finding F3: Kontext zahlt sich in der Action-Selection aus,
  nicht in der Bid-/Preis-Modulation.
- **Value-Dimensionen:** Economic / Strategic / Operational / Relationship.
- **Anker (verifiziert, siehe `paper/g6_haas_integration.md`):** Terho, Haas, Eggert & Ulaga
  (2012, IMM 41(1)) „value-based selling"; Böhm, Eggert, Terho, Ulaga & Haas (2020, JPSSM
  40(3)) „value opportunity recognition".
- **Abgrenzung:** Jede Arbeit liegt auf der **Automatisierungs-/Agentik-Achse** — sie
  operationalisiert Layer 0 maschinell, statt Haas' Theorie neu zu beweisen.

### 4.2 RQ-Portfolio mit Bachelor/Master-Split

| RQ | Track | Frage (Kurzform) | Konstrukt / Einheit | Daten & Benchmark | Bezug |
|---|---|---|---|---|---|
| **H7** | Bachelor | Schließt sich das agentic×lead-gen-Gap 2026→SS27? | Gap-Rate / Korpus-Keywords | bestehender Korpus; Keyword-Sensitivität | Methodik-Zubringer |
| **H8** | Bachelor | Wie ehrlich sind Agent-Shortlists — und senkt die Source-URL-Pflicht die Fehlerrate? | Claim-Verifikationsrate / Claim | mehrere Demo-Runs (mit/ohne URL-Pflicht) | Güte/Methodik |
| **H1** | Bachelor | Erkennen unabhängige Experten Opportunity-Fenster reliabel (κ ≥ 0.6)? | Opportunity-Fenster (binär) / Vignette | Haas-Panel (3–5 Rater), 30 Vignetten | Fundament (Voraussetzung für RQ5/6/7) |
| **H4** | Bachelor | Gewichten M+E-Experten operative/relationale Werte höher als ökonomische? | Wertdimensions-Präferenzrang | Forced-Choice-Umfrage | RQ6 |
| **H2** | **Master** | Korreliert der contract-basierte Agent-Score **stärker** mit den Experten-Labels als eine firmografische Profilheuristik? | Opportunity-/Relevanz-Score / Firma | LLM-Agent (pi/HRZ) vs. Profilheuristik, Ziel = H1-Labels; OOS Spearman ρ | **RQ7 (Kern)** |
| **H3** | Master | Welche öffentlichen Signale (L2/L4) sind mit Experten-Fenstern assoziiert? | Signal→Fenster / Signalfall | logistisches Modell, AUC; Web + H1-Labels | RQ6 |
| **H5** | Master | Verschiebt Value-Context- vs. firmografisches Framing die Signalpriorisierung? | Framing-Interaktion | Within-Subject-Vignette, Effektstärke d; Ethik/DSGVO | RQ5 |
| **H6** | Master | Erzeugt eine value-context-konditionierte Policy höheren realisierten Wert als die bid-modulierte Baseline? | realisierter Wert | `paper/cam_sim.py` (M+E-Parametrisierung), F3-Replikation | RQ5/7 |

### 4.2.1 Forschungslogik-Kette

`H7 → H8 → H1 → H2 → H3/H4 → H5 → H6`

- **Bachelor legt das Fundament:** Kriterium (H1), Instrument (H4), Feld-Tracking (H7),
  Güteprüfung (H8).
- **Master fährt die Kern-Empirie:** H2 (Herzstück), H3, H5, H6.
- **Synthese RQ5/6** wird zum Backbone des einen Papers (Autorenschaft: Kern-Team).

Jede RQ = eine Study; der Grad bestimmt **Tiefe/Scope**, nicht den Zuschnitt der Frage.

---

## 5. Nicht verhandelbar

- **Co-Autorschaft ist Outcome**, kein Automatismus.
- **Contract-first** pro RQ (Aufgabe, Kriterien, Abgabe vorab fixiert).
- **No invented facts** — Unverifiziertes zulässig, aber markiert.
- Haas' AI-Fokus nicht überzeichnen; keine erfundenen Titel zitieren.

---

## 6. Abhängigkeiten, Risiken, offene Fragen

**Abhängigkeiten**
- H1 setzt ein Experten-Panel (Haas-Netzwerk) voraus; H2/H3 hängen an H1.
- H4 liefert das Messinstrument für H5.
- H6 setzt Python-Betreuung / CS-Ko-Betreuung voraus.
- Alle empirischen RQs hängen am Lead-Register 2026 (Panel).

**Risiken**
- **Betreuung:** Wer führt Master-Studierende durch LLM-/Sim-RQs?
- **Ethik/DSGVO:** H5 (Vignette) und Interviews brauchen vorab geklärte Ethik.
- **Agent-Nichtdeterminismus:** Reproduzierbarkeit braucht fixierte Seeds/Temperature und Run-Logs.
- **Datenzugang:** Panel-Größe könnte für H3 (AUC) knapp sein.

**Offene Fragen**
1. Welche Methodenmodule haben die BWL-Bachelor absolviert (Statistik / empirische Methoden /
   Python)? Bestimmt die H1/H4-Zuordnung.
- wie viele Betreuungsressourcen (HiWi / Master-Studierende / Zeit) für technische RQs?
- Zielgröße des Lead-Registers (Panel-N) und ob die Lead-Aufgabe benotet oder als Bonus gewertet
  wird.
- Panel-/Assessment-Gewicht: benotet oder Bonus?

---

## 7. Erfolgskriterien

**2026**
- Contract-konforme Abgabe je Studierendem.
- ≥ *N* deduplizierte, URL-verifizierte Leads im Register (Panel-Größe für 2027 gesichert).

**2027**
- H1: Inter-Rater-κ ≥ 0.6 (Konstrukt existiert und ist messbar).
- H2: Kern-Test agentisch vs. profilbasiert ist entscheidbar (Vorzeichen/Signifikanz).
- Ein eingereichtes Working Paper (Gap + L0-Operationalisierung).

---

## 8. Out of Scope

- Kein Journal-Submissionszwang und keine fixe Timeline für 2027.
- Keine Änderungen an `papers.yaml` oder Pipeline-Outputs (`docs/*`, `statistics.json`,
  Root-`README.md`) — Repo-Regeln aus `AGENTS.md` bleiben gültig.
- Keine neue Taxonomie-/Korpus-Zelle (falls nötig: Rückfrage statt Erfindung).
