#!/usr/bin/env python3
"""
Script pour remplacer toutes les occurrences d'AnimeStream par AnimeZone
dans tous les fichiers du projet
"""

import os
import re
import sys

def remplacer_dans_fichier(fichier):
    """Remplace AnimeStream par AnimeZone dans un fichier"""
    try:
        # Lire le contenu du fichier
        with open(fichier, 'r', encoding='utf-8', errors='ignore') as f:
            contenu = f.read()
        
        # Vérifier si AnimeStream est présent dans le fichier
        if 'AnimeStream' in contenu or 'Animestream' in contenu or 'animestream' in contenu or 'ANIMESTREAM' in contenu:
            print(f"Modification de {fichier}...")
            
            # Remplacer toutes les variations
            nouveau_contenu = contenu
            nouveau_contenu = re.sub(r'AnimeStream', 'AnimeZone', nouveau_contenu)
            nouveau_contenu = re.sub(r'Animestream', 'Animezone', nouveau_contenu)
            nouveau_contenu = re.sub(r'animestream', 'animezone', nouveau_contenu)
            nouveau_contenu = re.sub(r'ANIMESTREAM', 'ANIMEZONE', nouveau_contenu)
            
            # Écrire le nouveau contenu
            with open(fichier, 'w', encoding='utf-8') as f:
                f.write(nouveau_contenu)
            
            return True
    except Exception as e:
        print(f"⚠️ Erreur avec {fichier}: {e}")
    
    return False

def parcourir_dossier(dossier):
    """Parcourt récursivement un dossier pour remplacer AnimeStream par AnimeZone"""
    modifies = 0
    total = 0
    
    # Extensions de fichiers à traiter
    extensions = ('.py', '.html', '.js', '.css', '.md', '.txt', '.json', '.sh', '.toml')
    
    for racine, dossiers, fichiers in os.walk(dossier):
        # Ignorer les dossiers cachés et __pycache__
        dossiers[:] = [d for d in dossiers if not d.startswith('.') and d != '__pycache__']
        
        for fichier in fichiers:
            if fichier.endswith(extensions) and not fichier.startswith('.'):
                chemin_complet = os.path.join(racine, fichier)
                total += 1
                if remplacer_dans_fichier(chemin_complet):
                    modifies += 1
    
    print(f"\n✅ Terminé! {modifies} fichiers modifiés sur {total} fichiers analysés")

if __name__ == "__main__":
    dossier_cible = 'AnimeZone'
    if not os.path.exists(dossier_cible):
        print(f"⚠️ Le dossier {dossier_cible} n'existe pas!")
        sys.exit(1)
    
    print(f"🔄 Remplacement de toutes les occurrences d'AnimeStream par AnimeZone dans {dossier_cible}...")
    parcourir_dossier(dossier_cible)