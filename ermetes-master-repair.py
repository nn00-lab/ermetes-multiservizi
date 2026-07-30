#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil
import re


ROOT = Path(".")
MASTER = ROOT / "index.html"
CSS = ROOT / "css/style.css"


STAMP = datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP = ROOT / f"backup-master-ui-{STAMP}"
REPORT = ROOT / "master-repair-report.txt"


log = []


def write_log(x):
    print(x)
    log.append(x)


print("=== ERMETES MASTER UI REPAIR ===")


# ======================
# BACKUP COMPLETO
# ======================

BACKUP.mkdir()

for item in ROOT.iterdir():

    if item.name.startswith("backup-"):
        continue

    if item.name == BACKUP.name:
        continue

    try:
        if item.is_dir():
            shutil.copytree(item, BACKUP / item.name)

        else:
            shutil.copy2(item, BACKUP / item.name)

    except:
        pass


write_log(f"Backup creato: {BACKUP}")


# ======================
# LEGGE HOME MASTER
# ======================

master = MASTER.read_text(encoding="utf-8")


# FONT MASTER

fonts = re.findall(
    r'<link[^>]+fonts\.googleapis[^>]+>',
    master
)

font_block = "\n".join(fonts)


# FOOTER MASTER

footer_match = re.search(
    r'<footer[\s\S]*?</footer>',
    master
)

footer = footer_match.group(0) if footer_match else ""


# ======================
# SISTEMA HTML
# ======================

for html in ROOT.rglob("*.html"):

    if "backup-" in str(html):
        continue

    if html == MASTER:
        continue


    text = html.read_text(encoding="utf-8")


    # CSS

    if "/css/style.css" not in text:

        text = text.replace(
            "</head>",
            '<link rel="stylesheet" href="/css/style.css">\n</head>'
        )

        write_log(
            f"CSS aggiunto: {html}"
        )


    # FONT

    text = re.sub(
        r'<link[^>]+fonts\.googleapis[^>]+>',
        '',
        text
    )


    if font_block:

        text = text.replace(
            "</head>",
            font_block + "\n</head>"
        )

        write_log(
            f"Font sincronizzato: {html}"
        )


    # FOOTER

    if footer:

        text = re.sub(
            r'<footer[\s\S]*?</footer>',
            footer,
            text
        )

        write_log(
            f"Footer sincronizzato: {html}"
        )


    html.write_text(
        text,
        encoding="utf-8"
    )


# ======================
# CSS MASTER UX
# ======================


css_fix = r"""


/* =====================================
 ERMETES MASTER UI SYSTEM
===================================== */


:root{

--green:#16805c;
--text:#182230;
--muted:#667085;
--border:#e4e7ec;
--bg:#ffffff;

}


body{

font-family:'Inter',sans-serif !important;
color:var(--text);

}


h1,h2,h3{

font-family:'Fraunces',serif !important;

}


/* HEADER */

.topbar{

position:sticky !important;
top:0 !important;
z-index:999999 !important;
overflow:visible !important;

}


.topbar__row{

display:flex !important;
align-items:center !important;
justify-content:space-between !important;

}


/* MENU */

.menu{

display:flex !important;
align-items:center !important;
gap:32px !important;

visibility:visible !important;
opacity:1 !important;

}


.menu a{

font-family:'Inter',sans-serif !important;
color:var(--text) !important;

}


/* DROPDOWN */

.menu-item{

position:relative !important;

}


.dropdown{

position:absolute !important;
top:100% !important;
left:0 !important;

display:none;

flex-direction:column !important;

min-width:260px;

background:white;

padding:15px;

border-radius:12px;

box-shadow:0 10px 30px rgba(0,0,0,.15);

z-index:999999;

}


.menu-item:hover .dropdown{

display:flex !important;

}


.dropdown a{

display:block !important;
padding:10px !important;
white-space:nowrap;

}


/* FOOTER */

footer{

font-family:'Inter',sans-serif !important;

}


"""


css_text = CSS.read_text(encoding="utf-8")


if "ERMETES MASTER UI SYSTEM" not in css_text:

    css_text += css_fix

    CSS.write_text(
        css_text,
        encoding="utf-8"
    )

    write_log(
        "CSS Master UI applicato"
    )


# ======================
# REPORT
# ======================


REPORT.write_text(
    "\n".join(log),
    encoding="utf-8"
)


print("")
print("=== COMPLETATO ===")
print("Backup:", BACKUP)
print("Report:", REPORT)
