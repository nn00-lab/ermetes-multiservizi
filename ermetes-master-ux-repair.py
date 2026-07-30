#!/usr/bin/env python3

import os
import shutil
import re
from datetime import datetime


ROOT="."
MASTER="index.html"


stamp=datetime.now().strftime("%Y%m%d-%H%M%S")
BACKUP=f"backup-master-ux-{stamp}"
REPORT="master-ux-report.txt"


print("\n=== ERMETES MASTER UX/UI REPAIR ===\n")


os.makedirs(BACKUP)


report=[]


# ==========================
# BACKUP
# ==========================

for root,dirs,files in os.walk(ROOT):

    if "backup" in root:
        continue

    for f in files:

        if f.endswith(".html") or f.endswith(".css"):

            src=os.path.join(root,f)

            dst=os.path.join(BACKUP,src)

            os.makedirs(os.path.dirname(dst),exist_ok=True)

            shutil.copy2(src,dst)



print("Backup:",BACKUP)



# ==========================
# READ MASTER HEADER FOOTER
# ==========================


def extract(text,start,end):

    a=text.find(start)

    b=text.find(end,a)

    if a==-1 or b==-1:
        return None

    return text[a:b]


with open(MASTER,encoding="utf8") as f:
    master=f.read()



master_header=extract(
    master,
    "<header class=\"topbar\">",
    "</header>"
)


master_footer=extract(
    master,
    "<footer",
    "</footer>"
)



if not master_header:
    print("ERRORE header master non trovato")
    exit()



# ==========================
# HTML NORMALIZATION
# ==========================


pages=[]


for root,dirs,files in os.walk(ROOT):

    if "backup" in root:
        continue

    for f in files:

        if f.endswith(".html"):

            pages.append(os.path.join(root,f))



for page in pages:


    if page==MASTER:
        continue


    try:

        text=open(page,encoding="utf8").read()


        old_header=extract(
            text,
            "<header class=\"topbar\">",
            "</header>"
        )


        if old_header:

            text=text.replace(
                old_header,
                master_header
            )

            report.append(
                f"HEADER sincronizzato {page}"
            )


        # =====================
        # FONT MASTER
        # =====================


        master_fonts=re.findall(
            r'<link[^>]+font[^>]+>',
            master
        )


        for font in master_fonts:

            if font not in text:

                text=text.replace(
                    "</head>",
                    font+"\n</head>"
                )

                report.append(
                    f"FONT aggiunto {page}"
                )



        # =====================
        # CTA VERDI FINALI
        # =====================


        text=re.sub(
            r'(final-cta|cta-final|section class="cta")[^>]*',
            'section class="cta-normal"',
            text,
            flags=re.I
        )


        # =====================
        # FOOTER
        # =====================


        if master_footer:

            old_footer=extract(
                text,
                "<footer",
                "</footer>"
            )

            if old_footer:

                text=text.replace(
                    old_footer,
                    master_footer
                )

                report.append(
                    f"FOOTER sincronizzato {page}"
                )



        open(page,"w",encoding="utf8").write(text)



    except Exception as e:

        report.append(
            f"ERRORE {page} {e}"
        )



# ==========================
# CSS MASTER OVERRIDE
# ==========================


css="css/style.css"


with open(css,encoding="utf8") as f:
    style=f.read()



override=r"""

/* ==========================================
   ERMETES MASTER UX/UI SYSTEM
   HOME INDEX AS DESIGN SOURCE
========================================== */


/* HEADER */

.topbar{
    position:sticky!important;
    top:0!important;
    z-index:9999!important;
}


.topbar__row{

    display:flex!important;
    align-items:center!important;
    justify-content:space-between!important;
    min-height:82px!important;

}


.menu{

    display:flex!important;
    align-items:center!important;
    gap:32px!important;

}


.menu a{

    font-family:inherit!important;
    font-size:.95rem!important;
    font-weight:600!important;

}


/* DROPDOWN */

.menu-item{

position:relative!important;

}


.dropdown{

position:absolute!important;
top:calc(100% + 12px)!important;
left:0!important;

display:none;

width:260px!important;

background:#fff!important;

padding:14px!important;

border-radius:12px!important;

box-shadow:
0 15px 40px rgba(0,0,0,.12)!important;


}


.dropdown a{

display:block!important;

padding:10px 12px!important;

line-height:1.4!important;

}


.menu-item:hover .dropdown{

display:block!important;

}



/* HERO */


.hero{

padding:110px 0 100px!important;

}


.hero h1{

font-size:clamp(36px,4vw,58px)!important;

line-height:1.1!important;

}



.hero__sub{

max-width:620px!important;

font-size:1.15rem!important;

line-height:1.7!important;

}



/* BUTTON */


.btn{

border-radius:14px!important;

font-weight:700!important;

padding:14px 28px!important;

}



/* NORMAL CTA */


.cta-normal,
.final-cta{

background:#fff!important;

color:inherit!important;

}


.cta-normal h2,
.final-cta h2{

color:#222!important;

}



/* FOOTER */


footer{

margin-top:80px!important;

}



/* DESKTOP FIX */

@media(min-width:901px){

.topbar__row{

padding-left:0!important;
padding-right:0!important;

}


.hero__grid{

align-items:center!important;

}

}



"""


with open(css,"a",encoding="utf8") as f:

    f.write("\n"+override)



# ==========================
# REPORT
# ==========================


with open(REPORT,"w",encoding="utf8") as f:

    for r in report:
        f.write(r+"\n")



print("\n=== COMPLETATO ===")
print("Backup:",BACKUP)
print("Report:",REPORT)
print("Pagine analizzate:",len(pages))
print("Modifiche:",len(report))
