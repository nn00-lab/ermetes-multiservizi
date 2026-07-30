#!/bin/bash

for file in $(find . -name "*.html" | grep -v backup-og); do

if grep -q 'property="og:title"' "$file"; then
    echo "Già presente: $file"
    continue
fi

title=$(python3 - <<PY
from bs4 import BeautifulSoup
soup=BeautifulSoup(open("$file").read(),"html.parser")
print(soup.title.text.strip() if soup.title else "")
PY
)

description=$(python3 - <<PY
from bs4 import BeautifulSoup
soup=BeautifulSoup(open("$file").read(),"html.parser")
m=soup.find("meta",attrs={"name":"description"})
print(m.get("content","").strip() if m else "")
PY
)

cat > /tmp/og.txt <<EOF

<meta property="og:type" content="website">

<meta property="og:title" content="$title">

<meta property="og:description" content="$description">

<meta property="og:image" content="https://www.ermetes.it/assets/hero/hero-ermetes.webp">

<meta property="og:locale" content="it_IT">

<meta name="twitter:card" content="summary_large_image">

<meta name="twitter:title" content="$title">

<meta name="twitter:description" content="$description">

<meta name="twitter:image" content="https://www.ermetes.it/assets/hero/hero-ermetes.webp">

EOF


python3 - "$file" /tmp/og.txt <<'PY'
import sys

file=sys.argv[1]
block=open(sys.argv[2]).read()

txt=open(file).read()

txt=txt.replace("</head>", block+"\n</head>")

open(file,"w").write(txt)
PY

echo "Aggiornato: $file"

done
