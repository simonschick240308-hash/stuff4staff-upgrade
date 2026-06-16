"""Generate all formula renders and illustrations used by build_presentation.py.

Run with: python3 generate_assets.py
Outputs PNG files into ./assets/
"""

import os
from math import comb

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon

from theme import (
    HEX_DEEP_BLUE, HEX_MID_BLUE, HEX_LIGHT_BLUE, HEX_ORANGE, HEX_YELLOW,
    HEX_DARK, HEX_GRAY, HEX_WHITE, HEX_BG, HEX_RED, HEX_BROWN,
)

ASSETS = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS, exist_ok=True)

plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"


def path(name):
    return os.path.join(ASSETS, name)


# ---------------------------------------------------------------------------
# Formula renders (matplotlib mathtext -> tightly cropped transparent PNG)
# ---------------------------------------------------------------------------

FORMULAS = {
    "f_zaehlprinzip": r"n_1 \cdot n_2 \cdot \ldots \cdot n_k",
    "f_permutation_ohne": r"P(n) = n!",
    "f_permutation_mit": r"P(n;\,k_1,\ldots,k_j) = \dfrac{n!}{k_1!\cdot k_2! \cdots k_j!}",
    "f_variation_ohne": r"V(n,k) = \dfrac{n!}{(n-k)!}",
    "f_variation_mit": r"V_W(n,k) = n^{\,k}",
    "f_kombination_ohne": r"C(n,k) = \binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}",
    "f_kombination_mit": r"C_W(n,k) = \binom{n+k-1}{k}",
    "f_laplace": r"P(A) = \dfrac{|A|}{|\Omega|}",
    "f_pasch": r"P(\mathrm{Pasch}) = \dfrac{6}{36} = \dfrac{1}{6}",
    "f_lotto_komb": r"\binom{45}{6} = 8\,145\,060",
    "f_lotto_prob": r"P(\mathrm{6\ Richtige}) = \dfrac{1}{8\,145\,060} \approx 0{,}0000123\,\%",
    "f_aufgabe1_loesung": r"3 \cdot 5 \cdot 2 = 30",
    "f_aufgabe1b_loesung": r"6! = 720",
    "f_aufgabe2_loesung": r"V(10,3) = \dfrac{10!}{7!} = 720",
    "f_aufgabe2b_loesung": r"\binom{7}{3} = 35",
    "f_aufgabe3_loesung": r"\dfrac{\binom{4}{2}}{\binom{10}{2}} = \dfrac{6}{45} = \dfrac{2}{15} \approx 13{,}3\,\%",
    "f_pascal_link": r"\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}",
    "f_beispiel_outfits": r"3 \cdot 4 \cdot 2 = 24",
    "f_beispiel_5fakultaet": r"5! = 120",
    "f_beispiel_ananas": r"\dfrac{6!}{3!\cdot 2!\cdot 1!} = 60",
    "f_beispiel_stockerl": r"V(8,3) = \dfrac{8!}{5!} = 336",
    "f_beispiel_pin": r"V_W(10,4) = 10^4 = 10\,000",
    "f_beispiel_eis": r"C_W(5,3) = \binom{7}{3} = 35",
    "f_beispiel_pascal_62": r"\binom{6}{2} = 15",
    "f_handshake": r"\binom{15}{2} = \dfrac{15!}{2!\cdot 13!} = 105",
    "f_klasse_perm": r"15! = 1\,307\,674\,368\,000 \approx 1{,}3 \times 10^{12}",
    "f_kartenspiel": r"52! \approx 8{,}07 \times 10^{67}",
}


def render_formula(tex, filename, fontsize=34, color=HEX_DEEP_BLUE):
    fig = plt.figure(figsize=(0.1, 0.1))
    fig.patch.set_alpha(0.0)
    fig.text(0, 0, f"${tex}$", fontsize=fontsize, color=color)
    fig.savefig(path(filename), dpi=300, bbox_inches="tight", pad_inches=0.06, transparent=True)
    plt.close(fig)


def generate_formulas():
    for name, tex in FORMULAS.items():
        render_formula(tex, f"{name}.png")
    print(f"Generated {len(FORMULAS)} formula images")


# ---------------------------------------------------------------------------
# Pascal's triangle
# ---------------------------------------------------------------------------

def pascal_triangle(filename="pascal_triangle.png", rows=8, highlight=(6, 2)):
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    for n in range(rows + 1):
        for k in range(n + 1):
            x = k - n / 2
            y = -n
            val = comb(n, k)
            is_hl = (n, k) == highlight
            face = HEX_ORANGE if is_hl else HEX_LIGHT_BLUE
            edge = HEX_ORANGE if is_hl else HEX_MID_BLUE
            txt_color = HEX_WHITE if is_hl else HEX_DEEP_BLUE
            r = 0.46
            circ = Circle((x, y), r, facecolor=face, edgecolor=edge, lw=1.6, zorder=2)
            ax.add_patch(circ)
            fs = 13 if val < 100 else (10 if val < 1000 else 8)
            ax.text(x, y, str(val), ha="center", va="center", fontsize=fs,
                    color=txt_color, fontweight="bold", zorder=3, family="sans-serif")
    ax.set_xlim(-rows / 2 - 0.7, rows / 2 + 0.7)
    ax.set_ylim(-rows - 0.7, 0.7)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Dice grid (sample space for two dice, Pasch diagonal highlighted)
# ---------------------------------------------------------------------------

PIP_LAYOUT = {
    1: [(0, 0)],
    2: [(-0.27, 0.27), (0.27, -0.27)],
    3: [(-0.27, 0.27), (0, 0), (0.27, -0.27)],
    4: [(-0.27, 0.27), (0.27, 0.27), (-0.27, -0.27), (0.27, -0.27)],
    5: [(-0.27, 0.27), (0.27, 0.27), (0, 0), (-0.27, -0.27), (0.27, -0.27)],
    6: [(-0.27, 0.27), (0.27, 0.27), (-0.27, 0), (0.27, 0), (-0.27, -0.27), (0.27, -0.27)],
}


def draw_die(ax, cx, cy, value, size=0.8, face=HEX_WHITE, edge=HEX_DEEP_BLUE, pip=HEX_DEEP_BLUE):
    box = FancyBboxPatch((cx - size / 2, cy - size / 2), size, size,
                          boxstyle=f"round,pad=0,rounding_size={size * 0.14}",
                          facecolor=face, edgecolor=edge, lw=1.3, zorder=2)
    ax.add_patch(box)
    for dx, dy in PIP_LAYOUT[value]:
        ax.add_patch(Circle((cx + dx * size, cy + dy * size), size * 0.085,
                             color=pip, zorder=3))


def dice_grid(filename="dice_grid.png"):
    fig, ax = plt.subplots(figsize=(6.4, 6.4))
    n = 6
    cell = 1.0
    # Header row (top) and column (left) showing die faces 1-6
    for j in range(n):
        draw_die(ax, j + 1.5, n + 1.0, j + 1, size=0.7)
    for i in range(n):
        draw_die(ax, 0.5, n - i, i + 1, size=0.7)

    for i in range(n):  # row = first die
        for j in range(n):  # col = second die
            x = j + 1
            y = n - i - 1
            is_pasch = i == j
            face = HEX_ORANGE if is_pasch else HEX_LIGHT_BLUE
            edge = HEX_ORANGE if is_pasch else HEX_MID_BLUE
            rect = Rectangle((x, y), cell * 0.94, cell * 0.94, facecolor=face,
                              edgecolor=edge, lw=1.2, zorder=1)
            ax.add_patch(rect)

    ax.set_xlim(-0.1, n + 1.6)
    ax.set_ylim(-0.1, n + 1.6)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Lotto balls
# ---------------------------------------------------------------------------

def lotto_balls(filename="lotto_balls.png", numbers=(4, 11, 19, 23, 30, 42)):
    fig, ax = plt.subplots(figsize=(8, 1.6))
    for idx, num in enumerate(numbers):
        x = idx * 1.2
        # shadow
        ax.add_patch(Circle((x + 0.05, -0.07), 0.5, color="#00000022", zorder=1))
        ax.add_patch(Circle((x, 0), 0.5, facecolor=HEX_ORANGE, edgecolor=HEX_DEEP_BLUE,
                             lw=1.5, zorder=2))
        ax.add_patch(Circle((x - 0.13, 0.13), 0.16, facecolor=HEX_YELLOW, alpha=0.55,
                             edgecolor="none", zorder=3))
        ax.text(x, 0, str(num), ha="center", va="center", fontsize=20,
                color=HEX_WHITE, fontweight="bold", zorder=4, family="sans-serif")
    ax.set_xlim(-0.7, (len(numbers) - 1) * 1.2 + 0.7)
    ax.set_ylim(-0.7, 0.7)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Podium (Stockerlplatz)
# ---------------------------------------------------------------------------

def podium(filename="podium.png"):
    fig, ax = plt.subplots(figsize=(6, 4.2))
    bars = [
        (0, 1.4, 1.6, HEX_MID_BLUE, "2"),
        (1.6, 0, 2.2, HEX_ORANGE, "1"),
        (3.2, 2.0, 1.0, HEX_LIGHT_BLUE, "3"),
    ]
    for x, y0, h, color, label in bars:
        ax.add_patch(Rectangle((x, 0), 1.5, h, facecolor=color, edgecolor=HEX_DEEP_BLUE, lw=1.5, zorder=2))
        ax.text(x + 0.75, h + 0.18, label, ha="center", va="bottom", fontsize=26,
                color=HEX_DEEP_BLUE, fontweight="bold", family="sans-serif", zorder=3)
        ax.add_patch(Circle((x + 0.75, h + 0.75), 0.32, facecolor=HEX_WHITE,
                             edgecolor=HEX_DEEP_BLUE, lw=1.3, zorder=3))
    ax.set_xlim(-0.3, 4.8)
    ax.set_ylim(0, 3.4)
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Ice cream cup (Kombination mit Wiederholung)
# ---------------------------------------------------------------------------

def icecream(filename="icecream.png"):
    fig, ax = plt.subplots(figsize=(3.2, 4.2))
    # cone
    cone = Polygon([(-0.6, -2.0), (0.6, -2.0), (0, -3.6)], closed=True,
                    facecolor=HEX_BROWN, edgecolor=HEX_DEEP_BLUE, lw=1.3, zorder=1)
    ax.add_patch(cone)
    # waffle lines
    for k in range(1, 4):
        ax.plot([-0.6 + k * 0.05, 0.6 - k * 0.05], [-2.0 - k * 0.4, -2.0 - k * 0.4],
                color=HEX_DEEP_BLUE, lw=0.6, alpha=0.4, zorder=2)
    # scoops
    scoop_colors = [HEX_ORANGE, HEX_YELLOW, HEX_BROWN]
    centers = [(0, -1.2), (-0.55, -0.4), (0.55, -0.4)]
    for (cx, cy), color in zip(centers, scoop_colors):
        ax.add_patch(Circle((cx, cy), 0.75, facecolor=color, edgecolor=HEX_DEEP_BLUE, lw=1.3, zorder=3))
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-3.8, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Urn with red/blue balls (Aufgabe Teil 3)
# ---------------------------------------------------------------------------

def urn(filename="urn.png"):
    import random
    rnd = random.Random(42)
    fig, ax = plt.subplots(figsize=(4, 4))
    # urn body (trapezoid)
    body = Polygon([(-1.6, 2.2), (1.6, 2.2), (1.1, -1.8), (-1.1, -1.8)], closed=True,
                    facecolor=HEX_LIGHT_BLUE, edgecolor=HEX_DEEP_BLUE, lw=2, zorder=1)
    ax.add_patch(body)
    # rim
    ax.add_patch(Rectangle((-1.75, 2.2), 3.5, 0.28, facecolor=HEX_MID_BLUE, edgecolor=HEX_DEEP_BLUE, lw=1.5, zorder=2))

    balls = [HEX_RED] * 4 + [HEX_MID_BLUE] * 6
    rnd.shuffle(balls)
    placed = []
    for color in balls:
        for _ in range(200):
            x = rnd.uniform(-1.0, 1.0)
            y = rnd.uniform(-1.6, 1.9)
            # keep inside trapezoid roughly
            width_at_y = 1.6 - (2.2 - y) / 4.0 * 0.5
            if abs(x) > width_at_y - 0.28:
                continue
            if all((x - px) ** 2 + (y - py) ** 2 > 0.30 ** 2 for px, py in placed):
                placed.append((x, y))
                ax.add_patch(Circle((x, y), 0.27, facecolor=color, edgecolor=HEX_DEEP_BLUE, lw=1, zorder=3))
                break
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.1, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Outfit grid (Zaehlprinzip): 3 Hemden x 4 Hosen color-coded grid
# ---------------------------------------------------------------------------

def outfit_grid(filename="outfit_grid.png"):
    shirt_colors = [HEX_DEEP_BLUE, HEX_ORANGE, HEX_YELLOW]
    pants_colors = [HEX_MID_BLUE, HEX_GRAY, HEX_BROWN, HEX_DARK]
    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    cell = 1.0
    for i, sc in enumerate(shirt_colors):  # rows = Hemden
        for j, pc in enumerate(pants_colors):  # cols = Hosen
            x, y = j, len(shirt_colors) - 1 - i
            ax.add_patch(Rectangle((x, y + 0.5), cell * 0.9, cell * 0.42, facecolor=sc,
                                    edgecolor=HEX_DEEP_BLUE, lw=1, zorder=2))
            ax.add_patch(Rectangle((x, y), cell * 0.9, cell * 0.42, facecolor=pc,
                                    edgecolor=HEX_DEEP_BLUE, lw=1, zorder=2))
            ax.add_patch(Rectangle((x, y), cell * 0.9, cell * 0.92, facecolor="none",
                                    edgecolor=HEX_DEEP_BLUE, lw=1.4, zorder=3))
    ax.set_xlim(-0.3, (len(pants_colors) - 1) + 0.9 + 0.3)
    ax.set_ylim(-0.3, (len(shirt_colors) - 1) + 0.92 + 0.3)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Permutation tree (3 Freunde -> 3! = 6 Reihenfolgen)
# ---------------------------------------------------------------------------

def permutation_tree(filename="permutation_tree.png"):
    fig, ax = plt.subplots(figsize=(9, 4.6))
    names = ["A", "B", "C"]
    root = (0, 3)
    level1_y = 1.8
    level2_y = 0.4
    level1_x = [-3, 0, 3]

    leaves = []
    for i, n1 in enumerate(names):
        x1 = level1_x[i]
        ax.plot([root[0], x1], [root[1], level1_y], color=HEX_GRAY, lw=1.4, zorder=1)
        ax.add_patch(Circle((x1, level1_y), 0.32, facecolor=HEX_LIGHT_BLUE, edgecolor=HEX_DEEP_BLUE, lw=1.3, zorder=2))
        ax.text(x1, level1_y, n1, ha="center", va="center", fontsize=13, fontweight="bold",
                color=HEX_DEEP_BLUE, zorder=3, family="sans-serif")

        remaining = [n for n in names if n != n1]
        offsets = [-0.9, 0.9]
        for off, n2 in zip(offsets, remaining):
            x2 = x1 + off
            ax.plot([x1, x2], [level1_y, level2_y], color=HEX_GRAY, lw=1.4, zorder=1)
            ax.add_patch(Circle((x2, level2_y), 0.32, facecolor=HEX_LIGHT_BLUE, edgecolor=HEX_DEEP_BLUE, lw=1.3, zorder=2))
            ax.text(x2, level2_y, n2, ha="center", va="center", fontsize=13, fontweight="bold",
                    color=HEX_DEEP_BLUE, zorder=3, family="sans-serif")
            n3 = [n for n in names if n not in (n1, n2)][0]
            leaf_label = f"{n1}{n2}{n3}"
            leaves.append((x2, leaf_label))

    for x2, label in leaves:
        y3 = -0.9
        ax.plot([x2, x2], [level2_y, y3], color=HEX_GRAY, lw=1.4, zorder=1)
        box = FancyBboxPatch((x2 - 0.5, y3 - 0.32), 1.0, 0.64, boxstyle="round,pad=0,rounding_size=0.08",
                              facecolor=HEX_ORANGE, edgecolor=HEX_DEEP_BLUE, lw=1.2, zorder=2)
        ax.add_patch(box)
        ax.text(x2, y3, label, ha="center", va="center", fontsize=12, fontweight="bold",
                color=HEX_WHITE, zorder=3, family="sans-serif")

    ax.add_patch(Circle(root, 0.34, facecolor=HEX_DEEP_BLUE, edgecolor=HEX_DEEP_BLUE, lw=1.3, zorder=2))
    ax.text(root[0], root[1], "Start", ha="center", va="center", fontsize=10, fontweight="bold",
            color=HEX_WHITE, zorder=3, family="sans-serif")

    ax.set_xlim(-4.6, 4.6)
    ax.set_ylim(-1.5, 3.6)
    ax.axis("off")
    fig.savefig(path(filename), dpi=200, bbox_inches="tight", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Factorial growth bar chart
# ---------------------------------------------------------------------------

def factorial_growth(filename="factorial_growth.png"):
    import math
    ns = list(range(1, 7))
    vals = [math.factorial(n) for n in ns]
    fig, ax = plt.subplots(figsize=(7, 4))
    colors = [HEX_LIGHT_BLUE, HEX_LIGHT_BLUE, HEX_MID_BLUE, HEX_MID_BLUE, HEX_ORANGE, HEX_ORANGE]
    bars = ax.bar([str(n) for n in ns], vals, color=colors, edgecolor=HEX_DEEP_BLUE, linewidth=1.3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:,}".replace(",", "."), ha="center",
                va="bottom", fontsize=11, fontweight="bold", color=HEX_DEEP_BLUE, family="sans-serif")
    ax.set_xlabel("n", fontsize=13, color=HEX_DEEP_BLUE, family="sans-serif")
    ax.set_ylabel("n!", fontsize=13, color=HEX_DEEP_BLUE, family="sans-serif")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["bottom", "left"]].set_color(HEX_GRAY)
    ax.tick_params(colors=HEX_DEEP_BLUE)
    fig.tight_layout()
    fig.savefig(path(filename), dpi=200, transparent=True)
    plt.close(fig)


if __name__ == "__main__":
    generate_formulas()
    pascal_triangle()
    dice_grid()
    lotto_balls()
    podium()
    icecream()
    urn()
    outfit_grid()
    permutation_tree()
    factorial_growth()
    print("All assets generated in", ASSETS)
