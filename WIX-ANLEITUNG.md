# Wix-Anleitung — Stuff4Staff auf „Make Office Green Again" umstellen

Komplette Schritt-für-Schritt-Anleitung, um deine **Wix-Seite** an das neue grüne Design
anzupassen, das **Register „Nachhaltigkeit"** zu ergänzen und die **Rechtsseiten** anzulegen.

> Den Wix-Editor kann ich nicht direkt bearbeiten — diese Anleitung führt dich durch alles.
> Die fertigen Register-Texte stehen in **`WIX-NACHHALTIGKEIT.md`**.
> Bilder (Logo, Produktfotos) liegen im Ordner **`assets/`** (auf GitHub: *Code → Download ZIP*).

---

## 0) Vorbereitung
1. Bei [wix.com](https://www.wix.com) einloggen → Seite **stuff4staff** → **Website bearbeiten**.
2. Aus dem Repo die Bilder herunterladen (Ordner `assets/`):
   `logo-green.png`, `leaf.png`, `produkt-drehsessel.png`, `produkt-regal-ramin.png`,
   `produkt-kaffeeautomat-ocx.png`, `produkt-heissgetraenkeautomat.png`.

---

## 1) Branding global einstellen

### Farben  (Editor → links **Website-Design** → **Farben** / „Farbe & Text bearbeiten")
Lege diese Palette an:

| Rolle | HEX |
|------|-----|
| Hauptfarbe (Grün) | `#1F8A4C` |
| Dunkelgrün (Hover/Buttons) | `#15633A` |
| Tiefgrün (Topbar/Footer) | `#0E3A20` |
| Hellgrün (Flächen/Badges) | `#E7F4EC` |
| Text (Anthrazit) | `#16191D` |
| Hintergrund | `#F4F8F3` |

### Schriften  (Website-Design → **Text-Themes**)
- **Überschriften:** „Manrope" (falls nicht vorhanden: *Poppins* oder Wix „Madefor Display"), fett.
- **Fließtext:** „Inter" (Alternative: *Open Sans* oder Wix „Madefor Text").

### Logo & Favicon
1. **Logo austauschen:** altes Logo anklicken → Bild ersetzen → `logo-green.png`.
   (Oder Textlogo „Stuff**4**Staff" mit grüner **4**.)
2. **Favicon:** Einstellungen → **Favicon** → `leaf.png` hochladen.
3. **Slogan/Tagline:** „Make Office Green Again".

---

## 2) Menü / Register-Struktur  (Editor → **Seiten & Menü**)
Sorge für diese Reihenfolge (Register = Menüpunkte):

```
Start · Über uns · Unsere Produkte · Nachhaltigkeit · Karriere · Kontakt
   (im Footer/„Mehr": Impressum · AGB · Datenschutz)
```
- **Neue Seite:** „+ Seite hinzufügen" → Name eingeben → erscheint automatisch im Menü.
- **Verschieben/Umbenennen:** Punkt anklicken → ziehen bzw. „Umbenennen".
- **In den Footer legen:** Seite anlegen, dann im Menü „Aus Hauptmenü entfernen" und im
  Footer manuell verlinken (für die Rechtsseiten empfohlen).

---

## 3) Startseite — Abschnitte & Texte
Tipp: Jeder Abschnitt = ein **Streifen/Strip**. Texte zum Einfügen:

**Hero (oben):**
- Label: *Nachhaltiger Großhandel · Make Office Green Again*
- Überschrift: **Weil der Arbeitsplatz mehr sein darf als nur ein Ort zum Arbeiten.**
- Text: *Stuff4Staff Handels GmbH ist nachhaltiger Großhändler für gesundheitsfördernde Büromöbel, Kaffeevollautomaten, erlesenen Kaffee und Genussartikel — die Übungsfirma der HAK Kirchdorf an der Krems.*
- Buttons: „Unsere Produkte" · „Nachhaltigkeit entdecken"

**Über uns:**
- Überschrift: **Eine Übungsfirma mit echtem Anspruch**
- Text: *Wir sind ein Team aus neun Schülerinnen und Schülern der HAK Kirchdorf an der Krems. Als Übungsfirma bilden wir reale Geschäftsprozesse ab — vom Einkauf über Marketing bis zum Verkauf.*
- Werte: Qualität & Professionalität · Vertrauensvolle Lieferanten · Faires Miteinander · Nachhaltigkeit (belegbar statt behauptet)
- Firmendaten: Stuff4Staff Handels GmbH · GmbH/Übungsfirma · Träger HAK Kirchdorf · GF Mag. Regina Braunsberger · FN 1157 · UID ATU50115717 · Weinzierler Straße 22, 4560 Kirchdorf/Krems

**Unsere Produkte** (8 Kacheln):
Gesundheitsfördernde Bürostühle · Höhenverstellbare Schreibtische · Büroschränke & Regale ·
Kaffeevollautomaten · Heißgetränke- & Vendingautomaten · Erlesener Kaffee & Tee ·
Kühlschränke & Mikrowellen · Entspannungs- & Genussartikel

**Nachhaltigkeits-Teaser:**
- Überschrift: **Make Office Green Again**
- Text: *Regionale Produkte, geprüfte Siegel und CO₂-neutraler Versand — belegbar statt behauptet.*
- Button: „Mehr zur Nachhaltigkeit" → Seite **Nachhaltigkeit**

**Karriere:**
- Überschrift: **Wirtschaft echt erleben**
- Abteilungen: Einkauf & Beschaffung · Marketing & Verkauf · Buchhaltung & Finanzen · Personal & Organisation
- Button: „Jetzt bewerben" → Kontakt

**Kontakt:**
- E-Mail: stuff4staff1157@uebungsfirmen.at · Tel: +43 7582 606 81-34
- Standort: Weinzierler Straße 22, 4560 Kirchdorf/Krems · Übungsbetrieb: Montag 12:00–14:30
- Wix-Formular einfügen (Felder: Vorname, Nachname, Firma, E-Mail, Anliegen, Nachricht + DSGVO-Häkchen)
- Social: Instagram @stuff4staff · TikTok @stuff4staff

---

## 4) Register „Nachhaltigkeit" anlegen
1. Seite **Nachhaltigkeit** hinzufügen (siehe Schritt 2).
2. Abschnitte mit den fertigen Texten aus **`WIX-NACHHALTIGKEIT.md`** füllen:
   Hero → 3 Säulen → Maßnahmen (Einkauf/Versand/Büroalltag) → Siegel & CO₂ →
   **Produkte** (4 Fotos hochladen) → Umweltleitbild → Das neue Logo → Vorteile → Quick Wins → Abschluss-CTA.
3. Produktfotos zuordnen:
   - Ergonomischer Drehsessel → `produkt-drehsessel.png`
   - Büroregal „Ramin" → `produkt-regal-ramin.png`
   - Kaffeeautomat „OCX" → `produkt-kaffeeautomat-ocx.png`
   - Heißgetränkeautomat → `produkt-heissgetraenkeautomat.png`

---

## 5) Rechtsseiten anlegen (Impressum · AGB · Datenschutz)
1. Drei Seiten hinzufügen, aus dem Hauptmenü nehmen und **im Footer verlinken**.
2. Texte 1:1 übernehmen aus den fertigen Seiten im Projekt:
   - **Impressum** → Inhalt aus `impressum.html`
   - **AGB** → Inhalt aus `agb.html`
   - **Datenschutz** → Inhalt aus `datenschutz.html`
3. ⚠️ Es sind **Übungsfirma-Mustertexte** — vor echtem Einsatz fachlich prüfen lassen.

---

## 6) Mobil & Veröffentlichen
1. Oben rechts auf das **Handy-Symbol** → mobile Ansicht prüfen (Abstände, Schriftgrößen).
2. **SEO Grundlagen:** Seitentitel & Beschreibung je Seite setzen (Einstellungen → SEO).
3. Oben rechts **Veröffentlichen**. Fertig — der neue Menüpunkt „Nachhaltigkeit" ist live.

---

## Schnell-Checkliste
- [ ] Farbpalette (Grün) gesetzt
- [ ] Schriften Manrope/Inter (oder Alternativen)
- [ ] Neues Logo `logo-green.png` + Favicon `leaf.png`
- [ ] Slogan „Make Office Green Again"
- [ ] Menü: Start · Über uns · Produkte · **Nachhaltigkeit** · Karriere · Kontakt
- [ ] Register „Nachhaltigkeit" mit Texten + 4 Produktfotos
- [ ] Footer: Impressum · AGB · Datenschutz verlinkt
- [ ] Mobil geprüft & veröffentlicht
