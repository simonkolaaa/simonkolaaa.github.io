<p align="center">
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30">
  <h1 align="center">Hello there, I'm Simon Kola! 👋</h1>
</p>

<p align="center">
  <strong>IT Student | Aspiring Software Engineer | Tech Enthusiast</strong>
</p>

<p align="center">
  <a href="https://simonkolaaa.github.io" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-2581-2c3e50?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website" />
  </a>
  <a href="https://linkedin.com/in/simon-kola" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://instagram.com/simonkolaaa" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="mailto:simonkola21@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

---

## 📖 Il Mio Progetto: Portfolio Full-Stack

Ho creato questo portfolio personalizzato inizialmente per avere un sito vetrina dove poter raccontare chi sono, mostrare le mie competenze e i miei progetti scolastici. Essendo un progetto in continua evoluzione, continuerò ad aggiornarlo man mano che il mio percorso di studi avanza e imparo cose nuove.

Successivamente, su prezioso consiglio del mio professore di informatica, ho deciso di fare un salto di qualità trasformando questo semplice sito statico in un vero e proprio sistema **Full-Stack**. L'obiettivo era creare un form di contatto realmente funzionante nella sezione *Get in Touch*, da poter collegare a un backend remoto per ricevere messaggi da chi visita la pagina.

### 🏗️ L'Evoluzione del Backend
Per costruire il lato server, ho deciso di non reinventare la ruota ma applicare le conoscenze scolastiche: **ho preso come struttura di partenza un "Blog Scolastico" sviluppato precedentemente in classe con Flask**. 

L'ho svuotato della parte visiva (HTML/Template) e l'ho modificato per usarlo esclusivamente come API "Headless", mantenendone l'impalcatura solida che conoscevamo:
- Pattern **Application Factory** (`create_app`)
- Divisione in **Blueprint** per le rotte API
- Layer dei **Repositories** dedicato all'interazione sicura col database

### 💻 Perché ho usato queste Tecnologie
- **Frontend (Questo Repository):** Sviluppato in **React**. L'ho scelto perché garantisce un caricamento immediato e fluido delle pagine (Single Page Application) e una gestione moderna dei componenti UI. È ospitato su *GitHub Pages*.
- **Backend API:** Scritto in **Python** con **Flask**. Essendo un framework molto leggero e modulare, è risultato perfetto per esporre un endpoint RESTful velocissimo. Ho aggiunto la libreria `flask-cors` per permettere al form React di inviare asincronamente i dati in sicurezza.
- **Database:** **SQLite**. La sua natura basata su un singolo file locale è eccellente e rapida per salvare tabelle semplici (come i messaggi di contatto) senza sovraccaricare il server.
- **Deploy Backend:** Il codice Python è stato caricato su un repository separato ed è ospitato da **PythonAnywhere**. Questo mi garantisce che il server sia in ascolto 24h ore su 24 per ricevere i moduli dal portfolio, salvando persistentemente i dati su disco cloud.

---

## 📂 Struttura dell'Architettura

Questa è la mappa semplificata di come i due rami del mio progetto si interconnettono:

```text
├── 🌍 SimonKola's Portfolio (Frontend / React) -- [IN QUESTO REPO]
│   ├── src/
│   │   ├── components/
│   │   │   └── home/
│   │   │       └── GetInTouch.jsx   <-- Form che invia i dati (Fetch POST)
│   │   └── App.js
│   └── package.json
│
└── ☁️ PythonAnywhere Server (Backend / Flask) -- [REPO SEPARATO]
    ├── app/
    │   ├── __init__.py           <-- Factory & CORS config
    │   ├── api.py                <-- Route d'ascolto (POST /api/contact)
    │   ├── db.py                 <-- Connessione Database
    │   └── repositories/
    │       └── contact_repo.py   <-- Query Builder SQLite (INSERT INTO)
    ├── instance/
    │   └── portfolio.sqlite      <-- Il database in cui si salvano i messaggi
    └── run.py                    <-- Entry point del server (WSGI Server)
```

---

### 📊 Le Mie Statistiche GitHub

Questo lavoro mi ha permesso di unire finalmente ciò che studio a scuola con le dinamiche reali di una vera architettura disaccoppiata moderna. E nel tempo libero... si continua a codare!

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=simonkolaaa&show_icons=true&theme=tokyonight&count_private=true&hide_border=true" height="170" alt="stats report" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=simonkolaaa&layout=compact&theme=tokyonight&hide_border=true&hide=css" height="170" alt="languages report" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=simonkolaaa&theme=tokyonight&hide_border=true" alt="streak stats" />
</p>

<p align="center">
  Built with ❤️ by Simon Kola
</p>
