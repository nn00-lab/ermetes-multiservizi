#!/usr/bin/env python3

import os
import shutil
from datetime import datetime


ROOT="."
CSS="css/style.css"

stamp=datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP=f"backup-complete-repair-{stamp}"

os.makedirs(BACKUP,exist_ok=True)

print("=== ERMETES COMPLETE REPAIR ===")


# backup
for root,dirs,files in os.walk(ROOT):
    dirs[:]=[
        d for d in dirs
        if not d.startswith("backup")
        and d!=".git"
    ]

    for f in files:
        if f.endswith(".html") or f.endswith(".css"):
            src=os.path.join(root,f)
            dst=os.path.join(BACKUP,src)
            os.makedirs(os.path.dirname(dst),exist_ok=True)
            shutil.copy2(src,dst)


print("Backup:",BACKUP)



html=[]

for root,dirs,files in os.walk(ROOT):

    dirs[:]=[
        d for d in dirs
        if not d.startswith("backup")
        and d!=".git"
    ]

    for f in files:
        if f.endswith(".html"):
            html.append(os.path.join(root,f))


report=[]


for f in html:

    data=open(f,encoding="utf8").read()

    if '<nav class="menu">' not in data:
        report.append("MENU MANCANTE "+f)

    if '/css/style.css' not in data:
        report.append("CSS MANCANTE "+f)

    if 'fonts.googleapis.com' in data:
        report.append("FONT PRESENTE "+f)

    if 'hero__image' in data:
        report.append("VECCHIA HERO IMAGE "+f)

    if 'hero-image' in data:
        report.append("OK HERO IMAGE "+f)



# CSS repair

if os.path.exists(CSS):

    css=open(CSS,encoding="utf8").read()


    repair=r'''

/* =====================================================
   ERMETES FINAL HEADER SYSTEM REPAIR
===================================================== */


.topbar{
position:relative;
z-index:1000;
}


.topbar__row{

display:flex;
align-items:center;
justify-content:space-between;

}


.menu{

display:flex !important;
align-items:center;
gap:32px;

visibility:visible !important;
opacity:1 !important;

}


.menu a{

display:inline-block;
text-decoration:none;

}


.menu-item{

position:relative;

}


.dropdown{

position:absolute;

top:100%;
left:0;

min-width:240px;

background:white;

padding:15px;

border-radius:12px;

box-shadow:
0 10px 30px rgba(0,0,0,.15);


display:none;

z-index:9999;

}


.dropdown a{

display:block;

padding:10px;

}


.menu-item:hover .dropdown{

display:block;

}



@media(max-width:900px){

.menu{

display:none !important;

}

}

'''

    css += repair

    open(CSS,"w",encoding="utf8").write(css)

    print("CSS HEADER REPAIRED")



open("repair-final-report.txt","w",encoding="utf8").write(
"\n".join(report)
)


print("")
print("=== COMPLETATO ===")
print("Backup:",BACKUP)
print("Report: repair-final-report.txt")
print("Problemi trovati:",len(report))
