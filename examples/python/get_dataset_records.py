#!/usr/bin/env python3
"""
Exemple : Récupération des enregistrements depuis les datasets Opendatasoft

Ce script démontre comment :
- Rechercher des datasets avec des enregistrements
- Récupérer des exemples d'enregistrements
- Explorer la structure des données
- Utiliser la pagination
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

def get_dataset_records(max_datasets=3, records_per_dataset=3):
    """
    Récupère et affiche les enregistrements depuis les datasets
    
    Args:
        max_datasets (int): Nombre maximum de datasets à traiter
        records_per_dataset (int): Nombre d'enregistrements à récupérer par dataset
    
    Returns:
        bool: True si succès, False sinon
    """
    try:
        # Création du client API avec la configuration depuis .env
        with create_api_client() as api_client:
            catalog_api = opendatasoft_explore.CatalogApi(api_client)
            dataset_api = opendatasoft_explore.DatasetApi(api_client)
            
            print("=== 📊 Opendatasoft - Récupération des Records ===\n")
            
            # 1. Recherche de datasets avec des enregistrements
            print("🔍 Recherche de datasets avec des enregistrements...")
            datasets = catalog_api.get_datasets(limit=20)
            
            datasets_with_records = []
            for dataset in datasets.results:
                default_metas = dataset.metas.get('default', {}) if dataset.metas else {}
                records_count = default_metas.get('records_count', 0)
                if records_count > 0:
                    datasets_with_records.append((dataset, records_count))
            
            print(f"✅ Trouvé {len(datasets_with_records)} datasets avec des enregistrements")
            print(f"📋 Traitement des {min(max_datasets, len(datasets_with_records))} premiers\n")
            
            # 2. Récupération des enregistrements
            for i, (dataset, records_count) in enumerate(datasets_with_records[:max_datasets], 1):
                dataset_id = dataset.dataset_id
                default_metas = dataset.metas.get('default', {}) if dataset.metas else {}
                dataset_title = default_metas.get('title', dataset_id)
                
                print("=" * 80)
                print(f"🎯 Dataset #{i}: {dataset_title}")
                print(f"   📁 ID: {dataset_id}")
                print(f"   📊 Total enregistrements: {records_count}")
                
                try:
                    # Récupération des enregistrements d'exemple
                    print(f"\n📥 Récupération de {records_per_dataset} enregistrements d'exemple...")
                    records = dataset_api.get_records(
                        dataset_id=dataset_id,
                        limit=records_per_dataset
                    )
                    
                    print(f"✅ Récupérés: {len(records.results)} enregistrements")
                    
                    # Affichage de la structure du dataset
                    if hasattr(dataset, 'fields') and dataset.fields:
                        print(f"\n🔧 Structure du dataset ({len(dataset.fields)} champs):")
                        for field in dataset.fields:
                            field_name = getattr(field, 'name', 'N/A')
                            field_type = getattr(field, 'type', 'N/A')
                            field_label = getattr(field, 'label', field_name)
                            print(f"   • {field_label} [{field_name}] ({field_type})")
                    
                    # Affichage des enregistrements
                    if records.results:
                        print(f"\n📋 Exemples d'enregistrements:")
                        
                        for j, record in enumerate(records.results, 1):
                            print(f"\n   📝 Enregistrement #{j}:")
                            
                            # Récupération des données du record
                            try:
                                record_dict = record.to_dict() if hasattr(record, 'to_dict') else {}
                                
                                # Affichage des champs de données (en évitant les métadonnées)
                                data_fields = 0
                                max_display_fields = 5
                                
                                for key, value in record_dict.items():
                                    # Ignorer les champs système
                                    if key not in ['id', 'timestamp', 'size', 'links'] and not key.startswith('_'):
                                        print(f"      {key}: {value}")
                                        data_fields += 1
                                        if data_fields >= max_display_fields:
                                            remaining = len(record_dict) - max_display_fields
                                            if remaining > 0:
                                                print(f"      ... et {remaining} autres champs")
                                            break
                                
                                if data_fields == 0:
                                    # Fallback : afficher le record brut
                                    print(f"      Record: {record}")
                                    
                            except Exception as record_error:
                                print(f"      ❌ Erreur d'accès au record: {record_error}")
                                print(f"      Record brut: {record}")
                    
                    # Informations sur la pagination
                    print(f"\n📄 Pagination: affichage de {len(records.results)} sur {records.total_count} enregistrements")
                    
                    if records.total_count > records_per_dataset:
                        print(f"   💡 Pour récupérer plus d'enregistrements, utilisez le paramètre 'offset'")
                    
                    print("-" * 80)
                    
                except ApiException as dataset_error:
                    print(f"❌ Erreur lors de la récupération des enregistrements: {dataset_error.reason}")
                    print("-" * 80)
                    continue
                    
                except Exception as e:
                    print(f"❌ Erreur inattendue pour le dataset {dataset_id}: {e}")
                    print("-" * 80)
                    continue
            
            # 3. Exemple de requête avec paramètres avancés
            if datasets_with_records:
                print(f"\n🔍 Exemple de requête avec paramètres avancés:")
                first_dataset, first_count = datasets_with_records[0]
                
                try:
                    print(f"   Dataset: {first_dataset.dataset_id}")
                    
                    # Requête avec pagination
                    paginated_records = dataset_api.get_records(
                        dataset_id=first_dataset.dataset_id,
                        limit=2,
                        offset=0
                    )
                    
                    print(f"   ✅ Pagination (limit=2, offset=0): {len(paginated_records.results)} enregistrements")
                    
                    # Test avec offset
                    if first_count > 2:
                        offset_records = dataset_api.get_records(
                            dataset_id=first_dataset.dataset_id,
                            limit=1,
                            offset=2
                        )
                        print(f"   ✅ Pagination (limit=1, offset=2): {len(offset_records.results)} enregistrements")
                    
                except ApiException as query_error:
                    print(f"   ❌ Erreur de requête paramétrique: {query_error.reason}")
            
            print(f"\n🎉 Récupération des enregistrements terminée!")
            return True
                
    except ApiException as e:
        print(f"❌ Erreur API: {e.reason} (Code: {e.status})")
        return False
    
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Point d'entrée principal du script"""
    try:
        success = get_dataset_records()
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