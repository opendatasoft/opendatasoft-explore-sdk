#!/usr/bin/env python3
"""
Exemple : Récupération des métadonnées du catalogue Opendatasoft

Ce script démontre comment :
- Se connecter à l'API Opendatasoft Explore
- Récupérer la liste des datasets du catalogue
- Afficher les métadonnées de chaque dataset
- Explorer la structure des champs
"""

import sys
import os
# Ajout du chemin vers le module de configuration
sys.path.insert(0, os.path.dirname(__file__))
# Ajout du chemin vers le SDK Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../python'))

import opendatasoft_explore
from opendatasoft_explore.rest import ApiException
from config import create_api_client

def get_catalog_metadata(limit=15, show_details=True):
    """
    Récupère et affiche les métadonnées du catalogue
    
    Args:
        limit (int): Nombre maximum de datasets à récupérer
        show_details (bool): Afficher les détails du premier dataset
    
    Returns:
        bool: True si succès, False sinon
    """
    try:
        # Création du client API avec la configuration depuis .env
        with create_api_client() as api_client:
            catalog_api = opendatasoft_explore.CatalogApi(api_client)
            
            print("=== 📊 Catalogue Opendatasoft - Métadonnées ===\n")
            
            # 1. Récupération de la liste des datasets
            print("🔍 Récupération des datasets...")
            datasets = catalog_api.get_datasets(limit=limit)
            
            print(f"✅ Nombre total de datasets dans le catalogue: {datasets.total_count}")
            print(f"📋 Datasets affichés: {len(datasets.results)}\n")
            
            print("=" * 80)
            
            # 2. Affichage des métadonnées de chaque dataset
            for i, dataset in enumerate(datasets.results, 1):
                print(f"\n🎯 Dataset #{i}")
                print(f"   📁 ID: {dataset.dataset_id}")
                
                # Récupération sécurisée des métadonnées
                default_metas = dataset.metas.get('default', {}) if dataset.metas else {}
                
                print(f"   📝 Titre: {default_metas.get('title', 'Sans titre')}")
                
                # Description (tronquée si trop longue)
                description = default_metas.get('description', '')
                if description:
                    desc_display = description[:100] + '...' if len(description) > 100 else description
                    print(f"   📄 Description: {desc_display}")
                
                print(f"   📊 Enregistrements: {default_metas.get('records_count', 0)}")
                print(f"   📅 Modifié: {default_metas.get('modified', 'N/A')}")
                
                # Éditeur (si disponible)
                publisher = default_metas.get('publisher')
                if publisher:
                    print(f"   🏢 Éditeur: {publisher}")
                
                print(f"   🌐 Langue: {default_metas.get('language', 'N/A')}")
                
                # Informations sur les champs
                if hasattr(dataset, 'fields') and dataset.fields:
                    print(f"   🔧 Champs disponibles ({len(dataset.fields)}):")
                    for field in dataset.fields[:5]:  # Afficher les 5 premiers champs
                        field_name = getattr(field, 'name', 'N/A')
                        field_type = getattr(field, 'type', 'N/A')
                        field_label = getattr(field, 'label', field_name)
                        print(f"      • {field_label} ({field_name}) - {field_type}")
                    
                    if len(dataset.fields) > 5:
                        print(f"      ... et {len(dataset.fields) - 5} autres champs")
                
                print("-" * 80)
            
            # 3. Détails du premier dataset (si demandé)
            if show_details and datasets.results:
                print(f"\n🔍 Détails du premier dataset:")
                first_dataset = datasets.results[0]
                
                try:
                    detailed_dataset = catalog_api.get_dataset(dataset_id=first_dataset.dataset_id)
                    default_metas = detailed_dataset.metas.get('default', {}) if detailed_dataset.metas else {}
                    
                    print(f"   🎯 Dataset détaillé: {first_dataset.dataset_id}")
                    print(f"   📝 Titre complet: {default_metas.get('title', 'N/A')}")
                    print(f"   🗂️ Références: {default_metas.get('references', 'N/A')}")
                    print(f"   🌍 Territoire: {default_metas.get('territory', 'N/A')}")
                    print(f"   🔐 Fédéré: {default_metas.get('federated', False)}")
                    
                    # Informations supplémentaires
                    if detailed_dataset.features:
                        print(f"   ⚡ Fonctionnalités: {', '.join(detailed_dataset.features)}")
                    
                    print(f"   👁️ Données visibles: {getattr(detailed_dataset, 'data_visible', 'N/A')}")
                    
                except ApiException as detail_error:
                    print(f"   ❌ Erreur lors de la récupération des détails: {detail_error.reason}")
            
            print(f"\n✅ Récupération des métadonnées terminée avec succès!")
            return True
            
    except ApiException as e:
        print(f"❌ Erreur API: {e.reason} (Code: {e.status})")
        return False
    
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return False

def main():
    """Point d'entrée principal du script"""
    try:
        success = get_catalog_metadata()
        if success:
            print("\n🎉 Script exécuté avec succès!")
        else:
            print("\n💥 Erreur lors de l'exécution du script")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⏹️ Script interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n💥 Erreur critique: {e}")
        if "OPENDATASOFT_" in str(e):
            print("\n💡 Astuce: Vérifiez votre fichier .env (copiez .env.example)")
        sys.exit(1)

if __name__ == "__main__":
    main()