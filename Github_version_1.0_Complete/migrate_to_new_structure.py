#!/usr/bin/env python3
"""
Script de migration vers la nouvelle structure de dossiers
Ce script facilite la transition de l'ancienne structure vers la nouvelle
"""

import os
import shutil
import sys
from pathlib import Path

def create_directory_structure():
    """Crée la structure de dossiers nécessaire"""
    directories = [
        "src/core",
        "src/api",
        "src/scripts",
        "src/config",
        "src/docs", 
        "archives/backup",
        "archives/temp"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Dossier créé: {directory}")

def move_files():
    """Déplace les fichiers dans leurs dossiers appropriés"""
    # Fichiers principaux
    core_files = ["app.py", "web_scraper.py"]
    for file in core_files:
        if os.path.exists(file):
            shutil.copy2(file, f"src/core/{file}")
            print(f"Copié: {file} -> src/core/{file}")
    
    # Scripts
    script_files = ["run.py", "run_replit.py", "run-server.py", "main.py", 
                   "execute_site.py", "reset_animes.py"]
    for file in script_files:
        if os.path.exists(file):
            shutil.copy2(file, f"src/scripts/{os.path.basename(file)}")
            print(f"Copié: {file} -> src/scripts/{os.path.basename(file)}")
    
    # Scripts shell
    shell_scripts = ["start.sh", "start-server.sh", "start-flask-server.sh", 
                    "start-server-bg.sh"]
    for file in shell_scripts:
        if os.path.exists(file):
            shutil.copy2(file, f"src/scripts/{file}")
            print(f"Copié: {file} -> src/scripts/{file}")
    
    # Configuration
    config_files = ["requirements.txt", ".gitignore", "data_discover.json"]
    for file in config_files:
        if os.path.exists(file):
            shutil.copy2(file, f"src/config/{os.path.basename(file)}")
            print(f"Copié: {file} -> src/config/{os.path.basename(file)}")
    
    # Documentation
    doc_files = ["README.md"]
    for file in doc_files:
        if os.path.exists(file):
            shutil.copy2(file, f"src/docs/{file}")
            print(f"Copié: {file} -> src/docs/{file}")
    
    # API
    if os.path.exists("API"):
        # Utiliser copytree avec ignore pour éviter de copier __pycache__
        def ignore_cache(dir, files):
            return [f for f in files if f == "__pycache__"]
        
        for item in os.listdir("API"):
            s = os.path.join("API", item)
            d = os.path.join("src/api", item)
            if os.path.isdir(s):
                shutil.copytree(s, d, ignore=ignore_cache, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print("Copié: API/ -> src/api/")
    
    # Dossiers supprimables
    if os.path.exists("backup_files_old"):
        # Copier les dossiers de sauvegarde
        for item in os.listdir("backup_files_old"):
            s = os.path.join("backup_files_old", item)
            d = os.path.join("archives/backup", item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print("Copié: backup_files_old/ -> archives/backup/")

def update_imports():
    """Met à jour les imports dans les fichiers Python"""
    # Exécuter le script update_imports.py
    try:
        os.system("python src/scripts/update_imports.py")
        print("Les imports ont été mis à jour")
    except Exception as e:
        print(f"Erreur lors de la mise à jour des imports: {e}")

def main():
    """Fonction principale de migration"""
    print("Début de la migration vers la nouvelle structure...")
    
    # Créer la structure de dossiers
    create_directory_structure()
    
    # Déplacer les fichiers
    move_files()
    
    # Mettre à jour les imports
    update_imports()
    
    print("\nMigration terminée avec succès!")
    print("\nNouvelle structure de dossiers:")
    print("--------------------------------")
    os.system("find src -type d | sort")
    
    print("\nPour utiliser la nouvelle structure:")
    print("1. Mettez à jour les scripts de démarrage pour utiliser src/main.py")
    print("2. Utilisez les imports depuis src.* dans vos fichiers Python")
    print("3. Consultez src/docs/STRUCTURE.md pour plus d'informations")

if __name__ == "__main__":
    main()