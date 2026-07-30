#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import shutil


CSS = Path("css/style.css")

backup = Path(
    f"backup-finalcta-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
)

backup.mkdir()

shutil.copy2(CSS, backup / "style.css")


print("=== FIX FINAL CTA ===")
print("Backup:", backup)


css = CSS.read_text(encoding="utf-8")


fix = r"""


/* =====================================
   FINAL CTA NORMAL UI
===================================== */


.finalcta,
.finalcta * {

    color:#182230 !important;

}


.finalcta {

    background:#ffffff !important;

}


.finalcta h1,
.finalcta h2,
.finalcta h3 {

    color:#182230 !important;
    font-family:'Fraunces',serif !important;

}


.finalcta p {

    color:#667085 !important;

}


.finalcta span {

    color:#182230 !important;

}


/* bottone */

.finalcta .btn {

    background:#16805c !important;
    color:#ffffff !important;

}


"""


if "FINAL CTA NORMAL UI" not in css:

    css += fix

    CSS.write_text(
        css,
        encoding="utf-8"
    )


print("")
print("=== COMPLETATO ===")
print("Final CTA normalizzata")
print("Aggiorna browser con CTRL+SHIFT+R")
