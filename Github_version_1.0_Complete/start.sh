#!/bin/bash
# Script de démarrage optimisé pour Replit
# Désactive le mode débug pour une meilleure stabilité

# Définit les variables d'environnement nécessaires
export FLASK_APP=app.py
export FLASK_ENV=production  # Utilise l'environnement de production pour plus de stabilité
export PYTHONUNBUFFERED=1    # Permet de voir les logs sans délai

# Démarrage optimisé pour Replit
echo "Démarrage du serveur AnimeStream sur Replit..."
python run_replit.py