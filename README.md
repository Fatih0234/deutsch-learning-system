# Deutsch Learning System

Ein kleines, versioniertes Lernsystem für Deutsch mit Fokus auf aktive Nutzung,
wiederkehrendes Feedback und langfristige Verbesserung.

## Ziel

Deutsch soll nicht nur als separates Lernfach existieren, sondern in den Alltag
integriert werden – besonders in Softwareentwicklung, Arbeit mit Coding-Agenten,
Lesen, Hören, Schreiben und Sprechen.

Das System folgt dieser Feedbackschleife:

```text
Input / Output
    ↓
Verständnis prüfen
    ↓
wichtiges Feedback extrahieren
    ↓
State aktualisieren
    ↓
Ziele für Wiederholung auswählen
    ↓
erneut aktiv benutzen
```

## Architektur

```text
deutsch-learning-system/
├── README.md
├── AGENTS.md
├── config/
│   └── learner.yaml
├── state/
│   ├── current.yaml
│   ├── errors.yaml
│   ├── vocabulary.yaml
│   ├── structures.yaml
│   ├── skills.yaml
│   └── review_queue.yaml
├── sessions/
│   └── YYYY/MM/
├── sources/
│   ├── reading/
│   └── listening/
├── templates/
│   ├── speaking.md
│   ├── writing.md
│   ├── reading.md
│   └── listening.md
├── schemas/
│   ├── errors.schema.json
│   ├── vocabulary.schema.json
│   └── structures.schema.json
└── scripts/
    └── validate_state.py
```

## Prinzipien

- Nicht jeden Fehler korrigieren.
- Wiederkehrende Fehler sind wichtiger als einmalige Fehler.
- Offensichtliche Speech-to-Text-Fehler nicht als Sprachfehler speichern.
- Lesen und Hören liefern neues Material.
- Sprechen und Schreiben aktivieren dieses Material.
- Neue Vokabeln werden nur gespeichert, wenn sie nützlich genug sind.
- Ein Lernziel wird nicht nach einer einzigen korrekten Verwendung als gemeistert markiert.
- `sessions/` ist das historische Event Log.
- `state/` ist der aktuelle, verdichtete Lernzustand.

## Empfohlener Ablauf pro Session

1. `state/current.yaml` lesen.
2. Lernaktivität durchführen.
3. Inhaltlich auf den Lernenden reagieren.
4. 3–5 wichtige Korrekturen auswählen.
5. Wiederkehrende Muster identifizieren.
6. Session-Log schreiben.
7. State-Dateien aktualisieren.
8. Ziele für die nächste Session auswählen.

## Statusmodell

### Fehler

```text
candidate → active → improving → mastered
```

### Wortschatz

```text
new → learning → active → stable → mastered
```

### Strukturen

```text
introduced → practicing → improving → stable → mastered
```

## Git-Konvention

Empfohlene Commit-Messages:

```text
learn: speaking session about coding agents
learn: reading session on AI agents
state: promote je-desto word order to active
review: reinforce sich anfühlen
```

## Startpunkt

Die initialen State-Dateien enthalten bereits Muster aus den ersten
Deutsch-Sessions:

- `sich anfühlen`
- Wortstellung bei `je ... desto ...`
- `ein gutes Ding` → `eine gute Sache`
- `Zeit mit Lernen verbringen`
- `einen Ort schaffen/einrichten`
- `Erfolgserlebnis`
- `sich mit etwas herumschlagen`
