import os

folder = r"C:\Users\Utente\Desktop\blog_scolastico\.vscode"
os.makedirs(folder, exist_ok=True)

settings_path = os.path.join(folder, "settings.json")
with open(settings_path, "w") as f:
    f.write('{\n    "python.defaultInterpreterPath": "venv\\\\Scripts\\\\python.exe",\n    "python.terminal.activateEnvironment": true\n}')

print("VS Code settings creati con successo.")
