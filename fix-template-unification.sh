#!/bin/bash

set -e

echo "=== FIX TEMPLATE ERMETES ==="

python3 <<'PY'

from pathlib import Path
import re


root = Path(".")


# -----------------------------
# estrazione header servizi
# -----------------------------

servizi = Path("servizi/index.html").read_text()

header_match = re.search(
    r'<header class="topbar">.*?</header>',
    servizi,
    re.S
)

if not header_match:
    raise Exception("Header servizi non trovato")

new_header = header_match.group(0)


# -----------------------------
# sostituzione header home
# -----------------------------

home = Path("index.html")

text = home.read_text()

old = re.search(
    r'<header class="topbar">.*?</header>',
    text,
    re.S
)

if old:
    text = text[:old.start()] + new_header + text[old.end():]

    home.write_text(text)

    print("Aggiornato header: index.html")


# -----------------------------
# uniforma google fonts
# -----------------------------

font_pattern = re.compile(
r'https://fonts\.googleapis\.com/css2\?[^"]+'
)


font_url = (
'https://fonts.googleapis.com/css2?'
'family=Inter:wght@400;500;600;700;800&'
'family=Fraunces:wght@600;700&'
'display=swap'
)


for file in root.rglob("*.html"):

    if "backup" in str(file):
        continue

    txt=file.read_text()

    new=font_pattern.sub(font_url, txt)

    if new != txt:
        file.write_text(new)
        print("Font aggiornati:", file)


print("=== COMPLETATO ===")

PY
