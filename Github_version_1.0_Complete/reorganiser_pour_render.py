#!/usr/bin/env python3
"""
Script pour réorganiser le projet en structure AnimeZone pour déploiement sur Render
Cette structure sépare les fichiers essentiels (dans AnimeZone/) des fichiers supprimables
"""

import os
import shutil
import sys
import re
from pathlib import Path

# Fichiers et dossiers essentiels à placer dans AnimeZone/
ESSENTIAL_FOLDERS = [
    'API',
    'static',
    'templates',
    'config',
    'workflows'
]

ESSENTIAL_FILES = [
    'app.py',
    'main.py',
    'run.py',
    'requirements.txt',
    'web_scraper.py',
    'data_discover.json'
]

# Fichiers et dossiers à ignorer (à laisser à la racine)
IGNORE_PATTERNS = [
    '__pycache__',
    '.git',
    '.replit',
    '.upm',
    '.config',
    '.pythonlibs',
    '.cache',
    'archives',
    'temp_backup',
    'backup_files_old',
    'migrate',
    '.gitignore'
]

def create_structure():
    """Crée la structure principale"""
    # Créer le dossier AnimeZone s'il n'existe pas
    if not os.path.exists('AnimeZone'):
        os.makedirs('AnimeZone')
        print("✅ Dossier AnimeZone créé")

def should_include(path):
    """Vérifie si un chemin doit être inclus dans AnimeZone"""
    path_parts = path.split(os.sep)
    
    # Ignorer les chemins qui commencent par un dossier à ignorer
    for ignore_pattern in IGNORE_PATTERNS:
        if any(part.startswith(ignore_pattern) for part in path_parts):
            return False
    
    # Inclure les chemins qui commencent par un dossier essentiel
    for folder in ESSENTIAL_FOLDERS:
        if path.startswith(folder):
            return True
    
    # Inclure les fichiers essentiels
    if os.path.isfile(path) and os.path.basename(path) in ESSENTIAL_FILES:
        return True
    
    return False

def copy_essential_files():
    """Copie les fichiers et dossiers essentiels dans AnimeZone/"""
    # Copier les dossiers essentiels
    for folder in ESSENTIAL_FOLDERS:
        if os.path.exists(folder) and os.path.isdir(folder):
            print(f"Copie du dossier {folder}...")
            # Ignorer les __pycache__ et autres fichiers non essentiels
            def ignore_func(src, names):
                return [name for name in names if any(pattern in name for pattern in IGNORE_PATTERNS)]
            
            # Copier le dossier
            dest_path = os.path.join('AnimeZone', folder)
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
            shutil.copytree(folder, dest_path, ignore=ignore_func)
            print(f"✅ Dossier {folder} copié vers AnimeZone/{folder}")
    
    # Copier les fichiers essentiels
    for file in ESSENTIAL_FILES:
        if os.path.exists(file) and os.path.isfile(file):
            print(f"Copie du fichier {file}...")
            shutil.copy2(file, os.path.join('AnimeZone', file))
            print(f"✅ Fichier {file} copié vers AnimeZone/{file}")

def create_render_deployment_files():
    """Crée les fichiers nécessaires pour le déploiement sur Render"""
    # Créer un fichier requirements.txt dans AnimeZone si nécessaire
    if not os.path.exists(os.path.join('AnimeZone', 'requirements.txt')):
        with open(os.path.join('AnimeZone', 'requirements.txt'), 'w') as f:
            f.write("# Dépendances pour AnimeZone\n")
            f.write("flask>=3.1.0\n")
            f.write("flask-login>=0.6.3\n")
            f.write("flask-sqlalchemy>=3.1.1\n")
            f.write("gunicorn>=23.0.0\n")
            f.write("httpx>=0.28.1\n")
            f.write("trafilatura>=2.0.0\n")
        print("✅ Fichier requirements.txt créé pour Render")
    
    # Créer un fichier start.sh pour Render
    with open(os.path.join('AnimeZone', 'start.sh'), 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Script de démarrage pour Render\n\n")
        f.write("# Exécuter gunicorn\n")
        f.write("exec gunicorn --bind 0.0.0.0:$PORT app:app\n")
    
    # Rendre start.sh exécutable
    os.chmod(os.path.join('AnimeZone', 'start.sh'), 0o755)
    print("✅ Fichier start.sh créé pour Render")
    
    # Créer un fichier README.md pour documentation
    with open(os.path.join('AnimeZone', 'README.md'), 'w') as f:
        f.write("# AnimeZone\n\n")
        f.write("Site de streaming d'anime avec fonctionnalités avancées.\n\n")
        f.write("## Déploiement sur Render\n\n")
        f.write("### Configuration\n\n")
        f.write("- **Build Command**: `pip install -r requirements.txt`\n")
        f.write("- **Start Command**: `sh start.sh`\n")
    print("✅ Fichier README.md créé avec instructions pour Render")

def rename_animestream_to_animezone():
    """Remplace toutes les occurrences de 'AnimeStream' par 'AnimeZone' dans les fichiers"""
    print("Remplacement de 'AnimeStream' par 'AnimeZone' dans les fichiers...")
    
    for root, dirs, files in os.walk('AnimeZone'):
        # Ignorer les dossiers __pycache__
        dirs[:] = [d for d in dirs if d != '__pycache__']
        
        for file in files:
            if file.endswith(('.py', '.html', '.js', '.css', '.md', '.txt', '.sh')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Remplacer les occurrences, en préservant la casse
                    modified = False
                    
                    # Cas spécifiques pour préserver la casse
                    replacements = [
                        ('AnimeStream', 'AnimeZone'),
                        ('Animestream', 'Animezone'),
                        ('animestream', 'animezone'),
                        ('ANIMESTREAM', 'ANIMEZONE')
                    ]
                    
                    new_content = content
                    for old, new in replacements:
                        if old in new_content:
                            new_content = new_content.replace(old, new)
                            modified = True
                    
                    if modified:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"✅ Remplacements effectués dans {file_path}")
                except Exception as e:
                    print(f"⚠️ Erreur lors du traitement de {file_path}: {e}")

def main():
    """Fonction principale"""
    print("🔄 Réorganisation du projet pour déploiement sur Render...")
    
    # Créer la structure
    create_structure()
    
    # Copier les fichiers essentiels
    copy_essential_files()
    
    # Créer les fichiers nécessaires pour Render
    create_render_deployment_files()
    
    # Remplacer AnimeStream par AnimeZone
    rename_animestream_to_animezone()
    
    print("\n✅ Réorganisation terminée !")
    print("   Le dossier AnimeZone/ contient tous les fichiers nécessaires pour le déploiement sur Render.")
    print("   Les fichiers et dossiers non essentiels sont restés à la racine.")

if __name__ == "__main__":
    main()