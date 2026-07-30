#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil
import re


FILE = Path("index.html")


backup = Path(
    f"backup-home-template-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
)

backup.mkdir(exist_ok=True)

shutil.copy(FILE, backup / FILE.name)

print("Backup creato:", backup)


text = FILE.read_text(encoding="utf-8")


# 1) hero testo
old = """
<div class="wrap hero__grid">


<div>
"""

new = """
<div class="wrap hero__grid">


<div class="hero__copy">
"""


if old in text:
    text = text.replace(old, new, 1)
    print("Aggiornato hero__copy")
else:
    print("hero__copy già presente")


# 2) immagine
old_img = """
<div class="hero__image">
"""

new_img = """
<div class="hero-image">
"""


if old_img in text:
    text = text.replace(old_img, new_img, 1)
    print("Aggiornato hero-image")
else:
    print("hero-image già corretto")


FILE.write_text(text, encoding="utf-8")


print("Completato")
