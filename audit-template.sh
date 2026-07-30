#!/bin/bash

echo "=== HEADER HOME ==="
grep -n "<header\|<nav\|menu\|logo" index.html

echo
echo "=== HEADER SERVIZI ==="
grep -n "<header\|<nav\|menu\|logo" servizi/index.html


echo
echo "=== CLASSI CSS HOME ==="
grep -o 'class="[^"]*"' index.html | sort | uniq > home-classi.txt

echo
echo "=== CLASSI CSS SERVIZI ==="
grep -o 'class="[^"]*"' servizi/index.html | sort | uniq > servizi-classi.txt


echo
echo "=== DIFFERENZE CLASSI ==="
diff -u home-classi.txt servizi-classi.txt


echo
echo "=== GOOGLE FONT ==="
grep -R "fonts.googleapis" -n index.html servizi/index.html


echo
echo "=== STYLE INLINE ==="
grep -R "<style" -n index.html servizi/index.html


echo
echo "FINE AUDIT"
