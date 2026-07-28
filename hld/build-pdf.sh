#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT="$SCRIPT_DIR/HLD-System-Design-Book.pdf"

COMBINED=$(mktemp /tmp/hld-combined-XXXXXX.md)
trap 'rm -f "$COMBINED"' EXIT

cat > "$COMBINED" <<'FRONTMATTER'
---
title: "High-Level System Design"
subtitle: "Interview Preparation Guide"
author: "System Design Notes"
date: \today
documentclass: report
papersize: a4
fontsize: 11pt
geometry:
  - top=25mm
  - bottom=25mm
  - left=20mm
  - right=20mm
mainfont: "Helvetica Neue"
monofont: "Fira Code"
monofontoptions:
  - Scale=0.72
header-includes:
  - |
    ```{=latex}
    \usepackage{fancyhdr}
    \usepackage{titlesec}
    \usepackage{xcolor}

    \definecolor{chaptercolor}{HTML}{2C3E50}
    \definecolor{sectioncolor}{HTML}{34495E}

    \titleformat{\chapter}[display]
      {\normalfont\huge\bfseries\color{chaptercolor}}
      {\chaptertitlename\ \thechapter}{20pt}{\Huge}
    \titleformat{\section}
      {\normalfont\Large\bfseries\color{sectioncolor}}
      {\thesection}{1em}{}
    \titleformat{\subsection}
      {\normalfont\large\bfseries\color{sectioncolor}}
      {\thesubsection}{1em}{}

    \pagestyle{fancy}
    \fancyhf{}
    \fancyhead[L]{\leftmark}
    \fancyhead[R]{\thepage}
    \fancyfoot[C]{\footnotesize High-Level System Design}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.2pt}

    \widowpenalty=10000
    \clubpenalty=10000

    \setcounter{tocdepth}{2}
    \setlength{\parskip}{0.5em}
    ```
toc: true
toc-depth: 2
colorlinks: true
linkcolor: "sectioncolor"
urlcolor: "blue"
---

FRONTMATTER

first=true
for f in "$SCRIPT_DIR"/[0-9]*.md; do
  echo "" >> "$COMBINED"
  echo "\\newpage" >> "$COMBINED"
  echo "" >> "$COMBINED"
  cat "$f" >> "$COMBINED"
  echo "" >> "$COMBINED"
done

echo "Building PDF..."
pandoc "$COMBINED" \
  -o "$OUTPUT" \
  --pdf-engine=xelatex \
  --lua-filter="$SCRIPT_DIR/keep-code-together.lua" \
  --toc \
  --number-sections \
  -V lang=en \
  --wrap=preserve \
  2>&1

echo ""
echo "Done! PDF saved to: $OUTPUT"
echo "Size: $(du -h "$OUTPUT" | cut -f1)"
