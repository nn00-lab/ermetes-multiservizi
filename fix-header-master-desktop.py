#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil


CSS = Path("css/style.css")

backup = Path(
    f"backup-header-master-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
)

backup.mkdir()

shutil.copy2(CSS, backup / "style.css")


print("=== ERMETES HEADER MASTER DESKTOP ===")
print("Backup:", backup)


css = CSS.read_text(encoding="utf-8")


fix = r"""


/* ==========================================
   ERMETES MASTER HEADER DESKTOP UX
   HOME IDENTICA SU TUTTE LE PAGINE
========================================== */


:root{

--header-height:82px;

}



/* HEADER */

.topbar{

height:82px !important;
min-height:82px !important;

display:flex !important;
align-items:center !important;

position:sticky !important;
top:0;

z-index:999999 !important;

background:#ffffff !important;

}



/* CONTENITORE */

.topbar__row{

height:82px !important;
min-height:82px !important;

display:flex !important;

align-items:center !important;

justify-content:space-between !important;

gap:32px !important;

}



/* LOGO */

.logo{

display:flex !important;

align-items:center !important;

height:82px !important;

}



.logo img{

height:52px !important;

width:auto !important;

display:block !important;

}



/* MENU */

.menu{

height:82px !important;

display:flex !important;

align-items:center !important;

gap:34px !important;

margin:0 !important;

padding:0 !important;

}



/* LINK */

.menu > a,
.menu-item > a{

height:82px !important;

display:flex !important;

align-items:center !important;

white-space:nowrap !important;

font-size:16px !important;

font-weight:600 !important;

}



/* SERVIZI */

.menu-item{

height:82px !important;

display:flex !important;

align-items:center !important;

}



/* DROPDOWN */

.dropdown{

top:82px !important;

}



/* AZIONI DESTRA */

.header-actions{

height:82px !important;

display:flex !important;

align-items:center !important;

gap:18px !important;

white-space:nowrap !important;

}



/* EVITA MOVIMENTI */

body{

overflow-x:hidden;

}



/* DESKTOP ONLY */

@media(min-width:901px){

.topbar__row{

max-width:1200px !important;

margin:auto !important;

}


}


"""


if "ERMETES MASTER HEADER DESKTOP UX" not in css:

    css += fix

    CSS.write_text(
        css,
        encoding="utf-8"
    )


print("")
print("=== COMPLETATO ===")
print("Header desktop uniformata alla HOME")
print("Backup:", backup)
