# AnimeStream - Nouvelle Structure de Projet

## Réorganisation du Projet

Le projet a été réorganisé pour améliorer la maintenabilité et la clarté du code. La nouvelle structure sépare clairement les différentes parties de l'application.

## Comment Migrer

Pour migrer vers la nouvelle structure, exécutez le script de migration :

```bash
python migrate_to_new_structure.py
```

Ce script :
1. Crée la nouvelle structure de dossiers
2. Copie les fichiers dans leurs emplacements appropriés
3. Met à jour les imports dans les fichiers Python

## Nouvelle Structure

```
.
├── src/                   # Code source principal
│   ├── api/               # API Anime-Sama et intégrations externes
│   ├── core/              # Noyau de l'application
│   ├── config/            # Fichiers de configuration
│   ├── docs/              # Documentation
│   └── scripts/           # Scripts utilitaires
├── static/                # Fichiers statiques (CSS, JS, images)
├── templates/             # Templates HTML
├── archives/              # Fichiers anciens, sauvegardes, fichiers supprimables
└── workflows/             # Configuration des workflows Replit
```

## Avantages

1. **Organisation Logique** : Les fichiers sont regroupés par fonction
2. **Évolutivité** : Facilite l'ajout de nouvelles fonctionnalités
3. **Maintenabilité** : Réduit la confusion et facilite la navigation dans le code
4. **Propreté** : Les fichiers supprimables sont isolés dans le dossier `archives`

## Après La Migration

Après la migration, vous devez :

1. Utiliser `src/main.py` comme point d'entrée pour Replit
2. Mettre à jour les scripts de démarrage pour pointer vers les nouveaux emplacements
3. Adapter les imports dans tout nouveau fichier créé

## Documentation Détaillée

Pour plus d'informations sur la nouvelle structure, consultez le fichier `src/docs/STRUCTURE.md`.