# Guide d'installation de la correction Hunter x Hunter pour AnimeZone

Ce guide vous explique comment installer et lancer la version corrigée d'AnimeZone avec le support de Hunter x Hunter.

## Prérequis

- Python 3.7 ou supérieur
- Un terminal ou invite de commande
- Les packages listés dans requirements.txt

## Installation

1. **Décompressez l'archive GitHubV1-HunterXHunter-Fix.zip** dans le répertoire de votre choix.

2. **Installez les dépendances requises** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Exécutez le script spécial pour GitHub** :
   ```bash
   python run_github.py
   ```
   
   Ce script démarre l'application avec les correctifs spéciaux pour Hunter x Hunter.

## Vérification

Pour confirmer que l'installation fonctionne correctement :

1. Accédez à l'interface web d'AnimeZone (par défaut sur http://localhost:5000)
2. Connectez-vous à votre compte ou créez-en un
3. Recherchez "Hunter x Hunter" dans la barre de recherche
4. Sélectionnez un épisode et vérifiez qu'il se charge correctement sans erreur 404

## Fonctionnalités spéciales

- **Recherche améliorée** : Plusieurs variantes du titre sont utilisées pour trouver Hunter x Hunter
- **Récupération dynamique des URLs** : Les URLs des épisodes sont récupérées en temps réel
- **Fallback intelligent** : En cas d'échec, des URLs de secours sont utilisées pour garantir le fonctionnement

## Problèmes connus

Si vous rencontrez encore des erreurs 404 :

1. Veillez à bien utiliser le script `run_github.py` et non les scripts standard
2. Vérifiez les logs pour des messages d'erreur spécifiques
3. Essayez de recharger la page ou de vider votre cache

## Support et aide

Si vous rencontrez des problèmes, référez-vous au fichier README-HUNTER-X-HUNTER.md pour des informations techniques détaillées sur les correctifs.