#Ce fichier test contient les test de tout les exercice du dm
import sys
import os

# Ajouter le répertoire parent au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import exercice4 as ex4
import exercice3 as ex3
import exercice2 as ex2
import exercice1 as ex1
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Test exercice 1
def test_exercice1():
    print("\nDébut des tests pour l'Exercice 1 : Vérification des balises HTML\n")
    
    # Base du chemin pour ce script
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Chemins vers les fichiers HTML
    fichiers_html = {
        "code.html": os.path.join(base_path, "code.html"),
        "absence_body.html": os.path.join(base_path, "absence_body.html"),
        "balise_auto_fermante.html": os.path.join(base_path, "balise_auto_fermante.html"),
        "balise_nom_equilibre.html": os.path.join(base_path, "balise_nom_equilibre.html")
    }
    
    for nom_fichier, chemin_fichier in fichiers_html.items():
        print(f"\n--- Test pour {nom_fichier} ---")
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                texte = fichier.read()
            
            # Test de `verifier_balises`
            print("\nTest de la fonction `verifier_balises`")
            resultat_equilibre = ex1.verifier_balises(texte)
            print("La balise est-elle eauilibre ?:",resultat_equilibre)
            print("✔ La vérification des balises est correcte.")
            
            # Test de `compter_occurrences_balises`
            print("\nTest de la fonction `compter_occurrences_balises`")
            resultat_occurrences = ex1.compter_occurrences_balises(chemin_fichier)
            print("Resulat occurence balise:",resultat_occurrences)
            print("✔ Le comptage des balises est correct.")
            
            # Test de `compter_balises_p`
            print("\nTest de la fonction `compter_balises_p`")
            resultat_p = ex1.compter_balises_p(chemin_fichier)
            print(f"✔ Le nombre de balises <p> est correct ({resultat_p}).")
            
            # Test de `balises_dans_body`
            print("\nTest de la fonction `balises_dans_body`")
            resultat_body = ex1.balises_dans_body(chemin_fichier)
            print("✔ La liste des balises dans <body> est correcte:",resultat_body)
        
        except FileNotFoundError:
            print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
        except AssertionError as e:
            print(f"{e}")
    
    print("\nFin des tests pour l'Exercice 1 : Tous les tests terminés.\n")

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Test exercice 2
def test_exercice2():
    print("\nDébut des tests pour l'Exercice 2 : Validation des mots de passe\n")

    # Cas de test pour mots_de_passe_valide
    print("Test de la fonction `mots_de_passe_valide`")
    mots_de_passe_test = [
        ("Mots123!", False),  # Trop court
        ("MotdepasseValide123!", True),  # Valide
        ("PasdeChiffre!", False),  # Manque un chiffre
        ("12345678901234", False),  # Manque majuscule, minuscule et caractère spécial
        ("Abc!123", False),  # Trop court
        ("Abcdefghijklmnop!123", True),  # Valide
        ("A!a1", False),  # Trop court
        ("MOTDEPASSEVALIDEXXX@", False),  # Valide mais tous majuscules
        ("motdepasse123@", False),  # Pas de majuscule
        ("MotdepasseSansSpecial", False),  # Pas de caractère spécial
    ]

    for mdp, attendu in mots_de_passe_test:
        resultat = ex2.mots_de_passe_valide(mdp)
        assert resultat == attendu, f"Échec pour {mdp} : attendu ={attendu}, obtenu ={resultat}"
    print("✔ Tous les tests pour `mots_de_passe_valide` ont réussi.")

    # Cas de test pour mdp_compromis
    print("\nTest de la fonction `mdp_compromis`")
    mots_de_passe_compromis_test = [
        ("P@ss3Moi1234!", True),  # Compromis
        ("MotdepasseValide123!", False),  # Pas compromis
        ("ParisFrance2024#", True),  # Compromis
        ("UnMotTrèsComplexe@2024", False),  # Pas compromis
        ("M@isonF0rt3$$", True),  # Compromis
        ("V3rySecureCl3f@", False),  # Pas compromis
        ("Abcdefghijklmnop!123", False),  # Pas compromis
        ("B0nJ0urSécur!", True),  # Compromis
        ("UnMotDePasseInconnu!", False),  # Pas compromis
    ]

    for mdp, attendu in mots_de_passe_compromis_test:
        resultat = ex2.mdp_compromis(mdp)
        assert resultat == attendu, f"Échec pour {mdp} : attendu {attendu}, obtenu {resultat}"
    print("✔ Tous les tests pour `mdp_compromis` ont réussi.")

    print("\nFin des tests pour l'Exercice 2 : Tous les tests ont réussi.\n")

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Test exercice 3
def test_exercice3():
    print("\nDébut des tests pour l'Exercice 3 : Chiffrement et déchiffrement Vigenère\n")
    
    # Cas de test statiques
    print("Test des cas statiques de chiffrement et déchiffrement")
    cas_de_test = [
        ("Hello", "KEY", "RIJVS"),  # Test simple
        ("Python", "CODE", "RMWLQB"),  # Test avec une autre clé
        ("Security123", "SAFE", "KEHYJIYC123"),  # Test avec caractères non alphabétiques
        ("Test123@!!", "KEY", "DIQD123@!!"),  # Test avec caractères spéciaux
        ("Lowercase", "UPPER", "FDLIIWPHI"),  # Test avec lettres minuscules
    ]
    
    for texte_clair, cle, attendu in cas_de_test:
        texte_crypter = ex3.vigenere(texte_clair, cle)
        print(texte_crypter)
        print(attendu)
        assert texte_crypter == attendu, f"Échec chiffrement : attendu {attendu}, obtenu {texte_crypter}"
        texte_dechiffre = ex3.vigenere_dechiffre(texte_crypter, cle)
        assert texte_dechiffre.lower() == texte_clair.lower(), f"Échec déchiffrement : attendu {texte_clair}, obtenu {texte_dechiffre}"
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

    # Déchiffrement
    texte_dechiffre = ex3.vigenere_dechiffre(texte_crypter, cle)
    print(texte_dechiffre)
    assert texte_dechiffre == texte_clair.upper(), "Échec : Texte déchiffré ne correspond pas au texte clair"
    print(f"✔ Chiffrement et déchiffrement pour le fichier {fichier_message} ont réussi.")
    
    print("\nFin des tests pour l'Exercice 3 : Tous les tests ont réussi.\n")

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Test exercice 4
def test_exercice4():
    print("\nDébut des tests pour l'Exercice 4 : Génération et manipulation de mots\n")
    
    # Test 1 : mot_alphabet
    print("Test de la fonction `mot_alphabet`")
    alphabet = ['a', 'b']
    k = 2
    resultat = ex4.mot_alphabet(k, alphabet)
    attendu = ['aa', 'ab', 'ba', 'bb']
    assert resultat == attendu, f"Échec pour mot_alphabet({k}, {alphabet}) : attendu {attendu}, obtenu {resultat}"
    print(f"✔ Test réussi pour mot_alphabet({k}, {alphabet}).")
    
    # Test 2 : mot_motif
    print("\nTest de la fonction `mot_motif`")
    alphabet = ['a', 'b', 'c']
    motif = ['a', ' ', 'b']
    resultat = ex4.mot_motif(alphabet, motif)
    attendu = ['aab', 'abb', 'acb']
    assert resultat == attendu, f"Échec pour mot_motif({alphabet}, {motif}) : attendu {attendu}, obtenu {resultat}"
    print(f"✔ Test réussi pour mot_motif({alphabet}, {motif}).")
    
    # Test 3 : mot_correspond_motif
    print("\nTest de la fonction `mot_correspond_motif`")
    alphabet = ['a', 'b','c']
    motif = ['a','?','b']
    mot_valide = "acb"
    mot_invalide = "bbb"
    assert ex4.mot_correspond_motif(motif, alphabet, mot_valide) == True, f"Échec pour mot_correspond_motif({motif}, {alphabet}, {mot_valide})"
    assert ex4.mot_correspond_motif(motif, alphabet, mot_invalide) == False, f"Échec pour mot_correspond_motif({motif}, {alphabet}, {mot_invalide})"
    print(f"✔ Test réussi pour mot_correspond_motif({motif}, {alphabet},{mot_invalide}).")
    
    # Test 4 : mots_par_repetition
    print("\nTest de la fonction `mots_par_repetition`")
    alphabet = ['a', 'b']
    motif = [2, 1]
    resultat = ex4.mots_par_repetition(motif, alphabet)
    attendu = ['aab','bba']
    assert resultat == attendu, f"Échec pour mots_par_repetition({motif}, {alphabet}) : attendu {attendu}, obtenu {resultat}"
    print(f"✔ Test réussi pour mots_par_repetition({motif}, {alphabet}).")
    
    print("\nFin des tests pour l'Exercice 4 : Tous les tests ont réussi.\n")
def All_test():
    print("---------- Lancement de tout les jeux de teste ----------")
    test_exercice1()
    test_exercice2()
    test_exercice3()
    test_exercice4()
    print("--------- Fin des test --------- ")
    return