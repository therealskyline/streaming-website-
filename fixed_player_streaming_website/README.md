# AnimeStream - Plateforme de Streaming d'Anime

Un site web de streaming d'anime construit avec Flask, permettant aux utilisateurs de découvrir, regarder et télécharger des animes.

## Fonctionnalités

- Recherche d'anime avec filtres par genres
- Lecture des épisodes en streaming VOSTFR et VF
- Téléchargement d'épisodes
- Suivi de progression de visionnage
- Favoris
- Interface utilisateur responsive

## Prérequis

- Python 3.9 ou supérieur
- Pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt
```
git clone https://github.com/therealskyline/streaming-website-.git
cd streaming-website-
```

2. Installez les dépendances
```
pip install -r requirements.txt
```

3. Lancez l'application
```
python run.py
```

ou utilisez le script de démarrage (Linux/Mac) :
```
./start.sh
```

## Structure du projet

- `app.py` : Point d'entrée principal de l'application Flask
- `run.py` : Script de démarrage avec gestion des processus et signaux
- `reset_animes.py` : Utilitaire pour nettoyer les données d'anime problématiques
- `templates/` : Fichiers HTML/Jinja2 pour le front-end
- `static/` : Fichiers statiques (CSS, JS, images)
- `data_discover.json` : Données pour la section "Découvrir de Nouvelles Séries"

## Utilisation

Une fois l'application démarrée, accédez à http://localhost:5000 dans votre navigateur. 

Par défaut, les utilisateurs devront se connecter ou créer un compte pour accéder au contenu.

## Résolution des problèmes

Si certains animes ne présentent pas toutes leurs saisons, utilisez le script reset_animes.py :

```
python reset_animes.py
```

Puis redémarrez l'application.

## Notes importantes

Ce projet utilise l'API Anime-Sama pour récupérer les métadonnées et liens des épisodes. Il est conçu pour un usage personnel/éducatif uniquement.