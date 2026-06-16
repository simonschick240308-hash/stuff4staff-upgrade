"""Shared color palette and fonts for the Kombinatorik presentation."""

from pptx.util import Pt
from pptx.dml.color import RGBColor

# Core palette: modern navy + vibrant electric blue + punchy orange
DEEP_BLUE = RGBColor(0x1E, 0x3A, 0x8A)   # blue-800
MID_BLUE = RGBColor(0x25, 0x63, 0xEB)    # blue-600 vivid
LIGHT_BLUE = RGBColor(0xEF, 0xF6, 0xFF)  # blue-50
ORANGE = RGBColor(0xEA, 0x58, 0x0C)      # orange-600 vibrant
YELLOW = RGBColor(0xFB, 0xBF, 0x24)      # amber-400
DARK = RGBColor(0x0F, 0x17, 0x2A)        # slate-900 near-black
GRAY = RGBColor(0x64, 0x74, 0x8B)        # slate-500
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BG = RGBColor(0xF0, 0xF4, 0xFF)          # blue-tinted off-white

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
