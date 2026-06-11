"""Shared color palette and fonts for the Kombinatorik presentation."""

from pptx.util import Pt
from pptx.dml.color import RGBColor

# Core palette: deep blue (structure) + orange/yellow (everyday examples)
DEEP_BLUE = RGBColor(0x1B, 0x3A, 0x5C)
MID_BLUE = RGBColor(0x3D, 0x6E, 0xA5)
LIGHT_BLUE = RGBColor(0xE8, 0xF1, 0xFA)
ORANGE = RGBColor(0xF2, 0x8C, 0x3C)
YELLOW = RGBColor(0xF6, 0xC8, 0x4C)
DARK = RGBColor(0x27, 0x30, 0x3A)
GRAY = RGBColor(0x8A, 0x96, 0xA6)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BG = RGBColor(0xFA, 0xFB, 0xFC)

# Hex strings (for matplotlib)
HEX_DEEP_BLUE = "#1B3A5C"
HEX_MID_BLUE = "#3D6EA5"
HEX_LIGHT_BLUE = "#E8F1FA"
HEX_ORANGE = "#F28C3C"
HEX_YELLOW = "#F6C84C"
HEX_DARK = "#27303A"
HEX_GRAY = "#8A96A6"
HEX_WHITE = "#FFFFFF"
HEX_BG = "#FAFBFC"

# Extra colors used only in diagram illustrations (e.g. urn, ice cream)
HEX_RED = "#D9534F"
HEX_BROWN = "#8B5E3C"

FONT_HEAD = "Calibri"
FONT_BODY = "Calibri"

TITLE_SIZE = Pt(34)
SUBTITLE_SIZE = Pt(20)
BODY_SIZE = Pt(18)
SMALL_SIZE = Pt(14)
LABEL_SIZE = Pt(13)
