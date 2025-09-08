#!/usr/bin/env python3
"""
Configuration utilitaire pour les exemples Python du SDK Opendatasoft Explore
"""

import os
import sys
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

def get_api_config():
    """
    Récupère la configuration API depuis les variables d'environnement
    
    Returns:
        tuple: (base_url, api_key)
        
    Raises:
        ValueError: Si les variables d'environnement ne sont pas configurées
    """
    base_url = os.getenv('OPENDATASOFT_BASE_URL')
    api_key = os.getenv('OPENDATASOFT_API_KEY')
    
    if not base_url:
        raise ValueError(
            "OPENDATASOFT_BASE_URL non configuré. "
            "Copiez .env.example vers .env et configurez vos valeurs."
        )
    
    if not api_key:
        raise ValueError(
            "OPENDATASOFT_API_KEY non configuré. "
            "Copiez .env.example vers .env et configurez vos valeurs."
        )
    
    return base_url, api_key

def create_api_client():
    """
    Crée un client API configuré avec les variables d'environnement
    
    Returns:
        opendatasoft_explore.ApiClient: Client API configuré
    """
    # Import ici pour éviter les erreurs si le SDK n'est pas installé
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../python'))
    
    import opendatasoft_explore
    
    base_url, api_key = get_api_config()
    
    # Configuration du client API
    configuration = opendatasoft_explore.Configuration(host=base_url)
    configuration.api_key['apikey'] = api_key
    
    return opendatasoft_explore.ApiClient(configuration)