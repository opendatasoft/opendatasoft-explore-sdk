# Exemples Python pour l'API Opendatasoft Explore

Ce dossier contient des exemples d'utilisation du SDK Python pour l'API Opendatasoft Explore v2.1.

## 🚀 Démarrage rapide

1. **Configurer l'environnement**:
   ```bash
   # Depuis le dossier racine du projet
   python3 -m venv venv
   source venv/bin/activate
   pip install -r python/requirements.txt
   pip install python-dotenv
   ```

2. **Configurer vos identifiants**:
   ```bash
   cd examples/python
   cp .env.example .env
   # Éditer .env avec vos valeurs
   ```

3. **Lancer les exemples**:
   ```bash
   # Depuis le dossier racine du projet
   python examples/python/get_catalog_metadata.py
   python examples/python/get_dataset_records.py
   ```

## 📁 Scripts disponibles

### 1. get_catalog_metadata.py
**Récupération des métadonnées du catalogue**

**Fonctionnalités :**
- Liste des datasets avec leurs métadonnées complètes
- Informations sur les champs disponibles (nom, type, label)
- Détails avancés d'un dataset spécifique

### 2. get_dataset_records.py
**Récupération des enregistrements depuis les datasets**

**Fonctionnalités :**
- Recherche intelligente de datasets avec des enregistrements
- Récupération d'exemples d'enregistrements avec données réelles
- Affichage de la structure complète des datasets
- Démonstration de la pagination et des requêtes avancées


## 🔧 Configuration

### Fichiers de configuration
- `.env.example` : Template de configuration
- `.env` : Votre configuration (créé à partir de .env.example)
- `config.py` : Module utilitaire pour charger la configuration

### Variables d'environnement requises
```bash
# Domaine de votre portail Opendatasoft
OPENDATASOFT_BASE_URL=https://votre-domaine.opendatasoft.com/api/explore/v2.1

# Votre clé API Opendatasoft
OPENDATASOFT_API_KEY=votre_cle_api_ici
```
