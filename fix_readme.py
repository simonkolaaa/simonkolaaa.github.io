import os

backend_readme = r"C:\Users\Utente\Desktop\portfolio-backend\portfolio-backend\README.md"
content = """# 📖 Portfolio Backend: Il Motore Dietro le Quinte

Ho creato il mio **Portfolio personale** per avere un sito vetrina dove poter raccontare chi sono, mostrare le mie competenze informatiche e i miei progetti scolastici. Essendo un progetto in divenire, continuerò ad aggiornarlo man mano che acquisisco nuove competenze.

Successivamente, su consiglio del mio **professore di informatica**, ho deciso di integrare un vero e proprio **Backend** al portfolio. Volevo che il form di contatto creato nella sezione *Get in Touch* funzionasse realmente, collegandosi a un server privato.

### 🏗️ La Scelta dell'Architettura
Invece di partire da zero, ho deciso di prendere come struttura base il **"Blog Scolastico"** che avevamo sviluppato in classe con Flask. Mi garantiva già un'impalcatura solida.
L'ho però pesantemente modificata, ripulendola dai template HTML, e riadattandola per servire esclusivamente come **API REST** (Headless Backend) in grado di comunicare col frontend React.

### 💻 Cosa ho usato e Perché

- **Backend (Python + Flask):** Ho usato Flask perché è modulare e leggero, perfetto per creare API essenziali. Ho mantenuto lo stile ad *Application Factory* e l'uso del *Repository Pattern* per avere codice scalabile.
- **Sicurezza (Flask-CORS):** Ho implementato i CORS per assicurarmi che solo le richieste in entrata dal mio sito Portfolio ufficiale venissero accettate dall'API protetta.
- **Database (SQLite):** Per salvare i messaggi in ingresso, ho tenuto SQLite. È leggero, affidabile e non richiede installazioni pesanti, perfetto per la portata di questo progetto.
- **Frontend App:** L'interfaccia (in un altro repository) è sviluppata in React. Ho usato fetch() per collegarlo a questa API asincronamente.

---

## 📂 Struttura del Progetto

```text
├── app/
│   ├── __init__.py           <-- Factory (create_app) & CORS config
│   ├── api.py                <-- Route d'ascolto (POST /api/contact)
│   ├── db.py                 <-- Connessione al Database
│   └── repositories/
│       └── contact_repo.py   <-- Gestione queries SQLite pulite (INSERT)
├── instance/
│   └── portfolio.sqlite      <-- Il file in cui vengono salvati i messaggi
├── schema.sql                <-- Schema base della tabella contacts
├── run.py                    <-- Entry point per avviare il server (localhost:5000)
└── setup_db.py               <-- Script per inizializzare il DB da zero
```

Il server remoto è ora ospitato stabilmente e attivo per ricevere contatti."""

with open(backend_readme, "w", encoding="utf-8") as f:
    f.write(content)
print("Scritto README nel backend!")
