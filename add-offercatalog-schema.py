#!/usr/bin/env python3

import glob
import json
import re

catalog = {
    "@type": "OfferCatalog",
    "name": "Servizi Ermetes",
    "itemListElement": [
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Pulizie professionali"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Pulizie condominiali"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Pulizie uffici"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Pulizie post cantiere"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Sanificazione ambienti"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Tinteggiature"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Cartongesso"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Manutenzioni immobiliari"
            }
        },
        {
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "name": "Manutenzione aree verdi"
            }
        }
    ]
}


files = glob.glob("*.html") + glob.glob("servizi/*.html")


for file in files:

    text = open(file, encoding="utf-8").read()

    changed = [False]


    def replace_schema(match):


        block = match.group(1)

        try:
            data = json.loads(block)
        except:
            return match.group(0)


        if data.get("@type") != "LocalBusiness":
            return match.group(0)


        if "hasOfferCatalog" in data:
            return match.group(0)


        data["hasOfferCatalog"] = catalog

        changed[0] = True

        return (
            '<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2)
            + '\n</script>'
        )


    new_text = re.sub(
        r'<script type="application/ld\+json">(.*?)</script>',
        replace_schema,
        text,
        flags=re.S
    )


    if changed[0]:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_text)

        print("Aggiornato:", file)
    else:
        print("Nessuna modifica:", file)


print("Completato")
