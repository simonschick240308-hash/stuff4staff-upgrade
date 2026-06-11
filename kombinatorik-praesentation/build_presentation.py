"""Build the Kombinatorik & Wahrscheinlichkeit presentation (.pptx).

Run with: python3 build_presentation.py
Outputs kombinatorik_praesentation.pptx in this directory.
"""

import os

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

from theme import (
    DEEP_BLUE, MID_BLUE, LIGHT_BLUE, ORANGE, YELLOW, DARK, GRAY, WHITE, BG,
    FONT_HEAD, FONT_BODY,
)
from slide_helpers import (
    SLIDE_W, SLIDE_H, MARGIN, new_slide, add_rect, add_title_bar, add_text,
    add_bullets, add_picture, add_picture_fit, add_formula, add_label_chip,
    add_panel, set_notes, page_number, no_bullet, add_colored_word, add_circle_badge,
)

CONTENT_LEFT = Inches(0.5)
CONTENT_TOP = Inches(1.35)
CONTENT_W = Inches(12.333)
COL_W = Inches(5.85)
COL2_LEFT = Inches(6.983)
ROW_H = Inches(2.78)
ROW2_TOP = Inches(4.28)


# ---------------------------------------------------------------------------
# Slide 1 - Titelfolie
# ---------------------------------------------------------------------------

def slide_01_title(prs):
    slide = new_slide(prs, bg=DEEP_BLUE)

    add_rect(slide, Inches(10.6), Inches(-1.2), Inches(4.0), Inches(4.0), fill=MID_BLUE, shape=MSO_SHAPE.OVAL)
    add_rect(slide, Inches(-1.3), Inches(5.1), Inches(3.6), Inches(3.6), fill=ORANGE, shape=MSO_SHAPE.OVAL)
    add_rect(slide, Inches(11.9), Inches(5.7), Inches(2.1), Inches(2.1), fill=YELLOW, shape=MSO_SHAPE.OVAL)

    add_text(slide, "MATURA MATHEMATIK  ·  STOCHASTIK", Inches(0.9), Inches(2.0), Inches(11.5), Inches(0.5),
             size=Pt(16), color=YELLOW, bold=True, font=FONT_BODY)
    add_text(slide, "Kombinatorik & Wahrscheinlichkeit", Inches(0.9), Inches(2.5), Inches(11.5), Inches(1.4),
             size=Pt(48), color=WHITE, bold=True, font=FONT_HEAD)
    add_text(slide, "Wie viele Möglichkeiten gibt es wirklich?", Inches(0.9), Inches(3.75), Inches(11.5), Inches(0.7),
             size=Pt(22), color=LIGHT_BLUE, italic=True, font=FONT_BODY)

    add_text(slide, "Vorgetragen von Person A, Person B & Person C", Inches(0.9), Inches(6.3), Inches(11.5), Inches(0.5),
             size=Pt(16), color=WHITE, font=FONT_BODY)
    add_text(slide, "5. Klasse HAK · Angewandte Mathematik", Inches(0.9), Inches(6.75), Inches(11.5), Inches(0.4),
             size=Pt(13), color=GRAY, font=FONT_BODY)

    set_notes(slide, "Begrüßung durch alle drei Vortragenden, kurze Vorstellung. "
              "Ziel der Präsentation nennen: Nach den nächsten 35-40 Minuten könnt ihr Kombinatorik-Aufgaben "
              "erkennen und lösen - und versteht, warum z.B. ein Lotto-Sechser so unwahrscheinlich ist. "
              "Überleitung zu Person A für die Agenda.")
    return slide


# ---------------------------------------------------------------------------
# Slide 2 - Agenda + Einstiegsfrage (Hook)
# ---------------------------------------------------------------------------

def slide_02_agenda(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Agenda & Einstiegsfrage", person="A", kicker="Heute auf dem Programm")

    add_bullets(slide, [
        "Das Zählprinzip - die Grundlage von allem",
        "Permutation - wie viele Reihenfolgen gibt es?",
        "Variation - Reihenfolge zählt, nicht alle werden gewählt",
        "Kombination - Auswahl ohne Reihenfolge (z. B. Lotto)",
        "Pascal'sches Dreieck & Binomialkoeffizient",
        "Laplace-Wahrscheinlichkeit - von Zählen zu Chancen",
        "Quiz, Übersicht & Zusammenfassung",
    ], CONTENT_LEFT, CONTENT_TOP, COL_W, Inches(5.6), size=Pt(18), space_after=Pt(14))

    add_panel(slide, COL2_LEFT, CONTENT_TOP, COL_W, Inches(5.6), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "EINSTIEGSFRAGE", COL2_LEFT + Inches(0.35), CONTENT_TOP + Inches(0.35),
                    fill=ORANGE, width=Inches(2.6), height=Inches(0.5))
    add_text(slide, "Dein Handy hat einen 4-stelligen PIN-Code (Ziffern 0-9).",
             COL2_LEFT + Inches(0.35), CONTENT_TOP + Inches(1.1), COL_W - Inches(0.7), Inches(1.1),
             size=Pt(20), color=DEEP_BLUE, bold=True)
    add_text(slide, "Wie viele verschiedene PINs sind möglich?",
             COL2_LEFT + Inches(0.35), CONTENT_TOP + Inches(2.15), COL_W - Inches(0.7), Inches(0.7),
             size=Pt(20), color=DARK)
    add_colored_word(slide, [(c, ORANGE) for c in "????"], COL2_LEFT, CONTENT_TOP + Inches(3.0), COL_W, Inches(1.2),
                      size=Pt(60))
    add_text(slide, "Wir lösen das in wenigen Minuten - bei der Variation mit Wiederholung!",
             COL2_LEFT + Inches(0.35), CONTENT_TOP + Inches(4.5), COL_W - Inches(0.7), Inches(0.9),
             size=Pt(14), color=GRAY, italic=True)

    page_number(slide, 2)
    set_notes(slide, "Person A stellt die Agenda vor und liest die Einstiegsfrage laut vor. "
              "Schätzungen aus dem Publikum zulassen (10? 100? 10.000?) - die Auflösung "
              "kommt erst bei der Variation mit Wiederholung (Folie 7). Überleitung zu Person B: "
              "'Bevor wir das beantworten können, brauchen wir das Zählprinzip.'")
    return slide


# ---------------------------------------------------------------------------
# Slide 3 - Zählprinzip (Outfit-Kombinationen)
# ---------------------------------------------------------------------------

def slide_03_zaehlprinzip(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Das Zählprinzip", person="B", kicker="Die Grundlage der Kombinatorik")

    add_text(slide, "Besteht ein Vorgang aus mehreren Schritten und gibt es für jeden "
             "Schritt mehrere Möglichkeiten, so multipliziert man die Anzahl der "
             "Möglichkeiten pro Schritt:",
             CONTENT_LEFT, CONTENT_TOP, COL_W, Inches(1.7), size=Pt(18))
    add_formula(slide, "f_zaehlprinzip", box_left=CONTENT_LEFT, box_top=Inches(3.0),
                 box_width=COL_W, box_height=Inches(1.0))

    add_panel(slide, CONTENT_LEFT, Inches(4.3), COL_W, Inches(2.55), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "BEISPIEL: OUTFIT", CONTENT_LEFT + Inches(0.3), Inches(4.55), fill=ORANGE,
                    width=Inches(2.6), height=Inches(0.45), size=Pt(14))
    add_text(slide, "3 Hemden  ×  4 Hosen  ×  2 Paar Schuhe\n"
             "Wie viele komplette Outfits sind möglich?",
             CONTENT_LEFT + Inches(0.3), Inches(5.15), COL_W - Inches(0.6), Inches(1.6), size=Pt(16))

    add_picture_fit(slide, "outfit_grid.png", COL2_LEFT, CONTENT_TOP, COL_W, Inches(4.25))
    add_text(slide, "Das Raster zeigt 3 Hemden × 4 Hosen = 12 Kombinationen. "
             "Für jede davon gibt es noch 2 Paar Schuhe → 12 × 2 = 24.",
             COL2_LEFT, Inches(5.55), COL_W, Inches(0.8), size=Pt(13), color=GRAY, align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_outfits", box_left=COL2_LEFT, box_top=Inches(6.25),
                 box_width=COL_W, box_height=Inches(0.85))

    page_number(slide, 3)
    set_notes(slide, "Person B erklärt das Zählprinzip Schritt für Schritt am Outfit-Beispiel: "
              "für jedes der 3 Hemden gibt es 4 Hosen -> 12 Kombinationen, für jede davon 2 Paar Schuhe "
              "-> 3*4*2=24 Outfits. Betonen: Das Zählprinzip ist die Basis für ALLE folgenden Formeln "
              "(Permutation, Variation, Kombination)! Überleitung zu Person C: 'Was passiert, wenn wir "
              "ALLE Elemente in eine Reihenfolge bringen wollen?'")
    return slide


# ---------------------------------------------------------------------------
# Slide 4 - Permutation (ohne & mit Wiederholung)
# ---------------------------------------------------------------------------

def slide_04_permutation(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Permutation", person="C", kicker="Sitzordnung & Anagramm")

    # Band 1: ohne Wiederholung
    add_label_chip(slide, "OHNE WIEDERHOLUNG", CONTENT_LEFT, CONTENT_TOP, fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_permutation_ohne", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(0.6), height=Inches(0.55))
    add_text(slide, "Alle n Elemente werden in einer Reihenfolge angeordnet - jede Position zählt.",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.35), COL_W, Inches(0.8), size=Pt(14))
    add_text(slide, "Beispiel: 5 Personen an einem Tisch →",
             CONTENT_LEFT, CONTENT_TOP + Inches(2.05), Inches(3.6), Inches(0.6), size=Pt(14))
    add_formula(slide, "f_beispiel_5fakultaet", left=CONTENT_LEFT + Inches(3.7), top=CONTENT_TOP + Inches(2.0),
                 height=Inches(0.5))

    add_picture_fit(slide, "permutation_tree.png", COL2_LEFT, CONTENT_TOP - Inches(0.05), COL_W, Inches(2.15))
    add_text(slide, "3 Freunde (A, B, C): jede Reihenfolge ist eine eigene Permutation → 3! = 6",
             COL2_LEFT, CONTENT_TOP + ROW_H - Inches(0.55), COL_W, Inches(0.55),
             size=Pt(13), color=GRAY, align=PP_ALIGN.CENTER)

    # Band 2: mit Wiederholung
    add_label_chip(slide, "MIT WIEDERHOLUNG", CONTENT_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_permutation_mit", left=CONTENT_LEFT, top=ROW2_TOP + Inches(0.6), height=Inches(0.6))
    add_text(slide, "Manche Elemente sind nicht unterscheidbar (z. B. gleiche Buchstaben) - "
             "wir teilen durch deren Fakultäten, damit wir nicht doppelt zählen.",
             CONTENT_LEFT, ROW2_TOP + Inches(1.4), COL_W, Inches(1.3), size=Pt(14))

    add_label_chip(slide, "BEISPIEL: ANAGRAMM", COL2_LEFT, ROW2_TOP, fill=MID_BLUE,
                    width=Inches(2.9), height=Inches(0.45), size=Pt(13))
    add_colored_word(slide, [
        ("A", DEEP_BLUE), ("N", ORANGE), ("A", DEEP_BLUE),
        ("N", ORANGE), ("A", DEEP_BLUE), ("S", MID_BLUE),
    ], COL2_LEFT, ROW2_TOP + Inches(0.55), COL_W, Inches(0.9), size=Pt(40))
    add_text(slide, "Wie viele unterschiedliche Anordnungen der Buchstaben von ANANAS gibt es?",
             COL2_LEFT, ROW2_TOP + Inches(1.5), COL_W, Inches(0.7), size=Pt(13), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_ananas", box_left=COL2_LEFT, box_top=ROW2_TOP + Inches(2.05),
                 box_width=COL_W, box_height=Inches(0.7))

    page_number(slide, 4)
    set_notes(slide, "Person C erklärt zuerst die Permutation ohne Wiederholung anhand des Baumdiagramms "
              "(3 Freunde -> 6 Sitzordnungen) und rechnet danach 5! = 120 für 5 Personen vor. "
              "Danach das ANANAS-Beispiel: 6 Buchstaben, aber A kommt 3x und N 2x vor - deshalb "
              "6!/(3!*2!*1!) = 60 statt 6! = 720. Überleitung zu Person A für die erste Übungsaufgabe.")
    return slide


# ---------------------------------------------------------------------------
# Slide 5 - Aufgabe für euch (Teil 1)
# ---------------------------------------------------------------------------

def slide_05_aufgabe1(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Aufgabe für euch - Teil 1", person="A", kicker="Zählprinzip & Permutation")

    panel_h = Inches(5.3)
    add_panel(slide, CONTENT_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "1", CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=DEEP_BLUE)
    add_label_chip(slide, "ZÄHLPRINZIP", CONTENT_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=DEEP_BLUE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "Eine Pizzeria bietet 3 Größen, 5 Saucen und 2 Käsesorten an.\n\n"
             "Wie viele verschiedene Pizzen kann man daraus zusammenstellen?",
             CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(2.6), size=Pt(18))

    add_panel(slide, COL2_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "2", COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=ORANGE)
    add_label_chip(slide, "PERMUTATION", COL2_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=ORANGE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "6 Freund:innen wollen sich für ein Gruppenfoto nebeneinander aufstellen.\n\n"
             "Wie viele verschiedene Anordnungen sind möglich?",
             COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(2.6), size=Pt(18))

    add_text(slide, "Überlegt in Zweier- oder Dreiergruppen - ca. 2 Minuten Zeit!",
             CONTENT_LEFT, CONTENT_TOP + panel_h + Inches(0.15), CONTENT_W, Inches(0.5),
             size=Pt(15), color=GRAY, italic=True, align=PP_ALIGN.CENTER)

    page_number(slide, 5)
    set_notes(slide, "Person A liest beide Aufgaben vor und gibt ca. 2 Minuten Zeit zum Nachdenken/Diskutieren "
              "in kleinen Gruppen. Tipp falls jemand nicht weiterkommt: Aufgabe 1 hat 3 unabhängige "
              "Schritte (Zählprinzip aus Folie 3), Aufgabe 2 verteilt ALLE 6 Personen auf ALLE Plätze "
              "(Permutation aus Folie 4). Überleitung zu Person B für die Lösung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 6 - Lösung (Teil 1)
# ---------------------------------------------------------------------------

def slide_06_loesung1(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Lösung - Teil 1", person="B", kicker="Zählprinzip & Permutation")

    panel_h = Inches(5.3)
    add_panel(slide, CONTENT_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "1", CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=DEEP_BLUE)
    add_label_chip(slide, "ZÄHLPRINZIP", CONTENT_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=DEEP_BLUE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "3 Größen × 5 Saucen × 2 Käsesorten:\n3 unabhängige Schritte → multiplizieren.",
             CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(1.4), size=Pt(17))
    add_formula(slide, "f_aufgabe1_loesung", box_left=CONTENT_LEFT, box_top=CONTENT_TOP + Inches(2.8),
                 box_width=COL_W, box_height=Inches(1.0))
    add_text(slide, "→ 30 verschiedene Pizzen", CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(4.0),
             COL_W - Inches(0.6), Inches(0.6), size=Pt(16), color=DEEP_BLUE, bold=True, align=PP_ALIGN.CENTER)

    add_panel(slide, COL2_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "2", COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=ORANGE)
    add_label_chip(slide, "PERMUTATION", COL2_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=ORANGE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "Alle 6 Personen besetzen alle 6 Plätze:\nPermutation ohne Wiederholung → 6!.",
             COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(1.4), size=Pt(17))
    add_formula(slide, "f_aufgabe1b_loesung", box_left=COL2_LEFT, box_top=CONTENT_TOP + Inches(2.8),
                 box_width=COL_W, box_height=Inches(1.0))
    add_text(slide, "→ 720 mögliche Aufstellungen", COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(4.0),
             COL_W - Inches(0.6), Inches(0.6), size=Pt(16), color=DEEP_BLUE, bold=True, align=PP_ALIGN.CENTER)

    page_number(slide, 6)
    set_notes(slide, "Person B löst beide Aufgaben gemeinsam mit dem Publikum auf. "
              "Aufgabe 1: 3*5*2=30 (Zählprinzip, drei unabhängige Schritte). "
              "Aufgabe 2: 6!=720 (Permutation, alle Personen werden angeordnet). "
              "Überleitung zu Person C: 'Was ist, wenn nicht ALLE Plätze besetzt werden, sondern "
              "nur ein Teil - z. B. nur die ersten drei beim Sportwettkampf?'")
    return slide


# ---------------------------------------------------------------------------
# Slide 7 - Variation (ohne & mit Wiederholung)
# ---------------------------------------------------------------------------

def slide_07_variation(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Variation", person="C", kicker="Stockerlplatz & PIN-Code")

    # Band 1: ohne Wiederholung - Stockerlplatz
    add_label_chip(slide, "OHNE WIEDERHOLUNG", CONTENT_LEFT, CONTENT_TOP, fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_variation_ohne", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(0.6), height=Inches(0.55))
    add_text(slide, "Reihenfolge wichtig, ohne Zurücklegen: Es werden nur k von n Elementen "
             "ausgewählt UND angeordnet.",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.35), COL_W, Inches(1.0), size=Pt(14))
    add_formula(slide, "f_beispiel_stockerl", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(2.25), height=Inches(0.5))

    add_picture_fit(slide, "podium.png", COL2_LEFT + Inches(0.6), CONTENT_TOP - Inches(0.05), COL_W - Inches(1.2), Inches(2.0))
    add_text(slide, "8 Läufer:innen, Plätze 1-3 (Stockerl) → V(8,3) = 8·7·6 = 336",
             COL2_LEFT, CONTENT_TOP + ROW_H - Inches(0.55), COL_W, Inches(0.55),
             size=Pt(13), color=GRAY, align=PP_ALIGN.CENTER)

    # Band 2: mit Wiederholung - PIN-Code
    add_label_chip(slide, "MIT WIEDERHOLUNG", CONTENT_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_variation_mit", left=CONTENT_LEFT, top=ROW2_TOP + Inches(0.6), height=Inches(0.55))
    add_text(slide, "Reihenfolge wichtig, MIT Zurücklegen: jedes der k Elemente kann erneut "
             "aus allen n Möglichkeiten gewählt werden.",
             CONTENT_LEFT, ROW2_TOP + Inches(1.35), COL_W, Inches(1.4), size=Pt(14))

    add_label_chip(slide, "AUFLÖSUNG: PIN-CODE", COL2_LEFT, ROW2_TOP, fill=MID_BLUE,
                    width=Inches(3.1), height=Inches(0.45), size=Pt(13))
    pin_w = Inches(0.9)
    pin_gap = Inches(0.28)
    pin_total = pin_w * 4 + pin_gap * 3
    pin_left = COL2_LEFT + (COL_W - pin_total) // 2
    for i in range(4):
        x = pin_left + i * (pin_w + pin_gap)
        add_rect(slide, x, ROW2_TOP + Inches(0.65), pin_w, pin_w, fill=LIGHT_BLUE, line=DEEP_BLUE,
                 line_width=Pt(1.5), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        add_text(slide, "?", x, ROW2_TOP + Inches(0.65), pin_w, pin_w, size=Pt(36), color=DEEP_BLUE,
                 bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, "4-stelliger PIN, Ziffern 0-9, Wiederholung erlaubt:",
             COL2_LEFT, ROW2_TOP + Inches(1.75), COL_W, Inches(0.45), size=Pt(13), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_pin", box_left=COL2_LEFT, box_top=ROW2_TOP + Inches(2.15),
                 box_width=COL_W, box_height=Inches(0.65))

    page_number(slide, 7)
    set_notes(slide, "Person C erklärt die Variation ohne Wiederholung am Stockerlplatz: 8 Läufer, aber "
              "nur 3 Plätze, Reihenfolge zählt -> V(8,3)=8!/5!=336. Danach Variation MIT Wiederholung "
              "und die Auflösung der Einstiegsfrage von Folie 2: PIN mit 4 Ziffern aus 10 möglichen "
              "(0-9), Wiederholung erlaubt -> 10^4 = 10.000 PINs! Überleitung zu Person A: "
              "'Jetzt kommt der dritte Fall: Was, wenn die Reihenfolge gar nicht wichtig ist?'")
    return slide


# ---------------------------------------------------------------------------
# Slide 8 - Kombination (ohne & mit Wiederholung)
# ---------------------------------------------------------------------------

def slide_08_kombination(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Kombination", person="A", kicker="Lotto & Eisbecher")

    # Band 1: ohne Wiederholung - Lotto
    add_label_chip(slide, "OHNE WIEDERHOLUNG", CONTENT_LEFT, CONTENT_TOP, fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_kombination_ohne", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(0.6), height=Inches(0.6))
    add_text(slide, "Reihenfolge EGAL, ohne Zurücklegen: Auswahl von k aus n Elementen, "
             "jede Auswahl zählt nur einmal.",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.4), COL_W, Inches(1.3), size=Pt(14))

    add_label_chip(slide, "BEISPIEL: LOTTO 6 AUS 45", COL2_LEFT, CONTENT_TOP, fill=MID_BLUE,
                    width=Inches(3.3), height=Inches(0.45), size=Pt(13))
    add_picture_fit(slide, "lotto_balls.png", COL2_LEFT, CONTENT_TOP + Inches(0.6), COL_W, Inches(1.0))
    add_formula(slide, "f_lotto_komb", box_left=COL2_LEFT, box_top=CONTENT_TOP + Inches(1.75),
                 box_width=COL_W, box_height=Inches(0.85))

    # Band 2: mit Wiederholung - Eisbecher
    add_label_chip(slide, "MIT WIEDERHOLUNG", CONTENT_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_kombination_mit", left=CONTENT_LEFT, top=ROW2_TOP + Inches(0.6), height=Inches(0.6))
    add_text(slide, "Reihenfolge egal, MIT Zurücklegen: Auswahl von k aus n Sorten, "
             "Wiederholung erlaubt.",
             CONTENT_LEFT, ROW2_TOP + Inches(1.4), COL_W, Inches(1.3), size=Pt(14))

    add_label_chip(slide, "BEISPIEL: EISBECHER", COL2_LEFT, ROW2_TOP, fill=MID_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_picture_fit(slide, "icecream.png", COL2_LEFT + Inches(1.6), ROW2_TOP + Inches(0.5), Inches(2.6), Inches(1.7))
    add_text(slide, "3 Kugeln aus 5 Sorten, Wiederholung erlaubt:",
             COL2_LEFT, ROW2_TOP + Inches(2.15), COL_W, Inches(0.4), size=Pt(13), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_eis", box_left=COL2_LEFT, box_top=ROW2_TOP + Inches(2.45),
                 box_width=COL_W, box_height=Inches(0.45))

    page_number(slide, 8)
    set_notes(slide, "Person A erklärt Kombination ohne Wiederholung am Lotto-Beispiel 6 aus 45: "
              "Reihenfolge der gezogenen Zahlen ist egal -> binom(45,6)=8.145.060 Möglichkeiten "
              "(Zahl wirkt riesig, wird auf Folie 14 für die Wahrscheinlichkeit gebraucht). "
              "Danach Kombination MIT Wiederholung am Eisbecher: 3 Kugeln aus 5 Sorten, man kann "
              "auch zweimal dieselbe Sorte nehmen -> binom(7,3)=35. Überleitung zu Person B: "
              "'Diese binom-Symbole erinnert euch vielleicht an etwas - das Pascal'sche Dreieck!'")
    return slide


# ---------------------------------------------------------------------------
# Slide 9 - Pascal'sches Dreieck <-> Binomialkoeffizient
# ---------------------------------------------------------------------------

def slide_09_pascal(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Pascal'sches Dreieck", person="B", kicker="Verbindung zum Binomialkoeffizienten")

    add_picture_fit(slide, "pascal_triangle.png", CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(4.0))

    panel_top = Inches(5.5)
    panel_h = Inches(1.7)
    add_panel(slide, CONTENT_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "REKURSIONSFORMEL", CONTENT_LEFT + Inches(0.3), panel_top + Inches(0.2), fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.4), size=Pt(12))
    add_formula(slide, "f_pascal_link", box_left=CONTENT_LEFT, box_top=panel_top + Inches(0.65),
                 box_width=COL_W, box_height=Inches(0.95))

    add_panel(slide, COL2_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "BEISPIEL", COL2_LEFT + Inches(0.3), panel_top + Inches(0.2), fill=ORANGE,
                    width=Inches(1.7), height=Inches(0.4), size=Pt(12))
    add_formula(slide, "f_beispiel_pascal_62", left=COL2_LEFT + Inches(0.4), top=panel_top + Inches(0.65),
                 height=Inches(0.7))
    add_text(slide, "Die orange Zahl im Dreieck zeigt genau diesen Wert -\ngenau wie bei \"6 aus 45\" beim Lotto.",
             COL2_LEFT + Inches(2.4), panel_top + Inches(0.65), COL_W - Inches(2.7), Inches(0.95), size=Pt(13))

    page_number(slide, 9)
    set_notes(slide, "Person B zeigt das Pascal'sche Dreieck: jede Zahl ist die Summe der beiden Zahlen "
              "darüber - das ist genau die Rekursionsformel binom(n,k)=binom(n-1,k-1)+binom(n-1,k). "
              "Die orange markierte 15 in Zeile 6 entspricht binom(6,2)=15 - dem Binomialkoeffizienten "
              "aus der Kombination (Folie 8). Das Dreieck ist also eine praktische Tabelle für alle "
              "Binomialkoeffizienten. Überleitung zu Person C für die zweite Übungsaufgabe.")
    return slide


# ---------------------------------------------------------------------------
# Slide 10 - Aufgabe für euch (Teil 2)
# ---------------------------------------------------------------------------

def slide_10_aufgabe2(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Aufgabe für euch - Teil 2", person="C", kicker="Variation & Kombination")

    panel_h = Inches(5.3)
    add_panel(slide, CONTENT_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "1", CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=DEEP_BLUE)
    add_label_chip(slide, "VARIATION", CONTENT_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=DEEP_BLUE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "Bei einem Wettbewerb treten 10 Teilnehmer:innen an.\n\n"
             "Wie viele Möglichkeiten gibt es für die Vergabe von Platz 1, 2 und 3?",
             CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(2.6), size=Pt(18))

    add_panel(slide, COL2_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "2", COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=ORANGE)
    add_label_chip(slide, "KOMBINATION", COL2_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=ORANGE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "Aus 7 Bewerber:innen werden 3 Personen für ein Projektteam ausgewählt "
             "(Reihenfolge egal).\n\n"
             "Wie viele verschiedene Teams sind möglich?",
             COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(2.6), size=Pt(18))

    add_text(slide, "Überlegt in Zweier- oder Dreiergruppen - ca. 2 Minuten Zeit!",
             CONTENT_LEFT, CONTENT_TOP + panel_h + Inches(0.15), CONTENT_W, Inches(0.5),
             size=Pt(15), color=GRAY, italic=True, align=PP_ALIGN.CENTER)

    page_number(slide, 10)
    set_notes(slide, "Person C liest beide Aufgaben vor, ca. 2 Minuten Zeit zum Nachdenken. "
              "Tipp: Aufgabe 1 - die Reihenfolge (Platz 1/2/3) ist wichtig -> Variation ohne "
              "Wiederholung, V(10,3). Aufgabe 2 - die Reihenfolge im Team ist egal -> Kombination "
              "ohne Wiederholung, binom(7,3). Überleitung zu Person A für die Lösung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 11 - Lösung (Teil 2)
# ---------------------------------------------------------------------------

def slide_11_loesung2(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Lösung - Teil 2", person="A", kicker="Variation & Kombination")

    panel_h = Inches(5.3)
    add_panel(slide, CONTENT_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "1", CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=DEEP_BLUE)
    add_label_chip(slide, "VARIATION", CONTENT_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=DEEP_BLUE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "Reihenfolge wichtig (Platz 1, 2, 3), nur 3 von 10\nwerden ausgewählt → Variation ohne Wiederholung.",
             CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(1.4), size=Pt(16))
    add_formula(slide, "f_aufgabe2_loesung", box_left=CONTENT_LEFT, box_top=CONTENT_TOP + Inches(2.8),
                 box_width=COL_W, box_height=Inches(1.0))
    add_text(slide, "→ 720 mögliche Stockerlplätze", CONTENT_LEFT + Inches(0.3), CONTENT_TOP + Inches(4.0),
             COL_W - Inches(0.6), Inches(0.6), size=Pt(16), color=DEEP_BLUE, bold=True, align=PP_ALIGN.CENTER)

    add_panel(slide, COL2_LEFT, CONTENT_TOP, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_circle_badge(slide, "2", COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(0.3), Inches(0.6), fill=ORANGE)
    add_label_chip(slide, "KOMBINATION", COL2_LEFT + Inches(1.1), CONTENT_TOP + Inches(0.35), fill=ORANGE,
                    width=Inches(2.4), height=Inches(0.5))
    add_text(slide, "Reihenfolge im Team egal, 3 von 7 werden\nausgewählt → Kombination ohne Wiederholung.",
             COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(1.2), COL_W - Inches(0.6), Inches(1.4), size=Pt(16))
    add_formula(slide, "f_aufgabe2b_loesung", box_left=COL2_LEFT, box_top=CONTENT_TOP + Inches(2.8),
                 box_width=COL_W, box_height=Inches(1.0))
    add_text(slide, "→ 35 mögliche Teams", COL2_LEFT + Inches(0.3), CONTENT_TOP + Inches(4.0),
             COL_W - Inches(0.6), Inches(0.6), size=Pt(16), color=DEEP_BLUE, bold=True, align=PP_ALIGN.CENTER)

    page_number(slide, 11)
    set_notes(slide, "Person A löst beide Aufgaben auf: V(10,3)=10!/7!=10*9*8=720 (Reihenfolge zählt). "
              "binom(7,3)=35 (Reihenfolge egal, Team-Zusammensetzung). Kurzer Vergleich: bei gleicher "
              "Auswahl ist die Variation immer GRÖSSER als die Kombination, weil sie zusätzlich die "
              "Reihenfolge mitzählt. Überleitung zu Person B: 'Jetzt verbinden wir das Zählen mit "
              "Wahrscheinlichkeiten.'")
    return slide


# ---------------------------------------------------------------------------
# Slide 12 - Laplace-Wahrscheinlichkeit
# ---------------------------------------------------------------------------

def slide_12_laplace(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Die Laplace-Wahrscheinlichkeit", person="B", kicker="Von Zählen zu Chancen")

    add_formula(slide, "f_laplace", box_left=CONTENT_LEFT, box_top=CONTENT_TOP,
                 box_width=CONTENT_W, box_height=Inches(1.5))

    panel_top = Inches(3.1)
    panel_h = Inches(2.1)
    add_panel(slide, CONTENT_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|A|  -  GÜNSTIGE FÄLLE", CONTENT_LEFT + Inches(0.3), panel_top + Inches(0.25),
                    fill=ORANGE, width=Inches(3.2), height=Inches(0.45), size=Pt(13))
    add_text(slide, "Anzahl der Ergebnisse, die das gewünschte Ereignis A erfüllen.",
             CONTENT_LEFT + Inches(0.3), panel_top + Inches(0.9), COL_W - Inches(0.6), Inches(1.1), size=Pt(15))

    add_panel(slide, COL2_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|Ω|  -  MÖGLICHE FÄLLE", COL2_LEFT + Inches(0.3), panel_top + Inches(0.25),
                    fill=DEEP_BLUE, width=Inches(3.2), height=Inches(0.45), size=Pt(13))
    add_text(slide, "Anzahl ALLER möglichen Ergebnisse - der gesamte Ergebnisraum Ω.",
             COL2_LEFT + Inches(0.3), panel_top + Inches(0.9), COL_W - Inches(0.6), Inches(1.1), size=Pt(15))

    add_panel(slide, CONTENT_LEFT, Inches(5.45), CONTENT_W, Inches(1.45), fill=YELLOW, line=ORANGE)
    add_text(slide, "Voraussetzung: Alle Ergebnisse müssen gleich wahrscheinlich sein "
             "(\"Laplace-Experiment\") - z. B. ein fairer Würfel oder eine faire Münze.",
             CONTENT_LEFT + Inches(0.4), Inches(5.45), CONTENT_W - Inches(0.8), Inches(1.45),
             size=Pt(17), bold=True, color=DEEP_BLUE, anchor=MSO_ANCHOR.MIDDLE)

    page_number(slide, 12)
    set_notes(slide, "Person B führt die Laplace-Wahrscheinlichkeit ein: P(A) = |A|/|Omega|. "
              "Wichtig: |Omega| und |A| werden oft genau mit den Formeln aus den letzten Folien "
              "(Zählprinzip, Permutation, Variation, Kombination) berechnet - Kombinatorik und "
              "Wahrscheinlichkeit hängen also direkt zusammen! Die Voraussetzung betonen: "
              "Laplace funktioniert NUR, wenn alle Ergebnisse gleich wahrscheinlich sind. "
              "Überleitung zu Person C für das Würfel-Beispiel.")
    return slide


# ---------------------------------------------------------------------------
# Slide 13 - Beispiel: Würfeln (Pasch)
# ---------------------------------------------------------------------------

def slide_13_wuerfeln(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Beispiel: Würfeln (Pasch)", person="C", kicker="Zwei Würfel, gleiche Augenzahl?")

    add_text(slide, "Zwei faire Würfel werden gleichzeitig geworfen.\n\n"
             "Wie groß ist die Wahrscheinlichkeit für einen Pasch "
             "(beide Würfel zeigen dieselbe Zahl)?",
             CONTENT_LEFT, CONTENT_TOP, COL_W, Inches(1.6), size=Pt(18))

    add_panel(slide, CONTENT_LEFT, Inches(2.95), COL_W, Inches(1.3), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|Ω| - MÖGLICHE FÄLLE", CONTENT_LEFT + Inches(0.3), Inches(3.15), fill=DEEP_BLUE,
                    width=Inches(2.9), height=Inches(0.45), size=Pt(13))
    add_text(slide, "6 · 6 = 36  (jeder Würfel hat 6 Augenzahlen → Zählprinzip)",
             CONTENT_LEFT + Inches(0.3), Inches(3.7), COL_W - Inches(0.6), Inches(0.5), size=Pt(14))

    add_panel(slide, CONTENT_LEFT, Inches(4.4), COL_W, Inches(1.3), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|A| - GÜNSTIGE FÄLLE", CONTENT_LEFT + Inches(0.3), Inches(4.6), fill=ORANGE,
                    width=Inches(2.9), height=Inches(0.45), size=Pt(13))
    add_text(slide, "6 Paschs: (1,1), (2,2), ..., (6,6) - die orange Diagonale",
             CONTENT_LEFT + Inches(0.3), Inches(5.15), COL_W - Inches(0.6), Inches(0.5), size=Pt(14))

    add_formula(slide, "f_pasch", box_left=CONTENT_LEFT, box_top=Inches(5.85),
                 box_width=COL_W, box_height=Inches(1.05))

    add_picture_fit(slide, "dice_grid.png", COL2_LEFT, CONTENT_TOP, COL_W, Inches(5.85))

    page_number(slide, 13)
    set_notes(slide, "Person C zeigt das 6x6-Raster aller Würfelergebnisse: |Omega|=36 nach dem "
              "Zählprinzip (Folie 3). Die orange Diagonale sind die 6 Paschs -> |A|=6. "
              "Mit der Laplace-Formel von Folie 12: P(Pasch)=6/36=1/6 ≈ 16,7%. "
              "Überleitung zu Person A: 'Jetzt kombinieren wir Laplace mit der riesigen Zahl "
              "vom Lotto-Beispiel.'")
    return slide


# ---------------------------------------------------------------------------
# Slide 14 - Lotto 6 aus 45: Wahrscheinlichkeit für 6 Richtige
# ---------------------------------------------------------------------------

def slide_14_lotto_wahrscheinlichkeit(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Lotto 6 aus 45", person="A", kicker="Wie groß ist die Chance auf 6 Richtige?")

    add_picture_fit(slide, "lotto_balls.png", CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(1.3))

    panel_top = Inches(2.85)
    panel_h = Inches(1.5)
    add_panel(slide, CONTENT_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|Ω| - MÖGLICHE FÄLLE", CONTENT_LEFT + Inches(0.3), panel_top + Inches(0.2), fill=DEEP_BLUE,
                    width=Inches(2.9), height=Inches(0.45), size=Pt(13))
    add_text(slide, "binom(45,6) = 8.145.060\nalle möglichen Lotto-Tipps (siehe Folie 8)",
             CONTENT_LEFT + Inches(0.3), panel_top + Inches(0.75), COL_W - Inches(0.6), Inches(0.7), size=Pt(14))

    add_panel(slide, COL2_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|A| - GÜNSTIGE FÄLLE", COL2_LEFT + Inches(0.3), panel_top + Inches(0.2), fill=ORANGE,
                    width=Inches(2.9), height=Inches(0.45), size=Pt(13))
    add_text(slide, "1\ngenau der eine gezogene Tipp",
             COL2_LEFT + Inches(0.3), panel_top + Inches(0.75), COL_W - Inches(0.6), Inches(0.7), size=Pt(14))

    add_formula(slide, "f_lotto_prob", box_left=CONTENT_LEFT, box_top=Inches(4.55),
                 box_width=CONTENT_W, box_height=Inches(1.1))

    add_panel(slide, CONTENT_LEFT, Inches(5.85), CONTENT_W, Inches(1.2), fill=YELLOW, line=ORANGE)
    add_text(slide, "Zum Vergleich: Das ist ungefähr so wahrscheinlich, wie unter allen "
             "Einwohner:innen Österreichs (ca. 9 Millionen) zufällig genau eine bestimmte "
             "Person auszuwählen.",
             CONTENT_LEFT + Inches(0.4), Inches(5.85), CONTENT_W - Inches(0.8), Inches(1.2),
             size=Pt(15), bold=True, color=DEEP_BLUE, anchor=MSO_ANCHOR.MIDDLE)

    page_number(slide, 14)
    set_notes(slide, "Person A verbindet die Kombination (Folie 8) mit Laplace: |Omega|=binom(45,6)=8.145.060, "
              "|A|=1 (genau der gezogene Tipp). P(6 Richtige)=1/8.145.060≈0,0000123%. "
              "Den Vergleich mit der österreichischen Bevölkerung nutzen, um die Größenordnung "
              "greifbar zu machen. Überleitung zu Person B für die dritte Übungsaufgabe (Urne).")
    return slide


# ---------------------------------------------------------------------------
# Slide 15 - Aufgabe für euch (Teil 3)
# ---------------------------------------------------------------------------

def slide_15_aufgabe3(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Aufgabe für euch - Teil 3", person="B", kicker="Laplace-Wahrscheinlichkeit")

    add_picture_fit(slide, "urn.png", CONTENT_LEFT, CONTENT_TOP, Inches(5.0), Inches(5.55))

    panel_left = Inches(5.85)
    panel_w = SLIDE_W - panel_left - MARGIN
    add_panel(slide, panel_left, CONTENT_TOP, panel_w, Inches(5.55), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "AUFGABE", panel_left + Inches(0.35), CONTENT_TOP + Inches(0.35), fill=MID_BLUE,
                    width=Inches(2.0), height=Inches(0.5))
    add_text(slide, "Eine Urne enthält 4 rote und 6 blaue Kugeln (insgesamt 10).\n\n"
             "Es werden gleichzeitig 2 Kugeln gezogen (ohne Zurücklegen, "
             "Reihenfolge egal).\n\n"
             "Wie groß ist die Wahrscheinlichkeit, dass BEIDE Kugeln rot sind?",
             panel_left + Inches(0.35), CONTENT_TOP + Inches(1.1), panel_w - Inches(0.7), Inches(3.1), size=Pt(18))
    add_text(slide, "Tipp: Überlegt euch |Ω| (alle möglichen 2er-Ziehungen aus 10) "
             "und |A| (beide Kugeln rot, aus den 4 roten).",
             panel_left + Inches(0.35), CONTENT_TOP + Inches(4.3), panel_w - Inches(0.7), Inches(1.0),
             size=Pt(14), italic=True, color=GRAY)

    add_text(slide, "Überlegt in Zweier- oder Dreiergruppen - ca. 2 Minuten Zeit!",
             CONTENT_LEFT, CONTENT_TOP + Inches(5.65), CONTENT_W, Inches(0.4),
             size=Pt(15), color=GRAY, italic=True, align=PP_ALIGN.CENTER)

    page_number(slide, 15)
    set_notes(slide, "Person B liest die Aufgabe vor und gibt ca. 2 Minuten Zeit. Tipp falls nötig: "
              "Reihenfolge spielt keine Rolle (gleichzeitiges Ziehen) -> Kombination ohne "
              "Wiederholung für |Omega| und |A|. |Omega|=binom(10,2), |A|=binom(4,2). "
              "Überleitung zu Person C für die Lösung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 16 - Lösung (Teil 3)
# ---------------------------------------------------------------------------

def slide_16_loesung3(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Lösung - Teil 3", person="C", kicker="Laplace-Wahrscheinlichkeit")

    add_picture_fit(slide, "urn.png", CONTENT_LEFT, CONTENT_TOP, Inches(5.0), Inches(5.85))

    panel_left = Inches(5.85)
    panel_w = SLIDE_W - panel_left - MARGIN

    add_panel(slide, panel_left, CONTENT_TOP, panel_w, Inches(1.4), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|A| - BEIDE ROT", panel_left + Inches(0.3), CONTENT_TOP + Inches(0.2), fill=ORANGE,
                    width=Inches(2.4), height=Inches(0.45), size=Pt(13))
    add_text(slide, "binom(4,2) = 6\n2 von 4 roten Kugeln auswählen",
             panel_left + Inches(0.3), CONTENT_TOP + Inches(0.75), panel_w - Inches(0.6), Inches(0.6), size=Pt(14))

    add_panel(slide, panel_left, CONTENT_TOP + Inches(1.55), panel_w, Inches(1.4), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|Ω| - ALLE ZIEHUNGEN", panel_left + Inches(0.3), CONTENT_TOP + Inches(1.75), fill=DEEP_BLUE,
                    width=Inches(2.6), height=Inches(0.45), size=Pt(13))
    add_text(slide, "binom(10,2) = 45\n2 beliebige Kugeln von 10 auswählen",
             panel_left + Inches(0.3), CONTENT_TOP + Inches(2.3), panel_w - Inches(0.6), Inches(0.6), size=Pt(14))

    add_formula(slide, "f_aufgabe3_loesung", box_left=panel_left, box_top=CONTENT_TOP + Inches(3.15),
                 box_width=panel_w, box_height=Inches(1.3))
    add_text(slide, "→ ca. 13,3 % Wahrscheinlichkeit für \"beide rot\"",
             panel_left, CONTENT_TOP + Inches(4.6), panel_w, Inches(0.6),
             size=Pt(16), color=DEEP_BLUE, bold=True, align=PP_ALIGN.CENTER)

    page_number(slide, 16)
    set_notes(slide, "Person C löst die Aufgabe: |A|=binom(4,2)=6 (beide rot), |Omega|=binom(10,2)=45 "
              "(alle 2er-Ziehungen aus 10). P(beide rot)=6/45=2/15≈13,3%. "
              "Überleitung zu Person A für das Quiz: 'Jetzt seid ihr dran - testen wir, ob alles "
              "hängen geblieben ist!'")
    return slide


# ---------------------------------------------------------------------------
# Slide 17 - Quiz für alle (Publikum)
# ---------------------------------------------------------------------------

def slide_17_quiz(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Quiz für alle", person="A", kicker="Welches Konzept passt?")

    questions = [
        ("1", "Du stellst 4 verschiedene Bücher in einer Reihe ins Regal.\nWie viele Anordnungen sind möglich?"),
        ("2", "Bei einem Pferderennen mit 6 Pferden werden die Plätze 1, 2 und 3 vergeben.\nWie viele Möglichkeiten gibt es?"),
        ("3", "Du ziehst gleichzeitig 3 Karten aus einem 32er-Kartenspiel (Reihenfolge egal).\nWie viele Möglichkeiten gibt es?"),
    ]
    panel_h = Inches(1.85)
    gap = Inches(0.1)
    for i, (num, q) in enumerate(questions):
        top = CONTENT_TOP + i * (panel_h + gap)
        add_panel(slide, CONTENT_LEFT, top, CONTENT_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
        add_circle_badge(slide, num, CONTENT_LEFT + Inches(0.3), top + Inches(0.6), Inches(0.65), fill=DEEP_BLUE)
        add_text(slide, q, CONTENT_LEFT + Inches(1.25), top, Inches(7.55), panel_h,
                 size=Pt(17), anchor=MSO_ANCHOR.MIDDLE)
        add_text(slide, "A) Zählprinzip\nB) Permutation\nC) Variation\nD) Kombination",
                 Inches(9.0), top, Inches(3.6), panel_h, size=Pt(14), color=DEEP_BLUE, bold=True,
                 anchor=MSO_ANCHOR.MIDDLE)

    page_number(slide, 17)
    set_notes(slide, "Person A liest die 3 Fragen vor. Das Publikum (14 Personen) ruft/zeigt jeweils "
              "A, B, C oder D als Antwort - kein Zwang zu schriftlichen Antworten, einfach laut "
              "abstimmen lassen. Nach jeder Frage kurz die Mehrheitsmeinung abfragen, bevor es zur "
              "Auflösung geht. Überleitung zu Person B für die Lösung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 18 - Lösung Quiz
# ---------------------------------------------------------------------------

def slide_18_loesung_quiz(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Lösung Quiz", person="B", kicker="Auflösung")

    answers = [
        ("1", "B) Permutation", DEEP_BLUE, "4! = 24",
         "Alle 4 Bücher werden angeordnet - Reihenfolge wichtig, alle Elemente werden verwendet."),
        ("2", "C) Variation (ohne Wdh.)", ORANGE, "V(6,3) = 120",
         "Reihenfolge wichtig (Platz 1/2/3), aber nur 3 von 6 Pferden werden platziert."),
        ("3", "D) Kombination (ohne Wdh.)", MID_BLUE, "C(32,3) = 4.960",
         "Reihenfolge egal - Auswahl von 3 Karten aus 32."),
    ]
    panel_h = Inches(1.85)
    gap = Inches(0.1)
    for i, (num, name, color, value, expl) in enumerate(answers):
        top = CONTENT_TOP + i * (panel_h + gap)
        add_panel(slide, CONTENT_LEFT, top, CONTENT_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
        add_circle_badge(slide, num, CONTENT_LEFT + Inches(0.3), top + Inches(0.6), Inches(0.65), fill=color)
        add_label_chip(slide, name, CONTENT_LEFT + Inches(1.25), top + Inches(0.25), fill=color,
                        width=Inches(3.7), height=Inches(0.5), size=Pt(14))
        add_text(slide, expl, CONTENT_LEFT + Inches(1.25), top + Inches(0.95), Inches(6.5), Inches(0.85), size=Pt(13))
        add_text(slide, value, Inches(9.0), top, Inches(3.6), panel_h, size=Pt(22), bold=True,
                 color=DEEP_BLUE, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)

    page_number(slide, 18)
    set_notes(slide, "Person B löst alle 3 Fragen auf und erklärt jeweils kurz, woran man das "
              "richtige Konzept erkennt: Frage 1 - alle Elemente, Reihenfolge wichtig -> Permutation. "
              "Frage 2 - nur ein Teil, Reihenfolge wichtig -> Variation. Frage 3 - nur ein Teil, "
              "Reihenfolge egal -> Kombination. Überleitung zu Person C für die Übersichtstabelle.")
    return slide


# ---------------------------------------------------------------------------
# Slide 19 - Übersichtstabelle: Wann verwende ich was?
# ---------------------------------------------------------------------------

def _set_cell(cell, text, bold=False, color=DARK, size=Pt(14), fill=WHITE, align=PP_ALIGN.LEFT):
    cell.text = text
    cell.margin_left = Inches(0.12)
    cell.margin_right = Inches(0.12)
    cell.margin_top = Inches(0.04)
    cell.margin_bottom = Inches(0.04)
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    cell.fill.solid()
    cell.fill.fore_color.rgb = fill
    p = cell.text_frame.paragraphs[0]
    p.alignment = align
    for run in p.runs:
        run.font.size = size
        run.font.bold = bold
        run.font.color.rgb = color
        run.font.name = FONT_BODY


def slide_19_uebersicht(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Übersichtstabelle", person="C", kicker="Wann verwende ich was?")

    rows, cols = 6, 4
    col_widths = [Inches(3.6), Inches(2.35), Inches(2.35), Inches(4.033)]
    table_h = Inches(5.35)
    table_shape = slide.shapes.add_table(rows, cols, CONTENT_LEFT, CONTENT_TOP, CONTENT_W, table_h)
    table = table_shape.table
    for i, w in enumerate(col_widths):
        table.columns[i].width = w
    table.rows[0].height = Inches(0.7)
    for r in range(1, rows):
        table.rows[r].height = Inches(0.93)

    headers = ["Konzept", "Reihenfolge wichtig?", "Wiederholung erlaubt?", "Formel"]
    for c, h in enumerate(headers):
        _set_cell(table.cell(0, c), h, bold=True, color=WHITE, size=Pt(15), fill=DEEP_BLUE, align=PP_ALIGN.CENTER)

    data = [
        ("Permutation", "Ja (alle n Elemente)", "ohne: nein  /  mit: ja",
         "P(n) = n!   bzw.   n! / (k₁!·k₂!·...)"),
        ("Variation - ohne Wiederholung", "Ja", "Nein", "V(n,k) = n! / (n−k)!"),
        ("Variation - mit Wiederholung", "Ja", "Ja", "V_W(n,k) = nᵏ"),
        ("Kombination - ohne Wiederholung", "Nein", "Nein", "C(n,k) = (n über k)"),
        ("Kombination - mit Wiederholung", "Nein", "Ja", "C_W(n,k) = (n+k−1 über k)"),
    ]
    for r, row_data in enumerate(data, start=1):
        fill = LIGHT_BLUE if r % 2 == 1 else WHITE
        for c, val in enumerate(row_data):
            bold = (c == 0)
            align = PP_ALIGN.LEFT if c in (0, 3) else PP_ALIGN.CENTER
            _set_cell(table.cell(r, c), val, bold=bold, color=DEEP_BLUE if c == 0 else DARK,
                      size=Pt(14), fill=fill, align=align)

    add_text(slide, "Tipp: Bei der Permutation gilt immer k = n - alle Elemente werden verwendet.",
             CONTENT_LEFT, Inches(6.85), CONTENT_W, Inches(0.4), size=Pt(13), color=GRAY, italic=True,
             align=PP_ALIGN.CENTER)

    page_number(slide, 19)
    set_notes(slide, "Person C fasst alle 5 Konzepte in einer Tabelle zusammen - das ist die "
              "Eselsbrücke für die Matura: Zuerst fragen 'Ist die Reihenfolge wichtig?', dann "
              "'Wird wiederholt / mit Zurücklegen gewählt?'. Diese zwei Ja/Nein-Fragen führen "
              "direkt zur richtigen Formel. Überleitung zu allen drei für die Zusammenfassung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 20 - Zusammenfassung
# ---------------------------------------------------------------------------

def slide_20_zusammenfassung(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Zusammenfassung", person="Alle", kicker="Die wichtigsten Takeaways")

    takeaways = [
        ("A", DEEP_BLUE, "Das Zählprinzip ist die Basis für alles: Bei mehreren unabhängigen "
         "Schritten einfach die Anzahl der Möglichkeiten pro Schritt multiplizieren."),
        ("B", ORANGE, "Zwei Fragen führen zur richtigen Formel: Ist die Reihenfolge wichtig? "
         "Wird mit Wiederholung gewählt? → Permutation, Variation oder Kombination."),
        ("C", MID_BLUE, "Mit Laplace P(A) = |A| / |Ω| werden aus Kombinatorik-Formeln konkrete "
         "Wahrscheinlichkeiten - z. B. warum ein Lotto-Sechser so unwahrscheinlich ist."),
    ]
    col_w = Inches(3.95)
    gap = Inches(0.24)
    badge_d = Inches(1.0)
    for i, (letter, color, text) in enumerate(takeaways):
        left = CONTENT_LEFT + i * (col_w + gap)
        add_panel(slide, left, CONTENT_TOP, col_w, Inches(5.6), fill=LIGHT_BLUE, line=color)
        add_circle_badge(slide, letter, left + (col_w - badge_d) // 2, CONTENT_TOP + Inches(0.4),
                          badge_d, fill=color, size=Pt(36))
        add_text(slide, text, left + Inches(0.35), CONTENT_TOP + Inches(1.75), col_w - Inches(0.7),
                 Inches(3.5), size=Pt(17), align=PP_ALIGN.CENTER)

    page_number(slide, 20)
    set_notes(slide, "Jede Person spricht ihren eigenen Takeaway in 1-2 Sätzen, in der Reihenfolge "
              "A -> B -> C. Diese drei Sätze sollen das gesamte Thema in Kürze zusammenfassen "
              "und sind die 'Kernbotschaften', die das Publikum mitnehmen soll. Überleitung zu "
              "Folie 'Quellen' (kurz) und dann zum Abschluss.")
    return slide


# ---------------------------------------------------------------------------
# Slide 21 - Quellen
# ---------------------------------------------------------------------------

def slide_21_quellen(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Quellen", person="Alle", kicker="Verwendete Materialien")

    add_bullets(slide, [
        "BMBWF - Lehrplan & Formelsammlung Angewandte Mathematik (AHS/BHS)",
        "Schulbuch Angewandte Mathematik (Klassenset - Titel/Verlag bitte ergänzen)",
        "mathe-online.at - Kombinatorik & Wahrscheinlichkeitsrechnung",
        "Österreichische Lotterien - Spielregeln & Gewinnwahrscheinlichkeiten Lotto 6 aus 45",
        "Wikipedia - Permutation, Variation, Kombination, Laplace-Wahrscheinlichkeit (Stand: Juni 2026)",
        "Alle Diagramme und Formelgrafiken: selbst erstellt mit Python (matplotlib, python-pptx)",
    ], CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(5.0), size=Pt(20), space_after=Pt(18))

    page_number(slide, 21)
    set_notes(slide, "Diese Folie kurz zeigen (relevant für die Bewertung), Inhalt nicht im Detail "
              "vortragen - z. B. nur sagen 'Unsere Quellen findet ihr hier zum Nachlesen.' "
              "Vor der Abgabe den genauen Schulbuch-Titel/Verlag ergänzen.")
    return slide


# ---------------------------------------------------------------------------
# Slide 22 - Danke / Fragen
# ---------------------------------------------------------------------------

def slide_22_danke(prs):
    slide = new_slide(prs, bg=DEEP_BLUE)

    add_rect(slide, Inches(-1.3), Inches(-1.2), Inches(3.6), Inches(3.6), fill=ORANGE, shape=MSO_SHAPE.OVAL)
    add_rect(slide, Inches(11.0), Inches(4.5), Inches(3.8), Inches(3.8), fill=MID_BLUE, shape=MSO_SHAPE.OVAL)
    add_rect(slide, Inches(0.8), Inches(5.8), Inches(2.0), Inches(2.0), fill=YELLOW, shape=MSO_SHAPE.OVAL)

    add_text(slide, "Danke für eure Aufmerksamkeit!", Inches(0.9), Inches(2.6), Inches(11.5), Inches(1.2),
             size=Pt(44), color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER)
    add_text(slide, "Fragen?", Inches(0.9), Inches(3.9), Inches(11.5), Inches(1.0),
             size=Pt(32), color=YELLOW, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER)

    add_text(slide, "Person A  ·  Person B  ·  Person C", Inches(0.9), Inches(6.5), Inches(11.5), Inches(0.5),
             size=Pt(16), color=LIGHT_BLUE, align=PP_ALIGN.CENTER)

    set_notes(slide, "Alle drei bedanken sich gemeinsam und stehen für Fragen aus dem Publikum bereit. "
              "Falls keine Fragen kommen: selbst eine Anschlussfrage stellen, z. B. "
              "'Welches der heutigen Beispiele hat euch am meisten überrascht?'")
    return slide


# ---------------------------------------------------------------------------
# Build & save
# ---------------------------------------------------------------------------

def build():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    slide_01_title(prs)
    slide_02_agenda(prs)
    slide_03_zaehlprinzip(prs)
    slide_04_permutation(prs)
    slide_05_aufgabe1(prs)
    slide_06_loesung1(prs)
    slide_07_variation(prs)
    slide_08_kombination(prs)
    slide_09_pascal(prs)
    slide_10_aufgabe2(prs)
    slide_11_loesung2(prs)
    slide_12_laplace(prs)
    slide_13_wuerfeln(prs)
    slide_14_lotto_wahrscheinlichkeit(prs)
    slide_15_aufgabe3(prs)
    slide_16_loesung3(prs)
    slide_17_quiz(prs)
    slide_18_loesung_quiz(prs)
    slide_19_uebersicht(prs)
    slide_20_zusammenfassung(prs)
    slide_21_quellen(prs)
    slide_22_danke(prs)

    return prs


if __name__ == "__main__":
    prs = build()
    out_path = os.path.join(os.path.dirname(__file__), "kombinatorik_praesentation.pptx")
    prs.save(out_path)
    print(f"Saved {out_path}")





