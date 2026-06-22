# Website öffnen & veröffentlichen

Kurzanleitung, wie du die Seite **ansehen** und **online stellen** kannst.

> Tipp: Die Dateien liegen aktuell im GitHub-Repo auf dem Branch
> `claude/trusting-archimedes-n3igpj`.

---

## A) Schnell ansehen (lokal, ohne Internet-Server)

**Variante 1 – Doppelklick (am einfachsten):**
1. Auf GitHub oben auf **Code → Download ZIP** klicken (Branch `claude/trusting-archimedes-n3igpj`).
2. ZIP entpacken.
3. Datei **`index.html`** doppelklicken → öffnet sich im Browser.
   Über das Menü „Nachhaltigkeit" kommst du auf das neue Register.

> Funktioniert offline. Nur die Schriftarten kommen aus dem Internet — ohne Netz
> nutzt der Browser automatisch eine Ersatzschrift, das Layout bleibt gleich.

**Variante 2 – lokaler Mini-Server (saubere Pfade):**
```bash
# im entpackten Ordner ausführen (Python ist auf den meisten PCs vorhanden)
python3 -m http.server 8080
```
Dann im Browser **http://localhost:8080** öffnen.

---

## B) Online stellen — kostenlos

### Option 1: GitHub Pages  ⭐ empfohlen (Repo ist schon auf GitHub)
1. Repo → **Settings → Pages**.
2. Bei **„Build and deployment" → Source: „Deploy from a branch"**.
3. Branch **`claude/trusting-archimedes-n3igpj`**, Ordner **`/ (root)`** → **Save**.
4. Nach 1–2 Minuten ist die Seite live unter:
   **https://simonschick240308-hash.github.io/stuff4staff-upgrade/**

*Alternative (modern):* Source auf **„GitHub Actions"** stellen — dann übernimmt der
mitgelieferte Workflow `.github/workflows/pages.yml` das Deployment automatisch bei
jedem Push auf `main` (oder manuell über den **Actions**-Tab → „Run workflow").

### Option 2: Netlify (Drag & Drop)
1. Auf [app.netlify.com/drop](https://app.netlify.com/drop) gehen.
2. Den **entpackten Projektordner** ins Fenster ziehen → sofort live.
   *(Oder Repo verbinden — die `netlify.toml` ist schon konfiguriert, kein Build nötig.)*

### Option 3: Vercel
1. Auf [vercel.com/new](https://vercel.com/new) das GitHub-Repo importieren.
2. Framework: **„Other / Static"**, keine Build-Einstellungen nötig
   (`vercel.json` liegt bei) → **Deploy**.

---

## C) Und die echte Wix-Seite?

Den Wix-Editor kann ich nicht direkt bearbeiten. Zwei Wege:
- **Diese Code-Seite live nehmen** (Option B) und ggf. eure Domain darauf zeigen lassen
  — dann ersetzt sie die Wix-Seite.
- **In Wix bleiben:** Lege dort ein neues Register „Nachhaltigkeit" an und füge die
  fertigen Texte aus **`WIX-NACHHALTIGKEIT.md`** ein (Schritt-für-Schritt dort enthalten).

---

## Dateiübersicht
| Datei | Inhalt |
|-------|--------|
| `index.html` | Startseite (grüner „Make Office Green Again"-Look) |
| `nachhaltigkeit.html` | Register „Nachhaltigkeit" + Produkte |
| `impressum.html` · `agb.html` · `datenschutz.html` | Rechtsseiten |
| `WIX-NACHHALTIGKEIT.md` | Texte zum Einfügen in Wix |
| `assets/` | Logo + Produktfotos |
