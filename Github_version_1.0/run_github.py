#!/usr/bin/env python3
"""
Point d'entrée spécial pour GitHub avec correctifs pour Hunter x Hunter
Script optimisé pour l'environnement GitHub
"""

import logging
import os
import signal
import sys
import subprocess
import time
from flask import Flask

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("AnimeZone-GitHub")

def kill_existing_servers():
    """
    Arrête tous les processus Python existants pour éviter les conflits de ports
    """
    logger.info("Arrêt des serveurs existants...")
    try:
        if sys.platform == 'win32':  # Windows
            os.system('taskkill /F /IM python.exe')
        else:  # Linux/Unix/Mac
            # Obtenir le PID actuel pour éviter de se tuer soi-même
            current_pid = os.getpid()
            
            try:
                # Obtenir tous les processus Python en cours d'exécution
                pythons = subprocess.check_output(["pgrep", "python"]).decode('utf-8').strip().split('\n')
                for pid in pythons:
                    try:
                        pid = int(pid)
                        # Ne pas tuer le processus actuel
                        if pid != current_pid:
                            logger.info(f"Arrêt du processus Python {pid}")
                            os.kill(pid, signal.SIGTERM)
                    except (ValueError, ProcessLookupError):
                        pass
            except (subprocess.SubprocessError, FileNotFoundError):
                logger.warning("Impossible d'obtenir la liste des processus Python")
        
        # Attendre un peu pour s'assurer que les processus sont arrêtés
        time.sleep(1)
        logger.info("Serveurs existants arrêtés.")
    except Exception as e:
        logger.error(f"Erreur lors de l'arrêt des serveurs: {e}")

def main():
    """
    Script principal pour démarrer l'application web AnimeZone sur GitHub
    Ce script s'assure que l'application démarre avec les bonnes options
    pour être accessible avec les correctifs spécifiques pour Hunter x Hunter
    """
    
    # Arrêter les serveurs existants pour éviter les conflits de port
    kill_existing_servers()
    
    # Import de l'application une fois que tous les autres serveurs sont arrêtés
    import app
    
    # Récupérer le port depuis l'environnement ou utiliser 5000 par défaut
    port = int(os.environ.get('PORT', 5000))
    
    # Récupérer l'hôte depuis l'environnement ou utiliser le safe default pour environnement GitHub
    host = os.environ.get('HOST', '0.0.0.0')
    
    logger.info(f"Démarrage de l'application AnimeZone GitHub sur {host}:{port}")
    
    # Configuration du gestionnaire de signaux pour arrêt propre
    def signal_handler(sig, frame):
        logger.info("Signal d'arrêt reçu, fermeture de l'application...")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Démarrer le serveur Flask
    logger.info("Version GitHub avec correctifs spéciaux pour Hunter x Hunter")
    app.app.run(host=host, port=port, debug=False, threaded=True)

if __name__ == "__main__":
    main()