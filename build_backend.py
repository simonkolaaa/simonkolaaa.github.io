import os

base_dir = r"C:\Users\Utente\Desktop\portfolio-backend"

# Struttura delle cartelle
directories = [
    os.path.join(base_dir, "app"),
    os.path.join(base_dir, "app", "repositories"),
]

for d in directories:
    os.makedirs(d, exist_ok=True)

# Contenuto dei file
files = {
    os.path.join(base_dir, "app", "__init__.py"): '''import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app) # Permette le richieste dal frontend React

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'portfolio.sqlite'),
    )

    from . import db
    db.init_app(app)

    # --- REGISTRAZIONE BLUEPRINTS ---
    from . import api
    app.register_blueprint(api.bp)

    return app
''',

    os.path.join(base_dir, "app", "db.py"): '''import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
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
        contact_repository.create_contact(name, email, message)
        return jsonify({"success": "Messaggio ricevuto in modo sicuro!"}), 201
    except Exception as e:
        return jsonify({"error": "Errore interno del server."}), 500

@bp.route('/contacts', methods=['GET'])
def get_contacts():
    # Solo per test, in produzione andrebbe protetta
    contacts = contact_repository.get_all_contacts()
    return jsonify([dict(c) for c in contacts]), 200
''',

    os.path.join(base_dir, "app", "repositories", "__init__.py"): '''# File vuoto per definire il modulo
''',

    os.path.join(base_dir, "app", "repositories", "contact_repository.py"): '''from app.db import get_db

def create_contact(name, email, message):
    db = get_db()
    db.execute(
        'INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
        (name, email, message)
    )
    db.commit()

def get_all_contacts():
    db = get_db()
    return db.execute('SELECT * FROM contacts ORDER BY created_at DESC').fetchall()
''',

    os.path.join(base_dir, "run.py"): '''from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
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

    print("Database portfolio.sqlite creato con successo in:", db_path)
    connection.close()
''',
    os.path.join(base_dir, "requirements.txt"): '''Flask
Flask-Cors
'''
}

for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Backend costruito con successo in:", base_dir)
