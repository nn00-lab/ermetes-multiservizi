#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

ROOT = "."
CSS = "css/style.css"

backup = f"backup-menu-fix-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

print("=== ERMETES MENU FINAL FIX ===")

# backup
os.makedirs(backup, exist_ok=True)

if os.path.exists(CSS):
    shutil.copy2(CSS, backup + "/style.css")

for f in ["index.html", "servizi/index.html"]:
    if os.path.exists(f):
        os.makedirs(backup + "/" + os.path.dirname(f), exist_ok=True)
        shutil.copy2(f, backup + "/" + f)


print("Backup:", backup)


# ----------------------------
# FIX CSS
# ----------------------------

with open(CSS, "r", encoding="utf-8") as f:
    css = f.read()


# elimina vecchio blocco mobile menu nascosto
old = """
@media(max-width:900px){

.menu{

display:none !important;

}

}
"""

css = css.replace(old, "")


# aggiunge fix definitivo
fix = """

/* ==============================
   ERMETES FINAL MENU REPAIR
============================== */

.topbar{
    overflow:visible !important;
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
    justify-content:center !important;
    gap:32px !important;
    visibility:visible !important;
    opacity:1 !important;
    position:relative !important;
    z-index:9999 !important;
}


.menu a{
    display:inline-block !important;
    visibility:visible !important;
    opacity:1 !important;
}


.menu-item{
    position:relative !important;
    display:block !important;
}


.dropdown{
    position:absolute !important;
    top:100% !important;
    left:0 !important;
    background:white !important;
    display:none;
    z-index:99999 !important;
}


.menu-item:hover .dropdown{
    display:block !important;
}


.header-actions{
    display:flex !important;
    align-items:center !important;
    visibility:visible !important;
    opacity:1 !important;
}


@media(max-width:900px){

.menu{
    display:flex !important;
}

}
"""


if "ERMETES FINAL MENU REPAIR" not in css:
    css += fix


with open(CSS, "w", encoding="utf-8") as f:
    f.write(css)


print("CSS sistemato")


# ----------------------------
# pulizia backup analisi
# ----------------------------

ignore = [
    "backup-",
    ".git"
]

print("\nAnalisi pagine:")

for root, dirs, files in os.walk("."):
    dirs[:] = [
        d for d in dirs
        if not any(d.startswith(x) for x in ignore)
    ]

    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root,file)

            try:
                data=open(path,encoding="utf-8").read()

                problemi=[]

                if '<nav class="menu">' not in data:
                    problemi.append("MENU")

                if '/css/style.css' not in data:
                    problemi.append("CSS")

                if problemi:
                    print(path, ":", ",".join(problemi))

            except:
                pass


print("""
=== COMPLETATO ===

Backup:
""", backup)

print("Ora fai CTRL+SHIFT+R nel browser")
