# Playbook: Branchenauswahl für die Demo-Shortlist

Wahl der Demo-Branche (und der 2 Demo-Unternehmen) für die Lead-Gen-Shortlist.
Ziel: eine Branche, die zum Haas-Lehrstuhl passt (Forschung + Lehre + Region),
sich als B2B-Vertriebsfall eignet und für die Live-Demo belastbare Daten liefert.
Dieses Playbook ist der wiederverwendbare Ablauf; jeder Durchlauf schärft ihn
(siehe [6. Iteratives Schärfen](#6-iteratives-schärfen)).

---

## 1. Prozess-Überblick (das wurde durchgeführt)

Der Ablauf aus V1 (13.10.2026), ausgelöst durch die Frage *„wieso Handel?"*:

| Phase | Was | Ergebnis V1 |
|---|---|---|
| **P0 · Trigger/Default hinterfragen** | Die bisherige Branche (deutscher Lebensmittelhandel) auf offensichtliche Schwächen prüfen: Passt sie zum Lehrstuhl? | Handel = B2C/Demand-Gen, kein Vertriebsstrategie-Fall → Zweifel |
| **P1 · Evidenz sammeln** | Quellen lt. Katalog (Abschnitt 3) abfragen: Lehrstuhl, Lehre, Region, Unternehmen, Register | Forschungsthemen der Professur + Branchenstruktur Mittelhessens erhoben |
| **P2 · Metriken definieren** | Metriken M1–M5 (Abschnitt 4) mit je einer konkreten Datenprobe festlegen | Kriterienraster steht |
| **P3 · Scoring & Ranking** | Je Branche 1–5 pro Metrik, Summe, Rangfolge (Abschnitt 5) | M+E 24, Optik/Photonik 23, … Handel 14 |
| **P4 · Entscheidung & Umsetzung** | Sektor-Wahl durch User; Kickoff-Prompts in `demo-script.md` + `test-protocol.md` anpassen; Deck um Sektor-Slide ergänzt | **Maschinen-/Anlagenbau gewählt** (User, 13.10.2026); Prompts + Deck-Slide umgesetzt |

---

## 2. Wiederholbar machen — Ablauf beim nächsten Mal

1. **Frage stellen**: Welche Branche? (Default nicht blind übernehmen — P0.)
2. **P1 ausführen**: Quellenkatalog (Abschnitt 3) abfragen — dieselben Suchen, dieselben Seiten.
3. **P2 bestätigen**: Metriken M1–M5 und Datenproben prüfen; bei Bedarf anpassen (→ Abschnitt 6, dann Run-Log-Eintrag).
4. **P3 ausführen**: Score-Sheet (Abschnitt 5) füllen, Guards anwenden, Ranking erstellen.
5. **P4 umsetzen**: Entscheidung einholen, dann **genau diese Dateien** ändern:
   - `demo-script.md` → Kickoff-Prompt („…from the German grocery retail sector…" ersetzen)
   - `test-protocol.md` → Copy-Block (Abschnitt „Kickoff prompt") + T1-Zeile („2 companies (discounter + wholesaler)")
   - `fallback-session.md` / `fallback-demo.mp4` → beim nächsten T1-Lauf mit neuem Sektor neu aufzeichnen
   - **Deck**: Sektor-Slide „Define the hunt“ (Slide 10) bei Branchenwechsel mit anpassen; restliche Slides bleiben branchenneutral.
6. **Run-Log-Eintrag** anlegen (Abschnitt 6.1) — Datum, Sektor, Ergebnis, Annahmen, Kalibrierung.

---

## 3. Quellenkatalog (fixe Probes)

| Quelle | Was suchen | V1-Probe |
|---|---|---|
| **Lehrstuhl-Seite (Uni Gießen), z.B. „Abschlussarbeiten“** | Forschungsschwerpunkte, Themenfelder | Produktmanagement, Kundenorientierung, Strategieimplementierung, Vertriebsmanagement |
| **Lehrveranstaltungen der Professur** | Kursinhalte, Zielgruppe, Schwerpunkte | „Marketing und Vertrieb in einer digitalen Welt“, „Verhandeln und Verkaufen“, Target-Kurs „Sales Strategy and Execution“ |
| **Regionalmanagement Mittelhessen / Cluster-Seiten** (Wetzlar, Marburg, Gießen) | Branchenstruktur, Leitbranchen, Arbeitgeber | M+E = Rückgrat, Optik/Photonik Wetzlar (Leica, Satisloh, Hensoldt, Bosch Thermotechnik), Life Science Marburg (BioNTech, CSL Behring, OPTIMA), Logistik (HOLM), Automotive |
| **Unternehmens-Newsrooms / Verzeichnisse** | Pressedichte, Datenschicht pro Unternehmen | Weber Food Technology, Rittal, Harmonic Drive, Leica Camera, Satisloh, … |
| **Förderregister (z.B. ZIM) / Uni-Pressemitteilungen** | Uni-Links, Förderprojekte (Kriterium 3 des AGENTS.md-Contracts) | ZIM-Projekte Mittelständler |

---

## 4. Metriken M1–M5 (Definition + Datenprobe)

| Metrik | Frage | Datenprobe (woran messen) | Gewicht |
|---|---|---|---|
| **M1 · Lehrstuhl-Forschungsfit** | Ist Vertrieb eine Kernfunktion der Branche? | Fakultäts-Forschungsthemen (Vertriebsmanagement, KAM, Vertriebssteuerung) | 1 |
| **M2 · Lehrinhalt-Fit** | Passt die Branche zur Zielveranstaltung „Sales Strategy and Execution“? | B2B-Projektgeschäft, lange Zyklen, Facheinkäufer | 1 |
| **M3 · Regionale Arbeitgeberrelevanz** | Wo landen JLU-Absolventen? | Leitbranchen Mittelhessen, Beschäftigtenzahlen | 1 |
| **M4 · Lead-Gen-Relevanz** | Ist Lead Generation ein echtes Vertriebs-Tool (nicht B2C-Demand-Gen)? | Ticketgröße, Zykluslänge, Einkäuferstruktur | 1 |
| **M5 · Demo-Datenverfügbarkeit** | Liefert die Branche belastbare öffentliche Evidenz für die Live-Demo? | Newsrooms, Presse, Register; 2 Ziel-URLs pro Unternehmen müssen resolver | 1 |

Gewichte starten bei 1; Anpassung nur über den Kalibrierungs-Loop (Abschnitt 6).

---

## 5. Score-Sheet & Entscheidungsregeln

**Score-Sheet** (1–5 je Metrik, Summe ungewichtet):

| Branche | M1 | M2 | M3 | M4 | M5 | Σ |
|---|---|---|---|---|---|---|
| Maschinen-/Anlagenbau (M+E) | 5 | 5 | 5 | 5 | 4 | 24 |
| Optik/Photonik/Feinmechanik | 5 | 5 | 5 | 4 | 4 | 23 |
| Pharma/LifeScience/MedTech | 5 | 4 | 4 | 4 | 3 | 20 |
| Automotive/Zulieferer | 4 | 4 | 4 | 4 | 3 | 19 |
| Industrie-Software/Dienstleistungen | 4 | 3 | 2 | 5 | 5 | 19 |
| Logistik | 3 | 3 | 5 | 3 | 3 | 17 |
| Handel (Vorgänger) | 2 | 2 | 3 | 2 | 5 | 14 |

**Guards (harte Regeln):**
- **Disqualifikation**: M1 < 4 **oder** M4 < 4 → Branche fliegt raus (Handel: M1=2, M4=2 — das war der entscheidende Gegenbefund).
- **Tiebreaker**: bei Summengleichstand entscheidet M5 (Demo-Robustheit).
- **Demo-Paar-Regel**: 1 „Anker“ (hohe Pressedichte, M5-stark, idealerweise Weltmarktführer) + 1 Mittelständler (Uni-Links über Förderregister belegbar). Region bevorzugen (M3).
- **Daten-Gate vor dem Wechsel**: 2 Ziel-URLs pro Unternehmen auflösen (kein 404) — Deckung mit T1/U2-Checkliste in `test-protocol.md`.

---

## 6. Iteratives Schärfen

### 6.1 Run-Log (Historie, Appends)

| Version | Datum | Trigger | Ergebnis | Annahmen | Kalibrierungsnotizen |
|---|---|---|---|---|---|
| v1 | 2026-10-13 | „wieso Handel?“ | Empfehlung M+E (24) / Optik (23); Handel disqualifiziert (M1, M4); **Entscheidung offen** | Gewichte = 1; Summe ungewichtet | — |
| v2 | 2026-10-13 | User-Entscheid auf v1-Empfehlung | **Maschinen-/Anlagenbau gewählt**; Guards erfüllt (M1=5, M4=5); Kickoff-Prompts umgestellt (demo-script, test-protocol, shortlist-template); Deck-Slide „Define the hunt“ eingebaut | Fokus B2B-Projektgeschäft; M3-Regionalität bleibt soft | T1-Demo-Paar-Vorschlag: Weber Food Technology (Anker) + Harmonic Drive SE (Mittelständler) — URL-Gate vor T1 prüfen |

Jeder Lauf trägt eine Zeile ein. „Schärfen“ heißt: Die v2-Regeln weichen nur mit
begründetem Log-Eintrag von v1 ab.

### 6.2 Feedback-Quellen (wann schärfen?)

| Signal | Woher | Konsequenz |
|---|---|---|
| T1-Dry-Runs: URLs/404-Traps, schwache Evidenz für Kriterium 2/3 | `test-protocol.md` Timing-Log + Env-Checkliste | M5-Gewicht prüfen oder Unternehmen tauschen (Anker-Regel) |
| Demo-Lauf: Resonanz, Timing dran? | 22-Oct-Durchlauf | Narration/Paar-Wahl kalibrieren |
| Dozenten-Feedback (Haas) nach Gastvortrag | Gespräch | M1/M2-Gewichte anheben/senken |
| Kurs-Evaluation „Sales Strategy and Execution“ (SS 27) | Vorlesungs-Ende | M2/M3 nachjustieren |
| Neue Quellen (Cluster-Berichte, Förderregister-Ausbau) | Recherche | Quellenkatalog (Abschnitt 3) erweitern |

### 6.3 Anpassungsregeln

- **Eine Metrik dominiert permanent** (z.B. jeder Lauf endet beim selben Sektor): Gewicht der
  übrigen Metriken prüfen — nicht wegargumentieren, Log fragen.
- **Empfehlung wird vom User abgelehnt**: Ablehnungsgrund als eigene Spalte im Run-Log
  festhalten und die entscheidende Metrik schärfen (Definition/Probe), nicht nur das Gewicht.
- **Datenlage ändert sich** (Unternehmen zugekauft, Newsroom abgeschaltet): Sektor behalten,
  Demo-Paar neu würfeln — kein kompletter Neulauf nötig.

---

## 7. Verknüpfte Dateien

| Datei | Rolle | Bei Branchenwechsel |
|---|---|---|
| `branchenauswahl-playbook.md` | dieser Ablauf | — |
| `demo-script.md` | Kickoff-Prompt + Narration | Prompt-Zeilen 18–22 anpassen |
| `test-protocol.md` | Teststufen + Copy-Block | Copy-Block + T1-Zeile anpassen |
| `shortlist-template.md` | Zielformat der Shortlist | Header-Sektor anpassen |
| `fallback-session.md` / `fallback-demo.mp4` | Fallback-Tier (noch zu erstellen) | beim nächsten T1-Lauf neu aufzeichnen |
| `agentic-ai-for-lead-generation.md` | Deck (20 Slides; Sektor-Slide „Define the hunt“ = Slide 10) | Sektor-Slide bei Branchenwechsel anpassen; Rest branchenneutral |