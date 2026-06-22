# Stuff4Staff GmbH — Website

Moderne, statische Website für **Stuff4Staff Handels GmbH**, die Übungsfirma der HAK Kirchdorf an der Krems — Großhandel für gesundheitsfördernde Büromöbel, Kaffeevollautomaten, erlesenen Kaffee und Genussartikel.

Neutrales, professionelles Design in Anlehnung an die bestehende Wix-Seite, mit einem eigenen, grün gestalteten **Nachhaltigkeits-Register**.

## Seiten

| Datei | Inhalt |
|-------|--------|
| `index.html` | Startseite (one-page): Start · Über uns · Produkte · Karriere · Kontakt + Nachhaltigkeits-Teaser |
| `nachhaltigkeit.html` | Register „Nachhaltigkeit" — Konzept, Maßnahmen, nachhaltige Produkte, Rebrand „Make Office Green Again" |
| `WIX-NACHHALTIGKEIT.md` | Alle Texte des Registers als Copy-&-Paste-Vorlage für den Wix-Editor |
| `assets/` | Neues grünes Logo + Produktfotos |

Beide HTML-Dateien sind **selbstständig** (Inline-CSS/-JS, keine Build-Schritte, keine externen JS-Abhängigkeiten außer Google Fonts).

## Struktur der Startseite

1. **Start (Hero)** — Tagline „Weil der Arbeitsplatz mehr sein darf als nur ein Ort zum Arbeiten"
2. **Über uns** — Team, Werte, transparente Firmendaten
3. **Kennzahlen** — animierte Stats
4. **Produkte** — 8 Produktkategorien
5. **Nachhaltigkeit (Teaser)** — Vorschau mit Link ins Register
6. **Karriere** — Abteilungen der Übungsfirma
7. **Kontakt** — Kontaktdaten + Formular (Client-seitige Validierung)
8. **Footer** — Links, Rechtliches, Übungsfirma-Hinweis

## Nachhaltigkeits-Register (`nachhaltigkeit.html`)

Mischung aus dem Nachhaltigkeitskonzept (Präsentation) und den neuen Produkten:
Drei Säulen · Leitprinzip „belegbar statt behauptet" · Maßnahmen (Einkauf/Versand/Büroalltag) ·
geprüfte Siegel · CO₂-neutraler Versand · 4 nachhaltige Produkte mit Fotos · Umweltleitbild ·
neues Logo/Rebrand · Vorteile · Quick-Wins-Roadmap.

## Design-Tokens

| Rolle | Startseite | Register |
|-------|-----------|----------|
| Akzent | Marken-Rot `#C0362F` | Grün `#1F8A4C` / `#15633A` |
| Text | `#16191D` | `#16191D` |
| Hintergrund | `#F6F6F3` | `#F4F8F3` |
| Schriften | Manrope (Headlines) · Inter (Text) | identisch |

## Vorschau / Deployment

Kein Build nötig — Datei direkt im Browser öffnen oder statisch hosten:

```bash
python3 -m http.server 8080
# dann http://localhost:8080
```

Deploybar auf Netlify, Vercel, GitHub Pages oder jedem Webserver.
Für die echte Wix-Seite: Inhalte aus `WIX-NACHHALTIGKEIT.md` in ein neues Register einfügen.

## Hinweis

Stuff4Staff ist eine **Übungsfirma**. Waren- und Zahlungsverkehr erfolgen ausschließlich zu
Ausbildungszwecken im Netzwerk der Übungsfirmen — keine realen Lieferungen oder Zahlungen.
