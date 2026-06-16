"""Build the Kombinatorik & Wahrscheinlichkeit presentation (.pptx) — 18 Folien, 20-25 Min.

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
# Slide 1 – Titelfolie
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

    set_notes(slide, "Begrüßung durch alle drei Vortragenden. Kurze Vorstellung. "
              "Ziel: Ihr versteht heute, wie man zählt ohne wirklich zu zählen – "
              "und warum manche Zahlen viel größer sind als man denkt.")
    return slide


# ---------------------------------------------------------------------------
# Slide 2 – Agenda + Gedankenexperiment-Einstieg
# ---------------------------------------------------------------------------

def slide_02_agenda(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Agenda & Einstiegsfragen", person="A", kicker="Heute auf dem Programm")

    add_bullets(slide, [
        "Das Zählprinzip",
        "Permutation, Variation, Kombination",
        "Pascal'sches Dreieck",
        "Laplace-Wahrscheinlichkeit",
        "Praktischer Teil: Estimation-Spiel",
    ], CONTENT_LEFT, CONTENT_TOP, COL_W, Inches(4.2), size=Pt(19), space_after=Pt(18))

    add_panel(slide, COL2_LEFT, CONTENT_TOP, COL_W, Inches(5.6), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "GEDANKENEXPERIMENT", COL2_LEFT + Inches(0.35), CONTENT_TOP + Inches(0.35),
                    fill=ORANGE, width=Inches(3.0), height=Inches(0.5))
    add_text(slide, "Drei Fragen – notiert eure Schätzung im Kopf:",
             COL2_LEFT + Inches(0.35), CONTENT_TOP + Inches(1.1), COL_W - Inches(0.7), Inches(0.6),
             size=Pt(16), bold=True, color=DARK)

    questions = [
        ("1", "Wie viele 4-stellige PIN-Codes gibt es?"),
        ("2", "Ihr alle tauscht eure Handynummern aus.\nWie viele Austausche finden statt?"),
        ("3", "Wie wahrscheinlich ist Lotto 6 aus 45?"),
    ]
    for i, (num, q) in enumerate(questions):
        top = CONTENT_TOP + Inches(1.8) + i * Inches(1.3)
        add_circle_badge(slide, num, COL2_LEFT + Inches(0.3), top, Inches(0.55), fill=DEEP_BLUE, size=Pt(18))
        add_text(slide, q, COL2_LEFT + Inches(1.1), top, COL_W - Inches(1.4), Inches(1.15), size=Pt(15))

    page_number(slide, 2)
    set_notes(slide, "Person A stellt die Agenda vor und präsentiert die drei Gedankenexperiment-Fragen. "
              "Kurze Pause nach jeder Frage – das Publikum soll mental schätzen, NICHT laut antworten. "
              "Sagen: 'Diese drei Fragen werden wir heute Schritt für Schritt beantworten!' "
              "Überleitung zu Person B für das Zählprinzip.")
    return slide


# ---------------------------------------------------------------------------
# Slide 3 – Zählprinzip
# ---------------------------------------------------------------------------

def slide_03_zaehlprinzip(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Das Zählprinzip", person="B", kicker="Die Grundlage der Kombinatorik")

    add_text(slide, "Besteht ein Vorgang aus mehreren Schritten und gibt es für jeden "
             "Schritt mehrere Möglichkeiten, multipliziert man die Anzahl der "
             "Möglichkeiten pro Schritt:",
             CONTENT_LEFT, CONTENT_TOP, COL_W, Inches(1.7), size=Pt(18))
    add_formula(slide, "f_zaehlprinzip", box_left=CONTENT_LEFT, box_top=Inches(3.0),
                 box_width=COL_W, box_height=Inches(1.0))

    add_panel(slide, CONTENT_LEFT, Inches(4.3), COL_W, Inches(2.55), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "BEISPIEL: OUTFIT", CONTENT_LEFT + Inches(0.3), Inches(4.55), fill=ORANGE,
                    width=Inches(2.6), height=Inches(0.45), size=Pt(14))
    add_text(slide, "3 Hemden  ×  4 Hosen  ×  2 Paar Schuhe\n"
             "Raster zeigt 12 Hemd-Hosen-Komb., × 2 Schuhe → 24 Outfits",
             CONTENT_LEFT + Inches(0.3), Inches(5.15), COL_W - Inches(0.6), Inches(1.55), size=Pt(16))

    add_picture_fit(slide, "outfit_grid.png", COL2_LEFT, CONTENT_TOP, COL_W, Inches(4.25))
    add_text(slide, "Formel: 3 × 4 × 2 =", COL2_LEFT, Inches(5.55), Inches(2.5), Inches(0.8),
             size=Pt(16), bold=True, color=DARK)
    add_formula(slide, "f_beispiel_outfits", left=COL2_LEFT + Inches(2.5), top=Inches(5.6), height=Inches(0.55))

    page_number(slide, 3)
    set_notes(slide, "Person B erklärt das Zählprinzip am Outfit-Beispiel: 3×4=12 Hemd-Hosen-Kombinationen, "
              "jede davon × 2 Schuhe = 24. Das Raster macht das visuell greifbar. "
              "Betonen: Das Zählprinzip ist die GRUNDLAGE für Permutation, Variation und Kombination! "
              "Überleitung zu Person C.")
    return slide


# ---------------------------------------------------------------------------
# Slide 4 – Permutation
# ---------------------------------------------------------------------------

def slide_04_permutation(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Permutation", person="C", kicker="Sitzordnung & Anagramm")

    # Band 1: ohne Wiederholung
    add_label_chip(slide, "OHNE WIEDERHOLUNG", CONTENT_LEFT, CONTENT_TOP, fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_permutation_ohne", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(0.6), height=Inches(0.55))
    add_text(slide, "Alle n Elemente werden angeordnet, jede Position zählt.",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.35), COL_W, Inches(0.7), size=Pt(14))
    add_text(slide, "Beispiel: 5 Personen am Tisch →",
             CONTENT_LEFT, CONTENT_TOP + Inches(2.1), Inches(3.6), Inches(0.6), size=Pt(14))
    add_formula(slide, "f_beispiel_5fakultaet", left=CONTENT_LEFT + Inches(3.7), top=CONTENT_TOP + Inches(2.05),
                 height=Inches(0.5))

    add_picture_fit(slide, "permutation_tree.png", COL2_LEFT, CONTENT_TOP - Inches(0.05), COL_W, Inches(2.15))
    add_text(slide, "3 Freunde (A, B, C): 3! = 6 Sitzordnungen",
             COL2_LEFT, CONTENT_TOP + ROW_H - Inches(0.55), COL_W, Inches(0.55),
             size=Pt(13), color=GRAY, align=PP_ALIGN.CENTER)

    # Band 2: mit Wiederholung
    add_label_chip(slide, "MIT WIEDERHOLUNG", CONTENT_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_permutation_mit", left=CONTENT_LEFT, top=ROW2_TOP + Inches(0.6), height=Inches(0.6))
    add_text(slide, "Manche Elemente sind gleich – teilen durch deren Fakultäten.",
             CONTENT_LEFT, ROW2_TOP + Inches(1.4), COL_W, Inches(0.8), size=Pt(14))

    add_label_chip(slide, "BEISPIEL: ANAGRAMM", COL2_LEFT, ROW2_TOP, fill=MID_BLUE,
                    width=Inches(2.9), height=Inches(0.45), size=Pt(13))
    add_colored_word(slide, [
        ("A", DEEP_BLUE), ("N", ORANGE), ("A", DEEP_BLUE),
        ("N", ORANGE), ("A", DEEP_BLUE), ("S", MID_BLUE),
    ], COL2_LEFT, ROW2_TOP + Inches(0.55), COL_W, Inches(0.9), size=Pt(40))
    add_text(slide, "Verschiedene Anordnungen von ANANAS?",
             COL2_LEFT, ROW2_TOP + Inches(1.5), COL_W, Inches(0.65), size=Pt(14), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_ananas", box_left=COL2_LEFT, box_top=ROW2_TOP + Inches(2.1),
                 box_width=COL_W, box_height=Inches(0.65))

    page_number(slide, 4)
    set_notes(slide, "Person C erklärt Permutation ohne Wiederholung (Baumdiagramm, 3 Freunde = 6 Reihenfolgen, "
              "dann 5 Personen = 5!=120). Danach ANANAS mit Wiederholung: 6 Buchstaben, "
              "A kommt 3x, N 2x vor → 6!/(3!·2!·1!)=60. "
              "Überleitung zu Person A.")
    return slide


# ---------------------------------------------------------------------------
# Slide 5 – Variation
# ---------------------------------------------------------------------------

def slide_05_variation(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Variation", person="A", kicker="Stockerlplatz & PIN-Code")

    # Band 1: ohne Wiederholung
    add_label_chip(slide, "OHNE WIEDERHOLUNG", CONTENT_LEFT, CONTENT_TOP, fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_variation_ohne", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(0.6), height=Inches(0.55))
    add_text(slide, "Reihenfolge wichtig, ohne Zurücklegen: k von n Elementen "
             "werden ausgewählt UND angeordnet.",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.35), COL_W, Inches(1.1), size=Pt(14))
    add_formula(slide, "f_beispiel_stockerl", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(2.35), height=Inches(0.5))

    add_picture_fit(slide, "podium.png", COL2_LEFT + Inches(0.6), CONTENT_TOP - Inches(0.05),
                     COL_W - Inches(1.2), Inches(2.0))
    add_text(slide, "8 Läufer:innen, Plätze 1-3 → V(8,3) = 8·7·6 = 336",
             COL2_LEFT, CONTENT_TOP + ROW_H - Inches(0.55), COL_W, Inches(0.55),
             size=Pt(13), color=GRAY, align=PP_ALIGN.CENTER)

    # Band 2: mit Wiederholung – Auflösung PIN-Hook
    add_label_chip(slide, "MIT WIEDERHOLUNG", CONTENT_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_variation_mit", left=CONTENT_LEFT, top=ROW2_TOP + Inches(0.6), height=Inches(0.55))
    add_text(slide, "Reihenfolge wichtig, MIT Zurücklegen: jede Stelle kann beliebig "
             "aus allen n Möglichkeiten gewählt werden.",
             CONTENT_LEFT, ROW2_TOP + Inches(1.35), COL_W, Inches(1.3), size=Pt(14))

    add_label_chip(slide, "AUFLÖSUNG: FRAGE 1", COL2_LEFT, ROW2_TOP, fill=MID_BLUE,
                    width=Inches(3.0), height=Inches(0.45), size=Pt(13))
    pin_w = Inches(0.9)
    pin_gap = Inches(0.28)
    pin_total = pin_w * 4 + pin_gap * 3
    pin_left = COL2_LEFT + (COL_W - pin_total) // 2
    for i in range(4):
        x = pin_left + i * (pin_w + pin_gap)
        add_rect(slide, x, ROW2_TOP + Inches(0.65), pin_w, pin_w, fill=LIGHT_BLUE, line=DEEP_BLUE,
                 line_width=Pt(1.5), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        add_text(slide, str(i) if False else "?", x, ROW2_TOP + Inches(0.65), pin_w, pin_w, size=Pt(36),
                 color=DEEP_BLUE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, "4-stelliger PIN, Ziffern 0-9, Wiederholung erlaubt:",
             COL2_LEFT, ROW2_TOP + Inches(1.75), COL_W, Inches(0.45), size=Pt(13), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_pin", box_left=COL2_LEFT, box_top=ROW2_TOP + Inches(2.2),
                 box_width=COL_W, box_height=Inches(0.6))

    page_number(slide, 5)
    set_notes(slide, "Person A erklärt Variation ohne Wiederholung (Stockerlplatz: 8 Läufer, nur 3 Plätze, "
              "Reihenfolge zählt → V(8,3)=336). Dann Variation MIT Wiederholung und die Auflösung der "
              "ersten Gedankenexperiment-Frage: 10^4 = 10.000 PINs! "
              "Überleitung zu Person B.")
    return slide


# ---------------------------------------------------------------------------
# Slide 6 – Kombination
# ---------------------------------------------------------------------------

def slide_06_kombination(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Kombination", person="B", kicker="Handynummern & Eisbecher")

    # Band 1: ohne Wiederholung – Handynummern (class-specific!)
    add_label_chip(slide, "OHNE WIEDERHOLUNG", CONTENT_LEFT, CONTENT_TOP, fill=DEEP_BLUE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_kombination_ohne", left=CONTENT_LEFT, top=CONTENT_TOP + Inches(0.6), height=Inches(0.6))
    add_text(slide, "Reihenfolge EGAL, ohne Zurücklegen.",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.4), COL_W, Inches(0.6), size=Pt(14))

    add_label_chip(slide, "AUFLÖSUNG: FRAGE 2", COL2_LEFT, CONTENT_TOP, fill=MID_BLUE,
                    width=Inches(3.0), height=Inches(0.45), size=Pt(13))
    add_text(slide, "Ihr 15 Schüler:innen tauscht gegenseitig\nHandynummern aus – wie viele Austausche?",
             COL2_LEFT, CONTENT_TOP + Inches(0.55), COL_W, Inches(1.0), size=Pt(16), bold=True, color=DEEP_BLUE)
    add_text(slide, "Reihenfolge egal (A tauscht mit B = B tauscht mit A) →",
             COL2_LEFT, CONTENT_TOP + Inches(1.55), COL_W, Inches(0.55), size=Pt(14))
    add_formula(slide, "f_handshake", box_left=COL2_LEFT, box_top=CONTENT_TOP + Inches(2.15),
                 box_width=COL_W, box_height=Inches(0.7))

    # Band 2: mit Wiederholung – Eisbecher
    add_label_chip(slide, "MIT WIEDERHOLUNG", CONTENT_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_kombination_mit", left=CONTENT_LEFT, top=ROW2_TOP + Inches(0.6), height=Inches(0.6))
    add_text(slide, "Reihenfolge egal, MIT Zurücklegen.",
             CONTENT_LEFT, ROW2_TOP + Inches(1.4), COL_W, Inches(0.6), size=Pt(14))

    add_label_chip(slide, "BEISPIEL: EISBECHER", COL2_LEFT, ROW2_TOP, fill=ORANGE,
                    width=Inches(2.7), height=Inches(0.45), size=Pt(13))
    add_picture_fit(slide, "icecream.png", COL2_LEFT + Inches(1.6), ROW2_TOP + Inches(0.55),
                     Inches(2.6), Inches(1.55))
    add_text(slide, "3 Kugeln aus 5 Sorten, Wiederholung erlaubt:",
             COL2_LEFT, ROW2_TOP + Inches(2.1), COL_W, Inches(0.4), size=Pt(13), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_beispiel_eis", box_left=COL2_LEFT, box_top=ROW2_TOP + Inches(2.4),
                 box_width=COL_W, box_height=Inches(0.5))

    page_number(slide, 6)
    set_notes(slide, "Person B erklärt Kombination ohne Wiederholung am Handynummer-Beispiel: "
              "15 Schüler:innen, Reihenfolge egal → C(15,2) = 105 Austausche! "
              "Viele Leute erwarten ~15 oder ~30 – 105 überrascht. Das ist die Auflösung von Frage 2! "
              "Dann Kombination MIT Wiederholung (Eisbecher). Überleitung zu Person C.")
    return slide


# ---------------------------------------------------------------------------
# Slide 7 – Pascal'sches Dreieck
# ---------------------------------------------------------------------------

def slide_07_pascal(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Pascal'sches Dreieck", person="C", kicker="Verbindung zum Binomialkoeffizienten")

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
    add_text(slide, "Die orange 15 im Dreieck = binom(6,2)\ngenau wie bei Lotto 6 aus 45.",
             COL2_LEFT + Inches(2.4), panel_top + Inches(0.65), COL_W - Inches(2.7), Inches(0.95), size=Pt(13))

    page_number(slide, 7)
    set_notes(slide, "Person C zeigt das Pascal'sche Dreieck: jede Zahl = Summe der zwei Zahlen darüber "
              "(Rekursionsformel). Die orange 15 = binom(6,2) – direkte Verbindung zu Kombination. "
              "Das Dreieck ist eine fertige Tabelle für alle Binomialkoeffizienten. "
              "Überleitung zu Person A.")
    return slide


# ---------------------------------------------------------------------------
# Slide 8 – Laplace-Formel + Würfeln (kombiniert)
# ---------------------------------------------------------------------------

def slide_08_laplace(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Laplace-Wahrscheinlichkeit", person="A", kicker="Von Zählen zu Chancen")

    # Linke Spalte: Formel + Konzept
    add_formula(slide, "f_laplace", box_left=CONTENT_LEFT, box_top=CONTENT_TOP,
                 box_width=COL_W, box_height=Inches(1.5))

    add_panel(slide, CONTENT_LEFT, Inches(3.0), COL_W, Inches(1.2), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|A|  –  GÜNSTIGE FÄLLE", CONTENT_LEFT + Inches(0.3), Inches(3.2), fill=ORANGE,
                    width=Inches(3.0), height=Inches(0.4), size=Pt(12))
    add_text(slide, "Ergebnisse, die Ereignis A erfüllen.",
             CONTENT_LEFT + Inches(0.3), Inches(3.7), COL_W - Inches(0.6), Inches(0.4), size=Pt(14))

    add_panel(slide, CONTENT_LEFT, Inches(4.35), COL_W, Inches(1.2), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|Ω|  –  MÖGLICHE FÄLLE", CONTENT_LEFT + Inches(0.3), Inches(4.55), fill=DEEP_BLUE,
                    width=Inches(3.0), height=Inches(0.4), size=Pt(12))
    add_text(slide, "Alle Ergebnisse – der gesamte Ergebnisraum Ω.",
             CONTENT_LEFT + Inches(0.3), Inches(5.05), COL_W - Inches(0.6), Inches(0.4), size=Pt(14))

    add_panel(slide, CONTENT_LEFT, Inches(5.7), COL_W, Inches(1.05), fill=YELLOW, line=ORANGE)
    add_text(slide, "Voraussetzung: Laplace-Experiment –\nalle Ergebnisse gleich wahrscheinlich.",
             CONTENT_LEFT + Inches(0.35), Inches(5.7), COL_W - Inches(0.7), Inches(1.05),
             size=Pt(15), bold=True, color=DEEP_BLUE, anchor=MSO_ANCHOR.MIDDLE)

    # Rechte Spalte: Würfeln Beispiel
    add_label_chip(slide, "BEISPIEL: WÜRFELN (PASCH)", COL2_LEFT, CONTENT_TOP, fill=MID_BLUE,
                    width=Inches(3.5), height=Inches(0.45), size=Pt(13))
    add_picture_fit(slide, "dice_grid.png", COL2_LEFT, CONTENT_TOP + Inches(0.6), COL_W, Inches(4.0))
    add_text(slide, "|Ω| = 36 (6·6, Zählprinzip)   |A| = 6 Paschs (Diagonale)",
             COL2_LEFT, CONTENT_TOP + Inches(4.75), COL_W, Inches(0.45), size=Pt(13), align=PP_ALIGN.CENTER)
    add_formula(slide, "f_pasch", box_left=COL2_LEFT, box_top=Inches(5.35),
                 box_width=COL_W, box_height=Inches(0.9))

    page_number(slide, 8)
    set_notes(slide, "Person A führt die Laplace-Wahrscheinlichkeit ein: P(A)=|A|/|Omega|. "
              "Sofort am Beispiel demonstrieren: Würfelpasch. |Omega|=36 (Zählprinzip!), |A|=6 (Diagonale). "
              "P(Pasch)=6/36=1/6. Betonen: Kombinatorik UND Wahrscheinlichkeit hängen direkt zusammen. "
              "Überleitung zu Person B.")
    return slide


# ---------------------------------------------------------------------------
# Slide 9 – Lotto 6 aus 45 (Auflösung Frage 3)
# ---------------------------------------------------------------------------

def slide_09_lotto(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Lotto 6 aus 45", person="B", kicker="Auflösung: Wie wahrscheinlich ist ein Sechser?")

    add_label_chip(slide, "AUFLÖSUNG: FRAGE 3", CONTENT_LEFT, CONTENT_TOP, fill=ORANGE,
                    width=Inches(3.0), height=Inches(0.5))
    add_picture_fit(slide, "lotto_balls.png", CONTENT_LEFT, CONTENT_TOP + Inches(0.65), CONTENT_W, Inches(1.2))

    panel_top = Inches(3.05)
    panel_h = Inches(1.4)
    add_panel(slide, CONTENT_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|Ω| – ALLE MÖGLICHEN TIPPS", CONTENT_LEFT + Inches(0.3), panel_top + Inches(0.2),
                    fill=DEEP_BLUE, width=Inches(3.2), height=Inches(0.45), size=Pt(13))
    add_formula(slide, "f_lotto_komb", box_left=CONTENT_LEFT, box_top=panel_top + Inches(0.75),
                 box_width=COL_W, box_height=Inches(0.6))

    add_panel(slide, COL2_LEFT, panel_top, COL_W, panel_h, fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "|A| – GENAU DEIN TIPP", COL2_LEFT + Inches(0.3), panel_top + Inches(0.2),
                    fill=ORANGE, width=Inches(2.8), height=Inches(0.45), size=Pt(13))
    add_text(slide, "1   (genau der eine gezogene Tipp)",
             COL2_LEFT + Inches(0.3), panel_top + Inches(0.75), COL_W - Inches(0.6), Inches(0.55), size=Pt(16))

    add_formula(slide, "f_lotto_prob", box_left=CONTENT_LEFT, box_top=Inches(4.65),
                 box_width=CONTENT_W, box_height=Inches(1.0))

    add_panel(slide, CONTENT_LEFT, Inches(5.85), CONTENT_W, Inches(1.1), fill=YELLOW, line=ORANGE)
    add_text(slide, "Das ist ungefähr so wahrscheinlich, wie unter allen Einwohner:innen Österreichs "
             "(9 Mio.) zufällig genau eine bestimmte Person auszuwählen.",
             CONTENT_LEFT + Inches(0.4), Inches(5.85), CONTENT_W - Inches(0.8), Inches(1.1),
             size=Pt(14), bold=True, color=DEEP_BLUE, anchor=MSO_ANCHOR.MIDDLE)

    page_number(slide, 9)
    set_notes(slide, "Person B löst die dritte Gedankenexperiment-Frage auf: P(6 Richtige)=1/8.145.060. "
              "Den Österreich-Vergleich nutzen, um die Größenordnung greifbar zu machen. "
              "Jetzt alle 3 Fragen beantwortet – kurze Pause, dann Überleitung zu Person C für "
              "den praktischen Teil.")
    return slide


# ---------------------------------------------------------------------------
# Slide 10 – Praktischer Teil: Estimation-Spiel (Intro)
# ---------------------------------------------------------------------------

def slide_10_spiel_intro(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Praktischer Teil", person="C", kicker="Estimation-Spiel")

    add_text(slide, "Jetzt seid ihr dran!", CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(1.0),
             size=Pt(44), bold=True, color=DEEP_BLUE, font=FONT_HEAD, align=PP_ALIGN.CENTER)

    add_panel(slide, CONTENT_LEFT, Inches(2.55), CONTENT_W, Inches(3.4), fill=LIGHT_BLUE, line=MID_BLUE)
    add_text(slide, "Wie das Spiel funktioniert:",
             CONTENT_LEFT + Inches(0.5), Inches(2.75), CONTENT_W - Inches(1.0), Inches(0.6),
             size=Pt(22), bold=True, color=DEEP_BLUE)
    add_bullets(slide, [
        "Wir stellen eine überraschende Frage.",
        "Jede Person schätzt still – kein Austausch mit Sitznachbar:innen!",
        "Dann rechnen wir gemeinsam nach.",
        "Wer lag am nächsten dran? (kein Preis, nur Ruhm 😄)",
    ], CONTENT_LEFT + Inches(0.5), Inches(3.45), CONTENT_W - Inches(1.0), Inches(2.3),
       size=Pt(18), space_after=Pt(12), bullet_color=ORANGE)

    add_text(slide, "2 Runden – bereit?",
             CONTENT_LEFT, Inches(6.15), CONTENT_W, Inches(0.7),
             size=Pt(24), bold=True, color=ORANGE, font=FONT_HEAD, align=PP_ALIGN.CENTER)

    page_number(slide, 10)
    set_notes(slide, "Person C erklärt kurz die Spielregeln und erzeugt Spannung. "
              "Wichtig: Schätzungen werden im Kopf behalten oder auf einen Zettel geschrieben – "
              "KEIN Taschenrechner, KEIN Gespräch! Dann Überleitung zu Person A für Runde 1.")
    return slide


# ---------------------------------------------------------------------------
# Slide 11 – Estimation Runde 1: Frage (Klasse verlässt Zimmer)
# ---------------------------------------------------------------------------

def slide_11_runde1_frage(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Runde 1 – Eure Schätzung", person="A", kicker="Permutation im echten Leben")

    add_panel(slide, CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(4.2), fill=LIGHT_BLUE, line=MID_BLUE)
    add_text(slide, "Wenn ihr alle nacheinander das Zimmer verlasst –",
             CONTENT_LEFT + Inches(0.5), CONTENT_TOP + Inches(0.35), CONTENT_W - Inches(1.0), Inches(0.9),
             size=Pt(24), bold=True, color=DEEP_BLUE)
    add_text(slide, "wie viele verschiedene Reihenfolgen gibt es\nfür euch 15 Schüler:innen?",
             CONTENT_LEFT + Inches(0.5), CONTENT_TOP + Inches(1.25), CONTENT_W - Inches(1.0), Inches(1.2),
             size=Pt(28), bold=True, color=DARK)
    add_colored_word(slide, [(c, ORANGE) for c in "?!?!?"],
                      CONTENT_LEFT, CONTENT_TOP + Inches(2.55), CONTENT_W, Inches(1.2), size=Pt(60))

    add_text(slide, "Schreib deine Schätzung auf – wir vergleichen gleich!",
             CONTENT_LEFT, CONTENT_TOP + Inches(4.4), CONTENT_W, Inches(0.55),
             size=Pt(17), italic=True, color=GRAY, align=PP_ALIGN.CENTER)

    page_number(slide, 11)
    set_notes(slide, "Person A liest die Frage vor und gibt 30-45 Sekunden Zeit zum Schätzen. "
              "Dann kurze Handshow: 'Wer schätzt unter 1.000? Unter 1 Million? Über 1 Milliarde?' "
              "Spannung erzeugen, dann Überleitung zu Person B für die Auflösung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 12 – Estimation Runde 1: Auflösung
# ---------------------------------------------------------------------------

def slide_12_runde1_aufloesung(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Runde 1 – Auflösung", person="B", kicker="15! – Permutation")

    add_formula(slide, "f_klasse_perm", box_left=CONTENT_LEFT, box_top=CONTENT_TOP,
                 box_width=CONTENT_W, box_height=Inches(1.3))

    add_text(slide, "Das entspricht der Permutation von 15 Personen: P(15) = 15!",
             CONTENT_LEFT, CONTENT_TOP + Inches(1.45), CONTENT_W, Inches(0.6),
             size=Pt(17), color=DARK, align=PP_ALIGN.CENTER)

    add_panel(slide, CONTENT_LEFT, Inches(3.3), COL_W, Inches(3.7), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "ZUM VERGLEICH", CONTENT_LEFT + Inches(0.3), Inches(3.5), fill=DEEP_BLUE,
                    width=Inches(2.4), height=Inches(0.45), size=Pt(13))
    add_bullets(slide, [
        "1 Reihenfolge pro Sekunde →",
        "≈ 41.466 Jahre, um alle durchzuprobieren",
        "Beginn: ca. 39.000 v. Chr. (Steinzeit!)",
        "Ende: ca. heute",
    ], CONTENT_LEFT + Inches(0.3), Inches(4.1), COL_W - Inches(0.6), Inches(2.7),
       size=Pt(16), space_after=Pt(10), bullet_color=ORANGE)

    add_panel(slide, COL2_LEFT, Inches(3.3), COL_W, Inches(3.7), fill=YELLOW, line=ORANGE)
    add_label_chip(slide, "FORMEL", COL2_LEFT + Inches(0.3), Inches(3.5), fill=ORANGE,
                    width=Inches(1.5), height=Inches(0.45), size=Pt(13))
    add_text(slide, "15! = 15 · 14 · 13 · ... · 2 · 1\n\n"
             "Wachstum der Fakultät ist astronomisch schnell –\n"
             "schon 15! übersteigt 1,3 Billionen!",
             COL2_LEFT + Inches(0.3), Inches(4.1), COL_W - Inches(0.6), Inches(2.7),
             size=Pt(17), color=DEEP_BLUE)

    page_number(slide, 12)
    set_notes(slide, "Person B enthüllt die Auflösung: 15! = 1.307.674.368.000 ≈ 1,3 Billionen! "
              "Den 'Steinzeit-Vergleich' als Anker verwenden: seit ca. 39.000 v. Chr. eine "
              "Reihenfolge pro Sekunde – und man wäre gerade fertig (Homo sapiens war damals "
              "gerade auf dem Weg nach Europa!). Kurzes 'WOW' abwarten. "
              "Überleitung zu Person C für Runde 2.")
    return slide


# ---------------------------------------------------------------------------
# Slide 13 – Estimation Runde 2: Frage (Kartenspiel)
# ---------------------------------------------------------------------------

def slide_13_runde2_frage(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Runde 2 – Eure Schätzung", person="C", kicker="Noch größere Zahlen")

    add_panel(slide, CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(4.2), fill=LIGHT_BLUE, line=MID_BLUE)
    add_text(slide, "Wie viele verschiedene Möglichkeiten gibt es,",
             CONTENT_LEFT + Inches(0.5), CONTENT_TOP + Inches(0.35), CONTENT_W - Inches(1.0), Inches(0.9),
             size=Pt(24), bold=True, color=DEEP_BLUE)
    add_text(slide, "ein Standard-Kartenspiel mit 52 Karten\nzu mischen?",
             CONTENT_LEFT + Inches(0.5), CONTENT_TOP + Inches(1.25), CONTENT_W - Inches(1.0), Inches(1.2),
             size=Pt(28), bold=True, color=DARK)
    add_colored_word(slide, [(c, ORANGE) for c in "?!?!?"],
                      CONTENT_LEFT, CONTENT_TOP + Inches(2.55), CONTENT_W, Inches(1.2), size=Pt(60))

    add_text(slide, "Tipp: Das ist eine Permutation von 52 Elementen – P(52) = 52!",
             CONTENT_LEFT, CONTENT_TOP + Inches(4.4), CONTENT_W, Inches(0.55),
             size=Pt(17), italic=True, color=GRAY, align=PP_ALIGN.CENTER)

    page_number(slide, 13)
    set_notes(slide, "Person C liest die Frage vor. Diesmal gibt es einen Tipp ('Permutation von 52') "
              "damit die Klasse annähernd die Größenordnung einschätzen kann. Gleich: Handshow-Schätzung "
              "'Wer sagt mehr als 1.000? 1 Million? 1 Milliarde? 1 Trillion?' "
              "Überleitung zu Person A für die Auflösung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 14 – Estimation Runde 2: Auflösung (52!)
# ---------------------------------------------------------------------------

def slide_14_runde2_aufloesung(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Runde 2 – Auflösung", person="A", kicker="52! – die unvorstellbare Zahl")

    add_formula(slide, "f_kartenspiel", box_left=CONTENT_LEFT, box_top=CONTENT_TOP,
                 box_width=CONTENT_W, box_height=Inches(1.0))

    add_panel(slide, CONTENT_LEFT, Inches(2.55), CONTENT_W, Inches(2.3), fill=LIGHT_BLUE, line=MID_BLUE)
    add_label_chip(slide, "DAS BEDEUTET ...", CONTENT_LEFT + Inches(0.4), Inches(2.7), fill=DEEP_BLUE,
                    width=Inches(2.5), height=Inches(0.45), size=Pt(13))
    add_bullets(slide, [
        "Das sichtbare Universum hat ca. 10⁸⁰ Atome.",
        "52! ≈ 8 × 10⁶⁷  –  das ist immer noch kleiner als 10⁸⁰.",
        "Aber: Wenn jedes Atom seit dem Urknall jede Sekunde eine neue Reihenfolge bildet "
        "→ es gäbe noch kaum Wiederholungen.",
    ], CONTENT_LEFT + Inches(0.4), Inches(3.25), CONTENT_W - Inches(0.8), Inches(1.45),
       size=Pt(16), space_after=Pt(8), bullet_color=ORANGE)

    add_panel(slide, CONTENT_LEFT, Inches(5.1), CONTENT_W, Inches(1.8), fill=YELLOW, line=ORANGE)
    add_text(slide, "Fazit: Fast jede Kartenmischung, die du je in deinem Leben machst,\n"
             "ist mit höchster Wahrscheinlichkeit einzigartig in der gesamten Menschheitsgeschichte.",
             CONTENT_LEFT + Inches(0.5), Inches(5.1), CONTENT_W - Inches(1.0), Inches(1.8),
             size=Pt(18), bold=True, color=DEEP_BLUE, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)

    page_number(slide, 14)
    set_notes(slide, "Person A enthüllt 52! ≈ 8,07×10^67. Die drei Bullet-Points nacheinander vorlesen "
              "und kurze Pause danach lassen – das 'Fazit' ist ein echter Gesprächsstarter. "
              "Überleitung zu Person B: 'Jetzt fassen wir alles nochmal kompakt zusammen – "
              "welche Formel, wann?'")
    return slide


# ---------------------------------------------------------------------------
# Slide 15 – Übersichtstabelle
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


def slide_15_uebersicht(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Übersichtstabelle", person="B", kicker="Wann verwende ich was?")

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
        ("Variation – ohne Wiederholung", "Ja", "Nein", "V(n,k) = n! / (n−k)!"),
        ("Variation – mit Wiederholung", "Ja", "Ja", "V_W(n,k) = nᵏ"),
        ("Kombination – ohne Wiederholung", "Nein", "Nein", "C(n,k) = (n über k)"),
        ("Kombination – mit Wiederholung", "Nein", "Ja", "C_W(n,k) = (n+k−1 über k)"),
    ]
    for r, row_data in enumerate(data, start=1):
        fill = LIGHT_BLUE if r % 2 == 1 else WHITE
        for c, val in enumerate(row_data):
            bold = (c == 0)
            align = PP_ALIGN.LEFT if c in (0, 3) else PP_ALIGN.CENTER
            _set_cell(table.cell(r, c), val, bold=bold, color=DEEP_BLUE if c == 0 else DARK,
                      size=Pt(14), fill=fill, align=align)

    add_text(slide, "Tipp: Zuerst fragen – Ist die Reihenfolge wichtig? Dann – Wird wiederholt?",
             CONTENT_LEFT, Inches(6.85), CONTENT_W, Inches(0.4), size=Pt(13), color=GRAY, italic=True,
             align=PP_ALIGN.CENTER)

    page_number(slide, 15)
    set_notes(slide, "Person B fasst alle 5 Konzepte in der Entscheidungstabelle zusammen. "
              "Die zwei Fragen (Reihenfolge? Wiederholung?) direkt nennen – das ist der "
              "Matura-Trick, der immer funktioniert. Überleitung zu allen drei für die Zusammenfassung.")
    return slide


# ---------------------------------------------------------------------------
# Slide 16 – Zusammenfassung
# ---------------------------------------------------------------------------

def slide_16_zusammenfassung(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Zusammenfassung", person="Alle", kicker="Die wichtigsten Takeaways")

    takeaways = [
        ("A", DEEP_BLUE, "Das Zählprinzip ist die Basis: Bei unabhängigen Schritten einfach "
         "die Möglichkeiten pro Schritt multiplizieren."),
        ("B", ORANGE, "Zwei Fragen führen zur richtigen Formel: Ist die Reihenfolge wichtig? "
         "Wird mit Wiederholung gewählt?"),
        ("C", MID_BLUE, "Mit Laplace P(A) = |A| / |Ω| werden Kombinatorik-Formeln zu "
         "konkreten Wahrscheinlichkeiten – z. B. beim Lotto."),
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

    page_number(slide, 16)
    set_notes(slide, "Jede Person spricht ihren eigenen Takeaway in 1-2 Sätzen, Reihenfolge A→B→C. "
              "Diese drei Sätze sind die Kernbotschaften für die Matura.")
    return slide


# ---------------------------------------------------------------------------
# Slide 17 – Quellen
# ---------------------------------------------------------------------------

def slide_17_quellen(prs):
    slide = new_slide(prs)
    add_title_bar(slide, "Quellen", person="Alle", kicker="Verwendete Materialien")

    add_bullets(slide, [
        "BMBWF – Lehrplan & Formelsammlung Angewandte Mathematik (AHS/BHS)",
        "Schulbuch Angewandte Mathematik (Titel/Verlag bitte ergänzen)",
        "mathe-online.at – Kombinatorik & Wahrscheinlichkeitsrechnung",
        "Österreichische Lotterien – Spielregeln & Gewinnwahrscheinlichkeiten Lotto 6 aus 45",
        "Wikipedia – Permutation, Variation, Kombination, Laplace-Wahrscheinlichkeit (Stand: Juni 2026)",
        "Alle Diagramme und Formelgrafiken: selbst erstellt mit Python (matplotlib, python-pptx)",
    ], CONTENT_LEFT, CONTENT_TOP, CONTENT_W, Inches(5.0), size=Pt(20), space_after=Pt(18))

    page_number(slide, 17)
    set_notes(slide, "Diese Folie kurz zeigen (relevant für die Bewertung) – "
              "Schulbuch-Titel/Verlag vor Abgabe ergänzen.")
    return slide


# ---------------------------------------------------------------------------
# Slide 18 – Danke / Fragen
# ---------------------------------------------------------------------------

def slide_18_danke(prs):
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

    set_notes(slide, "Alle drei bedanken sich gemeinsam und stehen für Fragen bereit. "
              "Falls keine Fragen: 'Was war eure überraschendste Zahl heute?'")
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
    slide_05_variation(prs)
    slide_06_kombination(prs)
    slide_07_pascal(prs)
    slide_08_laplace(prs)
    slide_09_lotto(prs)
    slide_10_spiel_intro(prs)
    slide_11_runde1_frage(prs)
    slide_12_runde1_aufloesung(prs)
    slide_13_runde2_frage(prs)
    slide_14_runde2_aufloesung(prs)
    slide_15_uebersicht(prs)
    slide_16_zusammenfassung(prs)
    slide_17_quellen(prs)
    slide_18_danke(prs)

    return prs


if __name__ == "__main__":
    prs = build()
    out_path = os.path.join(os.path.dirname(__file__), "kombinatorik_praesentation.pptx")
    prs.save(out_path)
    print(f"Saved {out_path} — {len(prs.slides._sldIdLst)} slides")
