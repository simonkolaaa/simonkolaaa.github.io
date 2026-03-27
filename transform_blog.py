import os
import shutil

base_dir = r"C:\Users\Utente\Desktop\blog_scolastico"

# Delete unneeded files from the old school blog
to_delete = [
    os.path.join(base_dir, "app", "templates"),
    os.path.join(base_dir, "app", "auth.py"),
    os.path.join(base_dir, "app", "main.py"),
    os.path.join(base_dir, "app", "repositories", "post_repository.py")
]
for p in to_delete:
    if os.path.exists(p):
        if os.path.isdir(p):
            shutil.rmtree(p)
        else:
            os.remove(p)

files = {
    os.path.join(base_dir, "app", "__init__.py"): '''import os
from flask import Flask
from flask_cors import CORS

def create_app():
    # Mantiene la tipica Factory Pattern che avevi usato a scuola
    app = Flask(__name__, instance_relative_config=True)
    
    # Aggiungiamo i CORS per permettere al Frontend React di contattare Flask
    CORS(app) 

    app.config.from_mapping(
        SECRET_KEY='portfolio-secret',
        DATABASE=os.path.join(app.instance_path, 'portfolio.sqlite'),
    )

    from . import db
    db.init_app(app)

    # Invece di 'main' e 'auth', registriamo un blueprint per le 'api'
    from . import api
    app.register_blueprint(api.bp)

    return app
''',

    os.path.join(base_dir, "app", "schema.sql"): '''DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''',

    os.path.join(base_dir, "app", "api.py"): '''from flask import Blueprint, request, jsonify
from app.repositories import contact_repository

# Blueprint per le rotte API, che sostituisce il tuo vecchio "main.py"
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if not name or not email or not message:
        return jsonify({"error": "Tutti i campi sono obbligatori."}), 400
        
    try:
        # Usiamo il repository per tenere il codice pulito (stessa tecnica usata a scuola)
        contact_repository.create_contact(name, email, message)
        return jsonify({"success": "Messaggio ricevuto con successo!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/contacts', methods=['GET'])
def get_contacts():
    # Rotta per leggere tutti i messaggi ricevuti (solo a scopo di test)
    contacts = contact_repository.get_all_contacts()
    return jsonify([dict(c) for c in contacts]), 200
''',

    os.path.join(base_dir, "app", "repositories", "contact_repository.py"): '''from app.db import get_db

# Questo sostituisce il tuo vecchio "post_repository.py"
def create_contact(name, email, message):
    db = get_db()
    db.execute(
        'INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
        (name, email, message)
    )
    db.commit()

def get_all_contacts():
    db = get_db()
    return db.execute('SELECT id, name, email, message, created_at FROM contacts ORDER BY created_at DESC').fetchall()
''',

    os.path.join(base_dir, "setup_db.py"): '''import sqlite3
import os
from app import create_app

app = create_app()

with app.app_context():
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    db_path = app.config['DATABASE']
    connection = sqlite3.connect(db_path)

    with open('app/schema.sql') as f:
        connection.executescript(f.read())

    print("Database portfolio.sqlite inizializzato con successo in:", db_path)
    connection.close()
''',

    os.path.join(base_dir, "requirements.txt"): '''Flask
Flask-Cors
'''
}

for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Blog trasformato in Portfolio Backend!")
