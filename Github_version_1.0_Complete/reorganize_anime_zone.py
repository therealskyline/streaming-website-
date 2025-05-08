#!/usr/bin/env python3
"""
Script pour réorganiser le projet en structure AnimeZone avec séparation backend/frontend
"""

import os
import shutil
import sys
from pathlib import Path
import re

def create_directory_structure():
    """Crée la structure de dossiers AnimeZone"""
    directories = [
        "AnimeZone/backend/core",
        "AnimeZone/backend/api",
        "AnimeZone/backend/config",
        "AnimeZone/backend/scripts",
        "AnimeZone/frontend/static",
        "AnimeZone/frontend/templates",
        "AnimeZone/docs"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Dossier créé: {directory}")

def organize_backend():
    """Organise les fichiers du backend"""
    # Fichiers principaux
    core_files = ["app.py", "web_scraper.py"]
    for file in core_files:
        if os.path.exists(file):
            shutil.copy2(file, f"AnimeZone/backend/core/{file}")
            print(f"Copié: {file} -> AnimeZone/backend/core/{file}")
    
    # API
    if os.path.exists("API"):
        for item in os.listdir("API"):
            src_path = os.path.join("API", item)
            # Ignorer les fichiers cache
            if item == "__pycache__" or item.endswith(".pyc"):
                continue
                
            if os.path.isdir(src_path):
                # Exclure les dossiers __pycache__ lors de la copie
                def ignore_cache(dir, files):
                    return [f for f in files if f == "__pycache__" or f.endswith(".pyc")]
                
                dst_path = os.path.join("AnimeZone/backend/api", item)
                shutil.copytree(src_path, dst_path, ignore=ignore_cache, dirs_exist_ok=True)
            else:
                dst_path = os.path.join("AnimeZone/backend/api", item)
                shutil.copy2(src_path, dst_path)
        print("API copiée dans AnimeZone/backend/api/")
    
    # Configuration
    config_files = ["requirements.txt", "data_discover.json"]
    for file in config_files:
        if os.path.exists(file):
            shutil.copy2(file, f"AnimeZone/backend/config/{file}")
            print(f"Copié: {file} -> AnimeZone/backend/config/{file}")
    
    # Scripts utiles
    script_files = ["run.py", "run_replit.py", "run-server.py", "start.sh", "main.py"]
    for file in script_files:
        if os.path.exists(file):
            shutil.copy2(file, f"AnimeZone/backend/scripts/{file}")
            print(f"Copié: {file} -> AnimeZone/backend/scripts/{file}")

def organize_frontend():
    """Organise les fichiers du frontend"""
    # Templates
    if os.path.exists("templates"):
        for item in os.listdir("templates"):
            src_path = os.path.join("templates", item)
            dst_path = os.path.join("AnimeZone/frontend/templates", item)
            
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
        print("Templates copiés dans AnimeZone/frontend/templates/")
    
    # Fichiers statiques (CSS, JS, images)
    if os.path.exists("static"):
        for item in os.listdir("static"):
            src_path = os.path.join("static", item)
            # Ignorer les fichiers cache
            if item == "__pycache__" or item.endswith(".pyc"):
                continue
                
            dst_path = os.path.join("AnimeZone/frontend/static", item)
            
            if os.path.isdir(src_path):
                # Exclure les dossiers __pycache__ lors de la copie
                def ignore_cache(dir, files):
                    return [f for f in files if f == "__pycache__" or f.endswith(".pyc")]
                
                shutil.copytree(src_path, dst_path, ignore=ignore_cache, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dst_path)
        print("Fichiers statiques copiés dans AnimeZone/frontend/static/")

def create_main_module():
    """Crée un fichier principal pour l'application"""
    main_py_content = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
AnimeZone - Application principale
Ce fichier est le point d'entrée principal pour l'application AnimeZone
\"\"\"

import os
import sys

# Ajouter le répertoire AnimeZone/backend au path pour les imports
backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Importer l'application depuis le backend
from core.app import app

if __name__ == "__main__":
    # Configuration du serveur
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Démarrage du serveur
    app.run(host=host, port=port, debug=debug)
"""
    
    with open("AnimeZone/main.py", "w") as f:
        f.write(main_py_content)
    print("Fichier principal créé: AnimeZone/main.py")

def create_readme():
    """Crée un fichier README pour expliquer la structure"""
    readme_content = """# AnimeZone - Streaming d'Anime

## Structure du Projet

```
AnimeZone/
├── backend/           # Côté serveur
│   ├── core/          # Application principale Flask
│   ├── api/           # API et intégrations externes
│   ├── config/        # Fichiers de configuration
│   └── scripts/       # Scripts utilitaires
├── frontend/          # Côté client
│   ├── static/        # Fichiers statiques (CSS, JS, images)
│   └── templates/     # Templates HTML
├── docs/              # Documentation du projet
└── main.py            # Point d'entrée principal
```

## Installation

```bash
# Se placer dans le dossier AnimeZone
cd AnimeZone

# Installer les dépendances
pip install -r backend/config/requirements.txt
```

## Lancement

```bash
# Lancer l'application
python main.py
```

## Développement

- **Backend**: Contient toute la logique serveur (Flask, API, etc.)
- **Frontend**: Contient les templates et fichiers statiques
"""
    
    with open("AnimeZone/README.md", "w") as f:
        f.write(readme_content)
    print("Fichier README créé: AnimeZone/README.md")

def main():
    """Fonction principale"""
    print("Réorganisation du projet en structure AnimeZone...")
    
    # Créer la structure de dossiers
    create_directory_structure()
    
    # Organiser les fichiers
    organize_backend()
    organize_frontend()
    
    # Créer les fichiers principaux
    create_main_module()
    create_readme()
    
    print("\nRéorganisation terminée avec succès!")
    print("\nNouvelle structure AnimeZone:")
    print("-----------------------------")
    os.system("find AnimeZone -type d | sort")

if __name__ == "__main__":
    main()