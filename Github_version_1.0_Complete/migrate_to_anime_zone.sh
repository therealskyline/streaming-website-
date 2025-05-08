#!/bin/bash
# Script pour migrer un projet existant vers la structure AnimeZone

echo "🔄 Migration vers la structure AnimeZone"
echo "========================================"

# Vérifier si Python est disponible
if ! command -v python3 &> /dev/null; then
    echo "⚠️ Python 3 n'est pas installé. Utilisation de 'python' à la place."
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo "1️⃣ Exécution du script de réorganisation..."
$PYTHON_CMD reorganize_anime_zone.py

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de la réorganisation."
    exit 1
fi

echo "2️⃣ Vérification de la structure..."
if [ ! -d "AnimeZone" ]; then
    echo "❌ Le dossier AnimeZone n'a pas été créé correctement."
    exit 1
fi

echo "3️⃣ Configuration des permissions..."
chmod +x AnimeZone/run.sh
chmod +x AnimeZone/setup.sh

echo "4️⃣ Installation dans le nouvel environnement..."
cd AnimeZone
./setup.sh

echo "✅ Migration terminée avec succès!"
echo "   Vous pouvez maintenant utiliser votre application depuis le dossier AnimeZone"
echo "   Lancez-la avec: cd AnimeZone && ./run.sh"