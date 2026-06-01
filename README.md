# Stuff4Staff GmbH — Website

Modern, single-page website for **Stuff4Staff GmbH**, a German B2B staffing and HR company specialising in Personalvermittlung, Zeitarbeit, and HR-Beratung.

## Overview

A fully self-contained `index.html` with inline CSS and JavaScript. No build step required — just open the file in a browser or deploy the single file to any static host.

## Features

- **3D Hero Section** — Three.js scene with rotating icosahedron, torus, boxes, and a 700-particle field
- **Typewriter effect** in the hero headline cycling through service phrases
- **GSAP ScrollTrigger animations** — fade-in-up, slide-in-left/right, staggered cards
- **Parallax scrolling** — the 3D canvas shifts as you scroll
- **3D card tilt** — CSS perspective tilt on hover for service cards
- **Animated counters** — 500+, 10+, 200+, 98% triggered on scroll
- **Testimonials carousel** — auto-advances, swipeable on mobile, with dot navigation
- **Contact form** — validation, simulated submission with success state
- **Sticky glass-morphism navbar** — transparent on load, frosted-glass on scroll
- **Fully responsive** — mobile menu, responsive grid breakpoints
- **German language** throughout

## Tech Stack

| Library | Version | Purpose |
|---------|---------|---------|
| [Three.js](https://threejs.org/) | r134 | 3D hero scene |
| [GSAP](https://greensock.com/gsap/) | 3.12.2 | Scroll animations, tweens |
| [ScrollTrigger](https://greensock.com/scrolltrigger/) | 3.12.2 | Scroll-based triggers |
| [Inter](https://fonts.google.com/specimen/Inter) | — | Typography (Google Fonts) |

All libraries are loaded from CDN — no local dependencies.

## Usage

No build step needed. Simply serve `index.html` from any static host:

```bash
# Local preview with Python
python3 -m http.server 8080
# then open http://localhost:8080
```

Or deploy directly to Netlify, Vercel, GitHub Pages, or any web server.

## Sections

1. **Navbar** — sticky, glass-morphism, mobile burger menu
2. **Hero** — 3D Three.js background, typewriter headline, trust indicators
3. **Leistungen** — three service cards (Personalvermittlung, Zeitarbeit, HR Beratung) with 3D tilt
4. **Kennzahlen** — animated stats bar (500+ Mitarbeiter, 10+ Jahre, 200+ Kunden, 98%)
5. **Über uns** — two-column layout with SVG team illustration and floating badges
6. **Referenzen** — auto-playing testimonials carousel (5 cards)
7. **Kontakt** — contact details + validated form with success state
8. **Footer** — brand, links, social icons, legal

## Colour Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--navy` | `#0a0e27` | Page background |
| `--navy-mid` | `#111535` | Cards, footer |
| `--blue` | `#4f8ef7` | Primary accent |
| `--blue-light` | `#7ab4ff` | Gradient end, hovers |
| `--muted` | `#8a96b8` | Secondary text |
