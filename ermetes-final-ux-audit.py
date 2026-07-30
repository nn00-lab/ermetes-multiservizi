#!/usr/bin/env python3

import os
import re
import shutil
from datetime import datetime


STAMP=datetime.now().strftime("%Y%m%d-%H%M%S")

BACKUP=f"backup-final-ux-{STAMP}"

REPORT="final-ux-report.txt"


print("""
====================================
 ERMETES FINAL UX/UI AUDIT ENGINE
====================================
""")


os.makedirs(BACKUP)



issues=[]



def backup_file(path):

    dest=os.path.join(BACKUP,path)

    os.makedirs(
        os.path.dirname(dest),
        exist_ok=True
    )

    shutil.copy2(path,dest)



# trova pagine

pages=[]


for root,dirs,files in os.walk("."):

    if "backup" in root:
        continue

    for f in files:

        if f.endswith(".html"):

            pages.append(
                os.path.join(root,f)
            )



print("Pagine:",len(pages))



# backup

for p in pages:

    backup_file(p)



backup_file("css/style.css")



master=open(
    "index.html",
    encoding="utf8"
).read()



master_header=re.search(
r'<header class="topbar".*?</header>',
master,
re.S
)



master_footer=re.search(
r'<footer.*?</footer>',
master,
re.S
)



header_ok=master_header.group(0) if master_header else None

footer_ok=master_footer.group(0) if master_footer else None




for page in pages:


    if page=="./index.html":
        continue


    text=open(
        page,
        encoding="utf8"
    ).read()



    original=text



    # HEADER uniformazione


    if header_ok:

        text=re.sub(
            r'<header class="topbar".*?</header>',
            header_ok,
            text,
            flags=re.S
        )



    # footer


    if footer_ok:

        text=re.sub(
            r'<footer.*?</footer>',
            footer_ok,
            text,
            flags=re.S
        )



    # classi hero


    text=text.replace(
        'hero__image',
        'hero-image'
    )



    # CTA verdi invasive


    text=re.sub(
        r'class="([^"]*)green([^"]*)"',
        r'class="\1\2"',
        text,
        flags=re.I
    )



    # font link uniformi


    fonts=re.findall(
        r'<link[^>]+font[^>]+>',
        master
    )


    if fonts:

        text=re.sub(
            r'<link[^>]+font[^>]+>',
            '',
            text
        )

        text=text.replace(
            '<head>',
            '<head>\n'+"\n".join(fonts)
        )



    if text!=original:


        with open(
            page,
            "w",
            encoding="utf8"
        ) as f:

            f.write(text)


        issues.append(
            page+" modificata"
        )




# CSS finale

css=open(
"css/style.css",
encoding="utf8"
).read()



css_fix=r"""

/* FINAL UX NORMALIZATION */


.container,
.wrap{

max-width:1200px;

}



h1,h2,h3{

letter-spacing:-.02em;

}



section{

position:relative;

}



.dropdown{

transition:
opacity .25s ease,
transform .25s ease;

}



footer{

margin-top:0;

}



.btn{

cursor:pointer;

}



.hero__sub{

color:#475467;

}



.final-cta,
.cta-final{

background:white!important;

}



"""



with open(
"css/style.css",
"a",
encoding="utf8"
) as f:

    f.write(css_fix)



# report


with open(
REPORT,
"w",
encoding="utf8"
) as f:


    f.write(
"""ERMETES FINAL UX AUDIT

Pagine analizzate:
{}

Modifiche:
{}

Backup:
{}

""".format(
len(pages),
"\n".join(issues),
BACKUP
)
)



print()
print("================================")
print(" COMPLETATO")
print("================================")
print()
print("Backup:",BACKUP)
print("Report:",REPORT)
print("Modifiche:",len(issues))
print()
print("Esegui:")
print("CTRL + SHIFT + R")
