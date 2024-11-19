import exercice2 as ex2

def test_exercice2():
    print("\nDébut des tests pour l'Exercice 2 : Validation des mots de passe\n")

    # Cas de test pour mots_de_passe_valide
    print("Test de la fonction `mots_de_passe_valide`")
    mots_de_passe_test = [
        ("Motdepasse123!", False),  # Trop court
        ("MotdepasseValide123!", True),  # Valide
        ("PasdeChiffre!", False),  # Manque un chiffre
        ("12345678901234", False),  # Manque majuscule, minuscule et caractère spécial
        ("Abc!123", False),  # Trop court
        ("Abcdefghijklmnop!123", True),  # Valide
        ("A!a1", False),  # Trop court
        ("MOTDEPASSEVALIDEXXX@", True),  # Valide mais tous majuscules
        ("motdepasse123@", False),  # Pas de majuscule
        ("MotdepasseSansSpecial", False),  # Pas de caractère spécial
    ]

    for mdp, attendu in mots_de_passe_test:
        resultat = ex2.mots_de_passe_valide(mdp)
        assert resultat == attendu, f"Échec pour {mdp} : attendu {attendu}, obtenu {resultat}"
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
