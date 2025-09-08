#!/usr/bin/env python3
"""
Script de test pour valider que les exemples fonctionnent correctement
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

def test_config():
    """Test de la configuration"""
    try:
        from config import get_api_config, create_api_client
        
        print("🔧 Test de la configuration...")
        
        # Test de récupération de la config
        base_url, api_key = get_api_config()
        print(f"   ✅ URL de base: {base_url}")
        print(f"   ✅ Clé API: {'*' * (len(api_key) - 8) + api_key[-8:]}")
        
        # Test de création du client
        with create_api_client() as client:
            print("   ✅ Client API créé avec succès")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erreur de configuration: {e}")
        return False

def test_catalog_script():
    """Test du script de récupération du catalogue"""
    try:
        print("\n📊 Test du script de catalogue...")
        
        from get_catalog_metadata import get_catalog_metadata
        
        # Test avec un petit échantillon
        success = get_catalog_metadata(limit=2, show_details=False)
        
        if success:
            print("   ✅ Script de catalogue OK")
            return True
        else:
            print("   ❌ Script de catalogue en échec")
            return False
            
    except Exception as e:
        print(f"   ❌ Erreur dans le script de catalogue: {e}")
        return False

def test_records_script():
    """Test du script de récupération des records"""
    try:
        print("\n📋 Test du script de records...")
        
        from get_dataset_records import get_dataset_records
        
        # Test avec un petit échantillon
        success = get_dataset_records(max_datasets=1, records_per_dataset=1)
        
        if success:
            print("   ✅ Script de records OK")
            return True
        else:
            print("   ❌ Script de records en échec")
            return False
            
    except Exception as e:
        print(f"   ❌ Erreur dans le script de records: {e}")
        return False

def main():
    """Test principal"""
    print("=== 🧪 Tests des exemples Python ===\n")
    
    tests = [
        ("Configuration", test_config),
        ("Script Catalogue", test_catalog_script),
        ("Script Records", test_records_script)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except KeyboardInterrupt:
            print(f"\n⏹️ Tests interrompus par l'utilisateur")
            break
        except Exception as e:
            print(f"❌ Erreur critique dans {test_name}: {e}")
            failed += 1
    
    print(f"\n=== Résultats ===")
    print(f"✅ Tests réussis: {passed}")
    print(f"❌ Tests échoués: {failed}")
    
    if failed == 0:
        print("\n🎉 Tous les tests sont passés!")
        return True
    else:
        print(f"\n💥 {failed} test(s) en échec")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)