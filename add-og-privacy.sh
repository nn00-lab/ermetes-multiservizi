#!/bin/bash

file="privacy.html"

schema='
<meta property="og:type" content="website">
<meta property="og:title" content="Privacy Policy | Ermetes Società Cooperativa Sociale Trento">
<meta property="og:description" content="Informativa privacy e trattamento dei dati personali del sito Ermetes.">
<meta property="og:image" content="https://www.ermetes.it/assets/hero/hero-ermetes.webp">
<meta property="og:url" content="https://www.ermetes.it/privacy.html">
<meta property="og:locale" content="it_IT">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Privacy Policy | Ermetes Società Cooperativa Sociale Trento">
<meta name="twitter:description" content="Informativa privacy e trattamento dei dati personali del sito Ermetes.">
<meta name="twitter:image" content="https://www.ermetes.it/assets/hero/hero-ermetes.webp">
'

python3 - "$file" "$schema" <<'PY'
import sys

file=sys.argv[1]
schema=sys.argv[2]

with open(file) as f:
    txt=f.read()

txt=txt.replace("</head>", schema+"\n</head>")

with open(file,"w") as f:
    f.write(txt)
PY

echo "Aggiornato: $file"
