# Stuff4Staff GmbH — Website

Moderne, statische Website für **Stuff4Staff Handels GmbH**, die Übungsfirma der HAK Kirchdorf an der Krems — nachhaltiger Großhandel für gesundheitsfördernde Büromöbel, Kaffeevollautomaten, erlesenen Kaffee und Genussartikel.

Durchgängiger **„Make Office Green Again"-Look** (grüner Rebrand aus dem Nachhaltigkeitskonzept) mit einem eigenen **Nachhaltigkeits-Register**.

## Dateien

| Datei | Inhalt |
|-------|--------|
| `index.html` | Startseite (one-page): Start · Über uns · Produkte · Karriere · Kontakt + Nachhaltigkeits-Teaser |
| `nachhaltigkeit.html` | Register „Nachhaltigkeit" — Konzept, Maßnahmen, nachhaltige Produkte, Rebrand |
| `impressum.html` · `agb.html` · `datenschutz.html` | Rechtsseiten (Übungsfirma-Mustertexte) |
| `WIX-NACHHALTIGKEIT.md` | Alle Register-Texte als Copy-&-Paste-Vorlage für den Wix-Editor |
| `DEPLOY.md` | Anleitung: Seite öffnen & online stellen |
| `assets/` | Grünes Logo + Produktfotos |

Alle HTML-Dateien sind **selbstständig** (Inline-CSS/-JS, kein Build-Schritt, keine externen JS-Abhängigkeiten außer Google Fonts).

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

| Rolle | Wert |
|-------|------|
| Akzent | Blattgrün `#1F8A4C` · Tannengrün `#15633A` · Dunkelgrün `#0E3A20` |
| Text | `#16191D` |
| Hintergrund | `#F4F8F3` |
| Schriften | Manrope (Headlines) · Inter (Text) |

## Vorschau & Deployment

Kein Build nötig. Schnellster Weg: `index.html` im Browser öffnen oder

```bash
python3 -m http.server 8080   # dann http://localhost:8080
```

Zum Online-Stellen (GitHub Pages / Netlify / Vercel) siehe **`DEPLOY.md`**.
Für die echte Wix-Seite: Inhalte aus `WIX-NACHHALTIGKEIT.md` in ein neues Register einfügen.

## Hinweis

Stuff4Staff ist eine **Übungsfirma**. Waren- und Zahlungsverkehr erfolgen ausschließlich zu
Ausbildungszwecken im Netzwerk der Übungsfirmen — keine realen Lieferungen oder Zahlungen.
Die Rechtsseiten sind Mustertexte und ersetzen keine Rechtsberatung.
