#!/bin/bash


MENU='
<nav class="menu">

<a href="/">
Home
</a>

<div class="menu-item">

<a href="/servizi/">
Servizi
</a>

<div class="dropdown">

<a href="/servizi/pulizie-uffici-trento.html">
Pulizie uffici
</a>

<a href="/servizi/pulizie-condomini-trento.html">
Pulizie condomini
</a>

<a href="/servizi/pulizie-post-cantiere-trento.html">
Post cantiere
</a>

<a href="/servizi/sanificazione.html">
Sanificazione
</a>

<a href="/servizi/tinteggiature.html">
Tinteggiature
</a>

<a href="/servizi/cartongesso.html">
Cartongesso
</a>

<a href="/servizi/manutenzioni.html">
Manutenzioni
</a>

<a href="/servizi/aree-verdi.html">
Aree verdi
</a>

</div>

</div>

<a href="/chi-siamo.html">
Chi siamo
</a>

<a href="/contatti.html">
Contatti
</a>

</nav>
'


FILES=$(find . -name "*.html")


for FILE in $FILES
do

python3 - <<EOF

from pathlib import Path
import re

path = Path("$FILE")

text = path.read_text()

new = '''$MENU'''

pattern = r'<nav class="menu">.*?</nav>'

text2 = re.sub(
    pattern,
    new,
    text,
    flags=re.S
)

if text != text2:
    path.write_text(text2)
    print("Aggiornato:", path)

EOF

done
