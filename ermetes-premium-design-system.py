#!/usr/bin/env python3

import os
import shutil
from datetime import datetime


stamp=datetime.now().strftime("%Y%m%d-%H%M%S")

BACKUP=f"backup-premium-design-{stamp}"

CSS="css/style.css"


print("=== ERMETES PREMIUM DESIGN SYSTEM ===")


os.makedirs(BACKUP)



# backup css

shutil.copy2(
    CSS,
    f"{BACKUP}/style.css"
)



for root,dirs,files in os.walk("."):

    if "backup" in root:
        continue

    for f in files:

        if f.endswith(".html"):

            src=os.path.join(root,f)

            dst=os.path.join(BACKUP,src)

            os.makedirs(
                os.path.dirname(dst),
                exist_ok=True
            )

            shutil.copy2(src,dst)



premium=r"""

/*
================================================

 ERMETES PREMIUM UX DESIGN SYSTEM

================================================
*/


:root{

--ux-radius:16px;

--ux-shadow:
0 20px 50px rgba(0,0,0,.08);

--ux-transition:
all .28s cubic-bezier(.4,0,.2,1);

}


/*
========================
GLOBAL
========================
*/


*{

box-sizing:border-box;

}


html{

scroll-behavior:smooth;

}


body{

-webkit-font-smoothing:antialiased;

line-height:1.65;

}


p{

max-width:720px;

}



section{

scroll-margin-top:100px;

}




/*
========================
HEADER PREMIUM
========================
*/


.topbar{

transition:
background .3s ease,
box-shadow .3s ease;

}



.topbar__row{

min-height:82px!important;

}



.menu{

gap:34px!important;

}



/*
 MENU STABILITY
*/


.menu-item{

position:relative;

padding-bottom:18px;

}



.dropdown{

opacity:0;

visibility:hidden;

transform:
translateY(12px);

transition:

opacity .25s ease,

transform .25s ease,

visibility .25s ease;


display:block!important;


pointer-events:none;

}



.menu-item:hover .dropdown{

opacity:1;

visibility:visible;

transform:
translateY(0);

pointer-events:auto;

}



/*
 lascia tempo al mouse
*/


.dropdown::before{

content:"";

position:absolute;

top:-20px;

left:0;

right:0;

height:20px;

}




.dropdown a{

transition:
padding .2s ease,
background .2s ease;

border-radius:10px;

}



.dropdown a:hover{

background:#f5f7f6;

padding-left:18px;

}



/*
========================
BUTTON PREMIUM
========================
*/


.btn{

transition:
transform .25s ease,
box-shadow .25s ease;

}



.btn:hover{

transform:translateY(-2px);

box-shadow:

0 12px 30px rgba(0,0,0,.12);

}




/*
========================
HERO
========================
*/


.hero{

padding-top:110px!important;

padding-bottom:100px!important;

}



.hero__copy{

animation:
fadeUp .6s ease;

}



.hero-image,
.hero__image{

animation:
fadeUp .7s ease;

}



@keyframes fadeUp{

from{

opacity:0;

transform:translateY(20px);

}

to{

opacity:1;

transform:none;

}

}



/*
========================
CARDS
========================
*/


.card{

border-radius:18px!important;

transition:

transform .3s ease,

box-shadow .3s ease;


}



.card:hover{

transform:translateY(-5px);

box-shadow:

0 20px 40px rgba(0,0,0,.08);

}




/*
========================
FORM PREMIUM
========================
*/


input,
textarea,
select{

width:100%;

border-radius:14px!important;

border:1px solid #d9dee5!important;

padding:15px 16px!important;

font-size:1rem;

transition:

border .25s ease,

box-shadow .25s ease;


}



input:focus,
textarea:focus,
select:focus{


outline:none!important;


border-color:#6dbb87!important;


box-shadow:

0 0 0 4px rgba(109,187,135,.15);


}




label{

font-weight:600;

margin-bottom:8px;

display:block;

}




form ul,
form ol{

padding-left:20px;

line-height:1.8;

}



.checkbox,
.radio{

display:flex;

gap:10px;

align-items:center;

}





/*
========================
CTA NORMAL
========================
*/


.final-cta,
.cta-final,
.cta{

background:#fff!important;

color:inherit!important;

border-radius:20px;

}




.final-cta h2,
.cta h2{

color:#1d2939!important;

}





/*
========================
FOOTER
========================
*/


footer{

padding-top:70px!important;

padding-bottom:50px!important;

}




footer a{

transition:
color .2s ease;

}




/*
========================
RESPONSIVE
========================
*/


@media(max-width:900px){


.menu{

gap:18px!important;

}



.hero{

padding-top:70px!important;

padding-bottom:60px!important;

}



}



/*
========================
ACCESSIBILITY
========================
*/


a:focus-visible,
button:focus-visible,
input:focus-visible{

outline:3px solid rgba(109,187,135,.5);

outline-offset:3px;

}



"""


with open(CSS,"a",encoding="utf8") as f:

    f.write(premium)



print()
print("=== COMPLETATO ===")
print("Backup:",BACKUP)
print("CSS premium installato")
print()
print("Ora:")
print("CTRL+SHIFT+R browser")
