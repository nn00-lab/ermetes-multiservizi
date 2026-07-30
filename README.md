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

# Setup del Progetto

Questa guida spiega come collegare il progetto a GitHub e Netlify per ottenere il deploy automatico.

---

# Architettura

```text
Server / PC
    │
    ▼
Git
    │
git push
    │
    ▼
GitHub
    │
Webhook
    │
    ▼
Netlify
(Build automatico)
    │
    ▼
Sito Online
```

Ogni modifica segue questo flusso:

```bash
git add .
git commit -m "Descrizione modifica"
git push
```

Netlify rileva automaticamente il nuovo commit, esegue il deploy e aggiorna il sito.

---

# 1. Inizializzare Git (solo la prima volta)

Entrare nella cartella del progetto:

```bash
cd ~/projects/ermetes-multiservizi
```

Inizializzare Git:

```bash
git init
```

Configurare il proprio nome:

```bash
git config --global user.name "Il tuo nome"
```

Configurare la propria email GitHub:

```bash
git config --global user.email "tua-email@example.com"
```

Aggiungere tutti i file:

```bash
git add .
```

Creare il primo commit:

```bash
git commit -m "Initial commit"
```

Impostare il branch principale:

```bash
git branch -M main
```

---

# 2. Collegare il repository GitHub

Aggiungere il repository remoto:

```bash
git remote add origin git@github.com:nn00-lab/ermetes-multiservizi.git
```

Verificare:

```bash
git remote -v
```

---

# 3. Configurazione SSH

Generare una chiave (solo se non esiste):

```bash
ssh-keygen -t ed25519 -C "tua-email@example.com"
```

Visualizzare la chiave pubblica:

```bash
cat ~/.ssh/id_ed25519.pub
```

Aggiungere la chiave su:

GitHub → **Settings** → **SSH and GPG keys** → **New SSH Key**

Testare la connessione:

```bash
ssh -T git@github.com
```

Se compare:

```text
Hi username! You've successfully authenticated...
```

la configurazione è corretta.

---

# 4. Primo Push

Inviare il progetto:

```bash
git push -u origin main
```

Da questo momento il repository locale e GitHub sono collegati.

---

# 5. Collegare Netlify

1. Accedere a Netlify.
2. Add new site.
3. Import an existing project.
4. Scegliere GitHub.
5. Selezionare il repository `nn00-lab/ermetes-multiservizi`.
6. Branch: `main`.
7. Build command: lasciare vuoto (per sito HTML/CSS/JS).
8. Publish directory: `.` (oppure lasciare vuoto se Netlify la rileva automaticamente).
9. Deploy.

---

# 6. Workflow quotidiano

Ogni volta che si modifica il progetto:

```bash
git add .
git commit -m "Descrizione modifica"
git push
```

Il sito verrà aggiornato automaticamente.

---

# Comandi utili

Controllare lo stato:

```bash
git status
```

Vedere il repository remoto:

```bash
git remote -v
```

Scaricare gli ultimi aggiornamenti:

```bash
git pull
```

Visualizzare i commit:

```bash
git log --oneline
```

---

# Flusso di lavoro

```text
Modifica file
      │
      ▼
git add .
      │
      ▼
git commit
      │
      ▼
git push
      │
      ▼
GitHub
      │
      ▼
Netlify
      │
      ▼
Deploy Automatico
      │
      ▼
Sito Online
```

---

# Buone pratiche

* Fare commit piccoli e descrittivi.
* Eseguire `git pull` se si lavora da più dispositivi.
* Non modificare direttamente i file su GitHub se il progetto viene sviluppato localmente.
* Conservare la chiave SSH in modo sicuro.
* Non inserire password o token all'interno del repository.

---

# Obiettivo finale

L'infrastruttura del progetto è:

```text
Ubuntu / VS Code
        │
        ▼
Git
        │
        ▼
GitHub
        │
        ▼
Netlify
        │
        ▼
Dominio
        │
        ▼
Sito Online
```

Questa configurazione permette di sviluppare, versionare e pubblicare il progetto con un semplice:

```bash
git add .
git commit -m "Nuova funzionalità"
git push
```
