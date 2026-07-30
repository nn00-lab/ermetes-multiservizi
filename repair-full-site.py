#!/usr/bin/env python3

import os
import re
import shutil
from datetime import datetime


ROOT="."
CSS="css/style.css"

STAMP=datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP=f"backup-auto-repair-{STAMP}"


print("=== ERMETES FULL SITE REPAIR ===")


# -----------------------------
# BACKUP
# -----------------------------

os.makedirs(BACKUP,exist_ok=True)

for root,dirs,files in os.walk("."):
    if BACKUP in root:
        continue

    for f in files:
        if f.endswith(".html") or f.endswith(".css"):
            src=os.path.join(root,f)
            dst=os.path.join(BACKUP,src)
            os.makedirs(os.path.dirname(dst),exist_ok=True)
            shutil.copy2(src,dst)


print("Backup creato:",BACKUP)



# -----------------------------
# ANALISI HTML
# -----------------------------

html=[]

for root,dirs,files in os.walk("."):

    if BACKUP in root:
        continue

    for f in files:
        if f.endswith(".html"):
            html.append(os.path.join(root,f))


print("\nPagine trovate:",len(html))


for f in html:

    data=open(f,encoding="utf8").read()

    if '<nav class="menu">' not in data:
        print("MENU ASSENTE:",f)


    if '/css/style.css' not in data:
        print("CSS MANCANTE:",f)



# -----------------------------
# NORMALIZZA FONT
# -----------------------------


FONT='''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:wght@600;700&display=swap" rel="stylesheet">'''


for f in html:

    data=open(f,encoding="utf8").read()

    data=re.sub(
        r'<link rel="preconnect".*?display=swap".*?>',
        FONT,
        data,
        flags=re.S
    )

    open(f,"w",encoding="utf8").write(data)

    print("Font:",f)



# -----------------------------
# CSS HEADER FIX
# -----------------------------


if os.path.exists(CSS):

    with open(CSS,encoding="utf8") as f:
        css=f.read()


    css += """



/* ================================
 AUTOMATIC HEADER REPAIR
================================ */


.topbar{
width:100%;
}


.topbar__row{

display:flex !important;
align-items:center !important;
justify-content:space-between !important;
gap:30px !important;

}


.menu{

display:flex !important;
align-items:center !important;
gap:32px !important;
visibility:visible !important;
opacity:1 !important;

}


.menu a{

display:block !important;

}


.menu-item{

position:relative;

}


.dropdown{

position:absolute;
top:100%;
left:0;
z-index:9999;

background:white;

}


.menu-item:hover .dropdown{

display:flex;

flex-direction:column;

}

"""


    with open(CSS,"w",encoding="utf8") as f:
        f.write(css)


    print("CSS riparato")



# -----------------------------
# REPORT
# -----------------------------


with open("repair-report.txt","w") as f:

    f.write("ERMETES AUTOMATIC REPAIR\n\n")

    for p in html:
        f.write(p+"\n")


print()
print("=== COMPLETATO ===")
print("Backup:",BACKUP)
print("Report: repair-report.txt")
