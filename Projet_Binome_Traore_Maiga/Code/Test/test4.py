import exercice4 as ex4

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
    alphabet = ['a', 'b']
    motif = ['a', '?', 'b']
    mot_valide = "acb"
    mot_invalide = "bbb"
    assert ex4.mot_correspond_motif(motif, alphabet, mot_valide) == True, f"Échec pour mot_correspond_motif({motif}, {alphabet}, {mot_valide})"
    assert ex4.mot_correspond_motif(motif, alphabet, mot_invalide) == False, f"Échec pour mot_correspond_motif({motif}, {alphabet}, {mot_invalide})"
    print(f"✔ Test réussi pour mot_correspond_motif({motif}, {alphabet}).")
    
    # Test 4 : mots_par_repetition
    print("\nTest de la fonction `mots_par_repetition`")
    alphabet = ['a', 'b']
    motif = [2, 1]
    resultat = ex4.mots_par_repetition(motif, alphabet)
    attendu = ['aab', 'abb', 'baa', 'bba']
    assert resultat == attendu, f"Échec pour mots_par_repetition({motif}, {alphabet}) : attendu {attendu}, obtenu {resultat}"
    print(f"✔ Test réussi pour mots_par_repetition({motif}, {alphabet}).")
    
    # Test 5 : Chaînes alphanumériques de longueur ≤ 3
    print("\nTest de la fonction `generer_chaines_alphanumeriques` avec longueur max = 3")
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    max_length = 3
    resultats = []
    for longueur in range(1, max_length + 1):
        combinaisons = ex4.mot_alphabet(longueur, alphabet)
        resultats.extend([mot for mot in combinaisons if mot[0].isalpha()])
    
    # Vérifier un nombre attendu de résultats
    attendu = 238328  # 62^3 combinaisons possibles pour longueur max = 3
    assert len(resultats) == attendu, f"Échec pour generer_chaines_alphanumeriques : attendu {attendu}, obtenu {len(resultats)}"
    print(f"✔ Test réussi pour generer_chaines_alphanumeriques avec longueur max = 3 (résultats : {len(resultats)}).")
    
    print("\nFin des tests pour l'Exercice 4 : Tous les tests ont réussi.\n")

