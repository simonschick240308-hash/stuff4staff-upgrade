"""Build sprechtext.docx from the speaker script content.

Run with: python3 build_sprechtext_docx.py
"""

import os

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = os.path.join(os.path.dirname(__file__), "sprechtext.docx")

DEEP_BLUE = RGBColor(0x1E, 0x3A, 0x8A)
ORANGE = RGBColor(0xEA, 0x58, 0x0C)
GRAY = RGBColor(0x64, 0x74, 0x8B)
DARK = RGBColor(0x0F, 0x17, 0x2A)

PERSON_COLOR = {"A": DEEP_BLUE, "B": ORANGE, "C": RGBColor(0x25, 0x63, 0xEB)}


def add_heading(doc, text, size=16, color=DEEP_BLUE, space_before=14, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = color
    return p


def add_meta(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = GRAY
    return p


def add_speaker_line(doc, person, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)
    p.paragraph_format.line_spacing = 1.25
    label = p.add_run(f"Person {person}: " if person else "")
    label.bold = True
    label.font.size = Pt(11.5)
    label.font.color.rgb = PERSON_COLOR.get(person, DARK)
    body = p.add_run(text)
    body.font.size = Pt(11.5)
    body.font.color.rgb = DARK
    return p


def add_stage_direction(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = GRAY
    return p


def add_rule(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    pPr = p._p.get_or_add_pPr()
    from docx.oxml.ns import qn
    pBdr = pPr.makeelement(qn("w:pBdr"), {})
    bottom = pPr.makeelement(qn("w:bottom"), {
        qn("w:val"): "single", qn("w:sz"): "6", qn("w:space"): "1", qn("w:color"): "C7D2E8",
    })
    pBdr.append(bottom)
    pPr.append(pBdr)


SLIDES = [
    {
        "num": 1, "title": "Titelfolie", "person": "Alle", "time": "~30 Sek.",
        "lines": [
            ("A", "Hallo zusammen! Wir drei – [Name A], [Name B] und [Name C] – nehmen euch heute "
                  "mit in die Welt der Kombinatorik und Wahrscheinlichkeit."),
            ("B", "Die zentrale Frage, um die es heute geht: Wie viele Möglichkeiten gibt es "
                  "eigentlich wirklich – und warum sind das fast immer viel mehr, als man im Kopf "
                  "schätzt?"),
            ("C", "Es wird nicht nur trockene Theorie, sondern auch ein praktischer Teil, bei dem "
                  "ihr mitraten dürft. Legen wir los!"),
        ],
    },
    {
        "num": 2, "title": "Agenda & Einstiegsfragen", "person": "A", "time": "~90 Sek.",
        "lines": [
            ("A", "Kurz zur Agenda: Wir starten beim Zählprinzip, das die Basis für alles Weitere "
                  "ist. Danach schauen wir uns Permutation, Variation und Kombination an – das sind "
                  "die drei großen Werkzeuge der Kombinatorik. Dann verbinden wir das mit dem "
                  "Pascal'schen Dreieck und der Laplace-Wahrscheinlichkeit. Zum Schluss gibt's einen "
                  "praktischen Teil, bei dem ihr aktiv mitmachen müsst."),
            ("A", "Bevor wir inhaltlich einsteigen, möchte ich euch drei Fragen stellen. Ihr müsst "
                  "nichts sagen oder aufschreiben – schätzt einfach kurz im Kopf, und merkt euch eure "
                  "Schätzung."),
            ("A", "Erste Frage: Wie viele verschiedene 4-stellige PIN-Codes gibt es überhaupt?"),
            (None, "[kurze Pause]"),
            ("A", "Zweite Frage: Stellt euch vor, ihr alle in dieser Klasse tauscht gegenseitig eure "
                  "Handynummern aus – jede Person mit jeder anderen, einmal. Wie viele Austausche "
                  "finden dabei insgesamt statt?"),
            (None, "[kurze Pause]"),
            ("A", "Und drittens: Wie wahrscheinlich ist es, beim Lotto 6 aus 45 einen Sechser zu "
                  "haben?"),
            (None, "[kurze Pause]"),
            ("A", "Behaltet eure drei Schätzungen im Kopf – wir werden sie im Laufe der Präsentation "
                  "Stück für Stück auflösen. Ich gebe jetzt weiter an [Name B] für das Zählprinzip."),
        ],
    },
    {
        "num": 3, "title": "Das Zählprinzip", "person": "B", "time": "~80 Sek.",
        "lines": [
            ("B", "Das Zählprinzip ist die Grundlage von allem, was heute noch kommt. Die Idee "
                  "dahinter ist eigentlich ganz simpel: Wenn ein Vorgang aus mehreren Schritten "
                  "besteht, und es für jeden Schritt mehrere Möglichkeiten gibt, dann multipliziert "
                  "man einfach die Anzahl der Möglichkeiten pro Schritt."),
            ("B", "Schauen wir uns das an einem Beispiel an, das jeder kennt: Sich morgens anziehen. "
                  "Sagen wir, ich habe 3 Hemden, 4 Hosen und 2 Paar Schuhe zur Auswahl. Wie viele "
                  "komplette Outfits kann ich daraus zusammenstellen?"),
            ("B", "Man könnte jetzt anfangen, alles einzeln durchzuzählen – aber das Zählprinzip "
                  "macht es viel einfacher: 3 Hemden mal 4 Hosen ergibt 12 mögliche "
                  "Hemd-Hosen-Kombinationen – das seht ihr auch im Raster hier rechts. Jede dieser "
                  "12 Kombinationen kann ich jetzt noch mit 2 verschiedenen Schuhen kombinieren. "
                  "Also: 3 mal 4 mal 2 gleich 24 Outfits."),
            ("B", "Das Zählprinzip ist wirklich die Basis – Permutation, Variation und Kombination, "
                  "die jetzt kommen, sind im Grunde nur spezielle, klar definierte Anwendungsfälle "
                  "genau dieses Prinzips. Ich gebe weiter an [Name C]."),
        ],
    },
    {
        "num": 4, "title": "Permutation", "person": "C", "time": "~100 Sek.",
        "lines": [
            ("C", "Bei der Permutation geht es darum, alle Elemente einer Menge in eine Reihenfolge "
                  "zu bringen – jede Position zählt."),
            ("C", "Schauen wir uns das zuerst ohne Wiederholung an, am Beispiel von 3 Freunden – A, "
                  "B und C – die sich nebeneinander hinsetzen. Im Baumdiagramm seht ihr: Für die "
                  "erste Position gibt es 3 Möglichkeiten, für die zweite noch 2, und für die letzte "
                  "bleibt nur noch 1 übrig. Das ergibt 3 mal 2 mal 1, also 3 Fakultät, gleich "
                  "6 mögliche Sitzordnungen. Allgemein gilt: Die Anzahl der Reihenfolgen von n "
                  "Elementen ist P(n) gleich n Fakultät. Bei 5 Personen am Tisch wären das schon "
                  "5 Fakultät, also 120 Sitzordnungen – die Zahl wächst extrem schnell, das werden "
                  "wir später noch genauer sehen."),
            ("C", "Jetzt zur Permutation mit Wiederholung: Hier kommen manche Elemente mehrfach vor, "
                  "und dann muss man durch die Fakultäten dieser Wiederholungen teilen, weil sonst "
                  "Reihenfolgen doppelt gezählt würden, die eigentlich gleich aussehen."),
            ("C", "Bestes Beispiel: das Wort ANANAS. 6 Buchstaben insgesamt, aber das A kommt 3 mal "
                  "vor und das N 2 mal. Wenn wir einfach 6 Fakultät rechnen würden, hätten wir viel "
                  "zu viele Anordnungen gezählt – weil ein Vertauschen der drei A's untereinander ja "
                  "optisch gar keinen Unterschied macht. Deshalb teilen wir 6 Fakultät durch "
                  "3 Fakultät mal 2 Fakultät mal 1 Fakultät, und kommen auf 60 verschiedene "
                  "Anordnungen des Wortes ANANAS. Weiter geht's mit [Name A] und der Variation."),
        ],
    },
    {
        "num": 5, "title": "Variation", "person": "A", "time": "~100 Sek.",
        "lines": [
            ("A", "Bei der Variation wählen wir nur einen Teil – k von n Elementen – aus, und die "
                  "Reihenfolge ist wichtig."),
            ("A", "Ohne Wiederholung heißt: kein Element darf doppelt gewählt werden, wie beim "
                  "Ziehen ohne Zurücklegen. Klassisches Beispiel: ein Wettlauf mit 8 Läuferinnen und "
                  "Läufern, aber nur die Plätze 1 bis 3 zählen fürs Stockerl. Reihenfolge ist hier "
                  "extrem wichtig – Gold, Silber und Bronze sind nicht gleich! Für Platz 1 gibt es "
                  "8 Möglichkeiten, für Platz 2 noch 7, für Platz 3 noch 6. Das ergibt V(8,3) gleich "
                  "8 mal 7 mal 6, also 336 mögliche Stockerl-Besetzungen – aus nur 8 Personen!"),
            ("A", "Jetzt zur Variation mit Wiederholung: Hier darf jede Stelle erneut aus allen n "
                  "Möglichkeiten gewählt werden, ganz unabhängig von den vorherigen Stellen."),
            ("A", "Und damit lösen wir jetzt unsere allererste Frage von vorhin auf: Wie viele "
                  "4-stellige PIN-Codes gibt es? Jede der 4 Stellen kann eine Ziffer von 0 bis 9 "
                  "sein, und Wiederholungen sind erlaubt – man kann ja z.B. 1-1-1-1 als PIN haben. "
                  "Das ergibt 10 hoch 4, also genau 10.000 mögliche PIN-Codes. Vergleicht das mal "
                  "mit eurer Schätzung von vorhin! Übergabe an [Name B] für die Kombination."),
        ],
    },
    {
        "num": 6, "title": "Kombination", "person": "B", "time": "~100 Sek.",
        "lines": [
            ("B", "Bei der Kombination ist – im Unterschied zu Permutation und Variation – die "
                  "Reihenfolge völlig egal. Uns interessiert nur, WELCHE Elemente ausgewählt wurden, "
                  "nicht WANN oder in welcher Reihenfolge."),
            ("B", "Schauen wir uns das ohne Wiederholung an unserer zweiten Frage von ganz am Anfang "
                  "an: Wenn ihr alle 15 Schüler:innen in dieser Klasse gegenseitig eure Handynummern "
                  "austauscht – wie viele Austausche sind das insgesamt? Wichtig hier: Wenn A mit B "
                  "tauscht, ist das dasselbe wie wenn B mit A tauscht – die Reihenfolge ist egal, "
                  "deshalb ist das eine Kombination, keine Variation! Wir wählen 2 Personen aus 15 "
                  "aus, ohne dass die Reihenfolge zählt. Das ergibt 15 über 2, also 15 Fakultät "
                  "durch 2 Fakultät mal 13 Fakultät, und das macht genau 105 Austausche."),
            (None, "[kurze Pause]"),
            ("B", "105! Die meisten schätzen hier viel zu niedrig – irgendwo bei 15 oder vielleicht "
                  "30. Aber weil jede Person mit jeder anderen tauscht, wächst das viel schneller "
                  "als man denkt. Das war Frage Nummer 2 von ganz am Anfang."),
            ("B", "Jetzt noch kurz die Kombination mit Wiederholung, am Beispiel eines Eisbechers: "
                  "Wir wählen 3 Kugeln aus 5 Sorten, und dabei dürfen auch mehrere Kugeln derselben "
                  "Sorte gewählt werden – zum Beispiel 3 mal Schoko. Mit der Formel für Kombination "
                  "mit Wiederholung kommen wir hier auf 35 mögliche Eisbecher-Zusammenstellungen. "
                  "Weiter zu [Name C] und dem Pascal'schen Dreieck."),
        ],
    },
    {
        "num": 7, "title": "Pascal'sches Dreieck", "person": "C", "time": "~70 Sek.",
        "lines": [
            ("C", "Das Pascal'sche Dreieck ist im Grunde eine fertige Tabelle für alle "
                  "Binomialkoeffizienten – also für alle 'n über k'-Werte, die wir bei der "
                  "Kombination brauchen."),
            ("C", "Die Regel, nach der es aufgebaut ist, ist eine Rekursionsformel: Jede Zahl im "
                  "Dreieck ist die Summe der zwei Zahlen direkt darüber. n über k ist also gleich "
                  "n-minus-1 über k-minus-1, plus n-minus-1 über k."),
            ("C", "Schaut euch die orange markierte 15 im Dreieck an – das ist genau 6 über 2. "
                  "Erkennt ihr das wieder? Genauso haben wir vorhin beim Lotto-Beispiel mit "
                  "Binomialkoeffizienten gerechnet. Das Dreieck ist also nicht nur eine "
                  "mathematische Spielerei, sondern ein super praktisches Hilfsmittel, wenn man "
                  "schnell einen Binomialkoeffizienten ohne Taschenrechner abschätzen will. "
                  "Übergabe an [Name A] für die Laplace-Wahrscheinlichkeit."),
        ],
    },
    {
        "num": 8, "title": "Laplace-Wahrscheinlichkeit", "person": "A", "time": "~90 Sek.",
        "lines": [
            ("A", "Bis jetzt haben wir nur gezählt – jetzt verbinden wir das mit Wahrscheinlichkeit. "
                  "Die Laplace-Formel ist denkbar einfach: P von A gleich Betrag A durch Betrag "
                  "Omega."),
            ("A", "Betrag A sind die günstigen Fälle – also alle Ergebnisse, die unser gewünschtes "
                  "Ereignis A erfüllen. Betrag Omega ist die Anzahl aller möglichen Ergebnisse, der "
                  "komplette Ergebnisraum."),
            ("A", "Ganz wichtig dabei: Diese Formel funktioniert nur, wenn alle Ergebnisse gleich "
                  "wahrscheinlich sind – das nennt man ein Laplace-Experiment. Bei einem fairen "
                  "Würfel ist das der Fall, bei einem gezinkten Würfel nicht mehr!"),
            ("A", "Schauen wir uns das am Würfeln an: Wir werfen zwei Würfel und fragen uns, wie "
                  "wahrscheinlich ein Pasch ist – also dass beide Würfel die gleiche Zahl zeigen. "
                  "Mit dem Zählprinzip von ganz am Anfang wissen wir: Es gibt 6 mal 6, also "
                  "36 mögliche Ergebnisse – das ist unser Omega. Schaut euch die Diagonale im Raster "
                  "an: Das sind genau die 6 Fälle, in denen beide Würfel gleich sind – das ist unser "
                  "A. Also P von Pasch gleich 6 durch 36, gleich 1 durch 6."),
            ("A", "Das zeigt schön: Kombinatorik und Wahrscheinlichkeit hängen direkt zusammen – "
                  "ohne richtig zu zählen, kann man gar keine Wahrscheinlichkeit berechnen. Weiter "
                  "zu [Name B] und unserer Lotto-Frage."),
        ],
    },
    {
        "num": 9, "title": "Lotto 6 aus 45", "person": "B", "time": "~80 Sek.",
        "lines": [
            ("B", "Jetzt lösen wir die dritte und letzte Frage von ganz am Anfang auf: Wie "
                  "wahrscheinlich ist ein Sechser beim Lotto 6 aus 45?"),
            ("B", "Zuerst brauchen wir Omega – alle möglichen Tipps. Wir wählen 6 Zahlen aus 45, "
                  "Reihenfolge ist egal, also eine Kombination ohne Wiederholung: 45 über 6. Das "
                  "ergibt die unglaubliche Zahl von 8.145.060 möglichen Tipps."),
            ("B", "Und A – die für uns günstigen Fälle? Das ist genau 1: nur der eine Tipp, der "
                  "tatsächlich gezogen wird. Damit ergibt sich P von 6 Richtige gleich 1 durch "
                  "8.145.060 – das sind ungefähr 0,0000123 Prozent."),
            ("B", "Um sich das vorstellen zu können: Das ist ungefähr so wahrscheinlich, wie wenn "
                  "man unter allen 9 Millionen Einwohnerinnen und Einwohnern Österreichs zufällig "
                  "genau eine ganz bestimmte Person herauspickt. Jetzt haben wir alle drei "
                  "Einstiegsfragen beantwortet – Zeit für den praktischen Teil! Übergabe an "
                  "[Name C]."),
        ],
    },
    {
        "num": 10, "title": "Praktischer Teil: Estimation-Spiel", "person": "C", "time": "~40 Sek.",
        "lines": [
            ("C", "Jetzt seid ihr dran! Wir machen ein kleines Schätzspiel mit zwei Runden."),
            ("C", "So funktioniert's: Wir stellen euch jeweils eine überraschende Frage. Jede "
                  "Person schätzt für sich selbst, still im Kopf oder auf einem Zettel – bitte "
                  "keinen Taschenrechner und kein Absprechen mit dem Sitznachbarn! Dann rechnen wir "
                  "gemeinsam die richtige Antwort aus, und ihr seht, wie nahe ihr dran wart."),
            ("C", "Zwei Runden – seid ihr bereit?"),
        ],
    },
    {
        "num": 11, "title": "Runde 1: Eure Schätzung", "person": "A", "time": "~60 Sek.",
        "lines": [
            ("A", "Hier die erste Frage: Stellt euch vor, ihr alle verlasst nacheinander, einer nach "
                  "dem anderen, das Klassenzimmer. Wie viele verschiedene Reihenfolgen gibt es dafür "
                  "– für euch 15 Schüler:innen?"),
            (None, "[30–45 Sekunden Zeit zum Schätzen geben]"),
            ("A", "Schreibt eure Schätzung auf oder merkt sie euch gut – wir vergleichen gleich!"),
            (None, "[kurze Handzeichen-Abfrage: 'Wer schätzt unter 1.000? Unter 1 Million? Über "
                   "1 Milliarde?']"),
            ("A", "Übergabe an [Name B] für die Auflösung."),
        ],
    },
    {
        "num": 12, "title": "Runde 1: Auflösung", "person": "B", "time": "~70 Sek.",
        "lines": [
            ("B", "Das hier ist genau die Permutation von 15 Personen – P(15) gleich 15 Fakultät. "
                  "Und 15 Fakultät ist..."),
            (None, "[kurze Pause, auf die Folie zeigen]"),
            ("B", "...1.307.674.368.000. Über 1,3 Billionen! Damit das greifbar wird: Stellt euch "
                  "vor, ihr probiert ab jetzt eine Reihenfolge pro Sekunde durch, ohne Pause. Wie "
                  "lange würdet ihr brauchen, um wirklich alle durchzuprobieren? Die Antwort: "
                  "ungefähr 41.466 Jahre. Wenn man heute damit anfangen würde, hätte man um ca. "
                  "39.000 vor Christus begonnen – das ist die Steinzeit, also bevor es überhaupt "
                  "Schrift, Landwirtschaft oder sesshafte Siedlungen gab!"),
            ("B", "Das zeigt: 15 Fakultät heißt 15 mal 14 mal 13 und so weiter bis 1 – die Fakultät "
                  "wächst astronomisch schnell. Schon bei nur 15 Elementen übersteigt das Ergebnis "
                  "1,3 Billionen. Übergabe an [Name C] für Runde 2."),
        ],
    },
    {
        "num": 13, "title": "Runde 2: Eure Schätzung", "person": "C", "time": "~60 Sek.",
        "lines": [
            ("C", "Runde 2, und jetzt wird's richtig groß: Wie viele verschiedene Möglichkeiten "
                  "gibt es, ein Standard-Kartenspiel mit 52 Karten zu mischen?"),
            ("C", "Kleiner Tipp dazu: Das ist eine Permutation von 52 Elementen, also P(52) gleich "
                  "52 Fakultät."),
            (None, "[Zeit zum Schätzen geben]"),
            (None, "[Handzeichen-Abfrage: 'Wer sagt mehr als 1.000? 1 Million? 1 Milliarde? "
                   "1 Trillion?']"),
            ("C", "Übergabe an [Name A] für die Auflösung."),
        ],
    },
    {
        "num": 14, "title": "Runde 2: Auflösung", "person": "A", "time": "~80 Sek.",
        "lines": [
            ("A", "52 Fakultät ist ungefähr 8,07 mal 10 hoch 67 – eine Zahl mit 68 Stellen!"),
            ("A", "Damit ihr eine Vorstellung davon kriegt, wie riesig das ist: Das gesamte "
                  "sichtbare Universum hat schätzungsweise 10 hoch 80 Atome. 52 Fakultät ist zwar "
                  "immer noch kleiner als das – aber stellt euch vor: Wenn seit dem Urknall JEDES "
                  "einzelne Atom im Universum JEDE Sekunde eine komplett neue Reihenfolge bilden "
                  "würde, gäbe es bis heute trotzdem kaum Wiederholungen."),
            ("A", "Die Schlussfolgerung daraus: Fast jede Kartenmischung, die du jemals in deinem "
                  "Leben machst, ist mit an Sicherheit grenzender Wahrscheinlichkeit einzigartig in "
                  "der gesamten Menschheitsgeschichte – noch nie zuvor in genau dieser Reihenfolge "
                  "gemischt worden, und wird es wahrscheinlich auch nie wieder. Übergabe an "
                  "[Name B] für die Zusammenfassung."),
        ],
    },
    {
        "num": 15, "title": "Übersichtstabelle", "person": "B", "time": "~70 Sek.",
        "lines": [
            ("B", "Bevor wir zusammenfassen, hier noch die kompakte Übersicht über alles, was wir "
                  "heute besprochen haben."),
            ("B", "Der Trick, um in der Matura schnell die richtige Formel zu finden, sind "
                  "eigentlich nur zwei Fragen: Erstens – ist die Reihenfolge wichtig? Wenn ja, sind "
                  "wir bei Variation oder Permutation, wenn alle Elemente verwendet werden. Wenn die "
                  "Reihenfolge egal ist, sind wir bei Kombination."),
            ("B", "Zweitens – wird mit oder ohne Wiederholung gewählt, also mit oder ohne "
                  "Zurücklegen? Das entscheidet, welche der beiden Formel-Varianten man nimmt."),
            ("B", "Mit diesen zwei Fragen kommt man bei jeder Kombinatorik-Aufgabe in der Matura "
                  "zur richtigen Formel. Übergabe an alle drei für die Zusammenfassung."),
        ],
    },
    {
        "num": 16, "title": "Zusammenfassung", "person": "Alle", "time": "~60 Sek.",
        "lines": [
            ("A", "Mein wichtigster Punkt für heute: Das Zählprinzip ist die Basis von allem. Bei "
                  "unabhängigen Schritten einfach die Möglichkeiten pro Schritt multiplizieren – "
                  "daraus folgt am Ende alles andere."),
            ("B", "Für mich: Zwei Fragen führen euch zur richtigen Formel – Ist die Reihenfolge "
                  "wichtig? Und: Wird mit Wiederholung gewählt? Wenn ihr diese zwei Fragen stellt, "
                  "findet ihr in der Matura immer die passende Formel."),
            ("C", "Und von mir: Mit Laplace, P von A gleich Betrag A durch Betrag Omega, werden aus "
                  "abstrakten Kombinatorik-Formeln ganz konkrete Wahrscheinlichkeiten – egal ob beim "
                  "Würfeln, beim Lotto, oder beim Kartenmischen."),
        ],
    },
    {
        "num": 17, "title": "Quellen", "person": "Alle", "time": "~20 Sek.",
        "lines": [
            ("A", "Hier kurz unsere Quellen – Lehrplan und Formelsammlung vom BMBWF, unser "
                  "Schulbuch, mathe-online.at, die Österreichischen Lotterien für die Lotto-Daten, "
                  "und Wikipedia für die Begriffsdefinitionen. Alle Diagramme und Grafiken haben wir "
                  "selbst mit Python erstellt."),
        ],
    },
    {
        "num": 18, "title": "Danke / Fragen", "person": "Alle", "time": "~20 Sek.",
        "lines": [
            ("A", "Damit sind wir am Ende unserer Präsentation."),
            ("B", "Danke für eure Aufmerksamkeit!"),
            ("C", "Habt ihr noch Fragen? Oder – was war eure überraschendste Zahl heute?"),
        ],
    },
]


def build():
    doc = Document()

    # Base style
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    for section in doc.sections:
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = title.add_run("Sprechtext – Kombinatorik & Wahrscheinlichkeit")
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = DEEP_BLUE

    add_meta(doc, "Vollständiges Sprechskript für alle 18 Folien. A → B → C rotierend. "
                  "Zieldauer: ca. 20–25 Minuten (Zeitangaben sind Richtwerte).")

    note = doc.add_paragraph()
    note.paragraph_format.space_after = Pt(14)
    r = note.add_run("Hinweis: Das ist ein Gerüst zum Üben, nicht zum Ablesen! Lest es ein paar Mal "
                      "durch, dann sagt es mit euren eigenen Worten – das wirkt natürlicher und ihr "
                      "wirkt sicherer.")
    r.font.size = Pt(10.5)
    r.font.color.rgb = GRAY
    r.italic = True

    add_rule(doc)

    for slide in SLIDES:
        add_heading(doc, f"Folie {slide['num']} – {slide['title']} "
                          f"(Person {slide['person']})")
        add_meta(doc, slide["time"])
        for person, text in slide["lines"]:
            if person is None:
                add_stage_direction(doc, text)
            else:
                add_speaker_line(doc, person, text)
        add_rule(doc)

    add_heading(doc, "Gesamtdauer-Check", size=14)
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(
        "Reine Sprechzeit liegt bei ca. 20–21 Minuten. Mit den eingeplanten Pausen für das "
        "Schätzspiel (Runde 1 + Runde 2, je 30–60 Sek. Stille + kurze Handzeichen-Abfrage) und "
        "etwas Luft zum natürlichen Sprechen kommt ihr realistisch auf 22–25 Minuten – genau im "
        "Zielbereich."
    )
    r.font.size = Pt(11)

    p2 = doc.add_paragraph()
    label = p2.add_run("Tipp: ")
    label.bold = True
    label.font.size = Pt(11)
    body = p2.add_run(
        "Übt die Übergaben zwischen den Personen extra – „Übergabe an [Name]“ sollte "
        "flüssig klingen, nicht abgelesen. Am besten merkt sich jede:r nur den letzten Satz der "
        "eigenen Folie und den ersten Satz der eigenen nächsten Folie auswendig, den Rest in "
        "eigenen Worten erzählen."
    )
    body.font.size = Pt(11)

    doc.save(OUT)
    print(f"Saved {OUT}")


if __name__ == "__main__":
    build()
