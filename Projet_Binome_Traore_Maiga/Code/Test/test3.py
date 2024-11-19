import exercice3 as ex3

def test_exercice3():
    print("\nDébut des tests pour l'Exercice 3 : Chiffrement et déchiffrement Vigenère\n")
    
    # Cas de test statiques
    print("Test des cas statiques de chiffrement et déchiffrement")
    cas_de_test = [
        ("HELLO", "KEY", "RIJVS"),  # Test simple
        ("PYTHON", "CODE", "RAVRJL"),  # Test avec une autre clé
        ("SECURITY123", "SAFE", "UMKYQWYQ123"),  # Test avec caractères non alphabétiques
        ("TEST123@!!", "KEY", "UIVU123@!!"),  # Test avec caractères spéciaux
        ("LOWERCASE", "UPPER", "MOPGDKLKQ"),  # Test avec lettres minuscules
    ]
    
    for texte_clair, cle, attendu in cas_de_test:
        texte_crypter = ex3.vigenere(texte_clair, cle)
        assert texte_crypter == attendu, f"Échec chiffrement : attendu {attendu}, obtenu {texte_crypter}"
        texte_dechiffre = ex3.vigenere_dechiffre(texte_crypter, cle)
        assert texte_dechiffre == texte_clair.lower(), f"Échec déchiffrement : attendu {texte_clair.lower()}, obtenu {texte_dechiffre}"
    print("✔ Tous les tests statiques ont réussi.")
    
    # Test avec un fichier
    print("\nTest avec un fichier texte")
    def lire_fichier(nom_fichier):
        with open(nom_fichier, 'r') as f:
            return f.read()

    fichier_message = "message.txt"
    cle = "mystere"
    texte_clair = lire_fichier(fichier_message)
    
    # Chiffrement
    texte_crypter = ex3.vigenere(texte_clair, cle)
    print("Texte cryptogramme généré :")
    print(texte_crypter[:100] + "...")  # Afficher les 100 premiers caractères du cryptogramme

    # Déchiffrement
    texte_dechiffre = ex3.vigenere_dechiffre(texte_crypter, cle)
    assert texte_dechiffre == texte_clair.lower(), "Échec : Texte déchiffré ne correspond pas au texte clair"
    print("✔ Chiffrement et déchiffrement pour le fichier ont réussi.")
    
    print("\nFin des tests pour l'Exercice 3 : Tous les tests ont réussi.\n")
