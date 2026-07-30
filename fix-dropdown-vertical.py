#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil

css = Path("css/style.css")

backup = f"backup-dropdown-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
Path(backup).mkdir()

shutil.copy2(css, Path(backup) / "style.css")

data = css.read_text(encoding="utf-8")


fix = """

/* =================================
   ERMETES DROPDOWN VERTICAL MENU
================================= */

.menu-item{
    position:relative !important;
}


.dropdown{
    display:none;
    position:absolute !important;
    top:100% !important;
    left:0 !important;

    flex-direction:column !important;

    min-width:260px !important;
    padding:15px !important;

    background:#ffffff !important;
    border-radius:12px !important;

    box-shadow:0 10px 30px rgba(0,0,0,.15) !important;

    z-index:999999 !important;
}


.menu-item:hover .dropdown{
    display:flex !important;
    flex-direction:column !important;
}


.dropdown a{

    display:block !important;

    width:100% !important;

    padding:10px 14px !important;

    white-space:nowrap !important;

}


.dropdown a:hover{

    background:#f4f7f5 !important;

}

"""

if "ERMETES DROPDOWN VERTICAL MENU" not in data:
    data += fix

css.write_text(data, encoding="utf-8")


print("=== DROPDOWN VERTICALE SISTEMATO ===")
print("Backup:", backup)
