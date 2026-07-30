# Landing Page — Pulizie & Piccole Manutenzioni

## File
- `index.html` — struttura + SEO + JSON-LD + hook GTM
- `style.css` — token di design (colori/font in `:root`)
- `script.js` — wizard 6 step, validazione, tracking, invio lead
- `assets/favicon.svg`

## Da configurare prima del deploy
1. **script.js** → `WEBHOOK_URL`: incolla URL n8n/Make/Zapier/Sheets/CRM (riceve JSON POST).
2. **index.html**:
   - `GTM-XXXXXXX` → il tuo ID GTM (gestisci da lì GA4, Meta Pixel, Google Ads da GTM — consigliato, zero altro codice da toccare).
   - JSON-LD `LocalBusiness`: nome, telefono, indirizzo reali.
   - Numeri di telefono ed email in header/footer.
   - `tuodominio.it` → dominio reale (canonical, OG image).
3. **assets/**: aggiungi `og-cover.jpg` (1200x630) per anteprime social.

## Tracking incluso (via dataLayer, da mappare in GTM)
`page_view`, `cta_click`, `step_view`, `scroll_depth`, `generate_lead`, `form_abandon`, `form_error`.
Parametri lead: UTM, gclid/fbclid/ttclid/msclkid, device/browser/OS/viewport/lingua/timezone, lead_uuid, tempo di compilazione, step abbandonato.

## Deploy
Drag&drop della cartella su Netlify o Cloudflare Pages, oppure push su repo GitHub collegato a Vercel/GitHub Pages. Nessuna build richiesta.

## Note tecniche
- No framework, no dipendenze.
- Honeypot anti-bot incluso; rate limit e reCAPTCHA vanno aggiunti lato webhook/server.
- Nessun localStorage: stato del wizard solo in memoria di sessione.
