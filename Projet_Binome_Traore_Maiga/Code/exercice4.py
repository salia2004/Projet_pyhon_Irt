
"""
Exercice 4 : Génération et manipulation de mots basés sur un alphabet

Ce programme génère des combinaisons de mots basées sur un alphabet et
des motifs spécifiques. Il offre des outils pour :
- Générer toutes les combinaisons possibles pour une longueur donnée.
- Créer des mots respectant un motif défini.
- Vérifier si un mot correspond à un motif.
- Générer des mots basés sur des répétitions spécifiques de lettres.

Fonctions principales :
- mot_alphabet : Génère toutes les combinaisons possibles d'un alphabet.
- mot_motif : Génère des mots respectant un motif donné.
- mot_correspond_motif : Vérifie si un mot correspond à un motif.
- mots_par_repetition : Génère des mots selon un motif de répétition.
-generer_chaine_alphanumerique :Génère et affiche toutes les chaînes alphanumériques commençant par une lettre et de longueur ≤ 5
"""

def mot_alphabet(k,alphabet):
    combinaison=[]#liste de scombinaison possible
    if k<=0:
        print("Erreur  : un mot de longueur 0 ne peut etre generer ")
        return [ ]
    if k==1:
        return alphabet
    else:
        # Fonction récursive pour construire les mots
        def construire_mots(prefixe, longueur_restante):
            if longueur_restante == 0:
                combinaison.append(prefixe)
                return
            for lettre in alphabet:
                construire_mots(prefixe + lettre, longueur_restante - 1)
        
        # Démarrer la construction des mots
        construire_mots("", k)
        return combinaison


def mot_motif(alphabet,motif):
    mots=[]
    taille_mot=len(motif)
    structure_motif=[]
    # Recense les caractères fixes et leurs positions
    for i, char in enumerate(motif):
        if char != " ":
            structure_motif.append((char, i))
    liste_mots=mot_alphabet(taille_mot,alphabet)
    for mot in liste_mots:
        est_motif=True
        for (m,indice) in structure_motif:
            if (mot[indice]!=m):#si un element fixe du motif ne correspond pas on enleve le mots
                est_motif=False
        if est_motif:
            mots.append(mot)
    return mots



def mot_correspond_motif(motif, alphabet, mot):
    """    
    :param motif: decrit la structure des mots rechercher 
    :param alphabet: Alphabet utilisé pour générer les mots.
    :param mot: Mot a verifier
    :return:si le mot donner correspond ou pas au motif .
    """
    # Vérifie si la longueur du mot correspond à celle du motif
    if len(mot) != len(motif):
        return False
    # Vérifie chaque caractère du mot par rapport au motif
    for i, char in enumerate(motif):
        if char != '?':  # Si le caractère du motif est fixe
            if char != mot[i]:  # Le caractère doit correspondre exactement
                return False
        elif mot[i] not in alphabet:  # Si le caractère n'est pas dans l'alphabet
            return False
    # Si toutes les conditions sont remplies, le mot correspond au motif
    return True


def mots_par_repetition(motif, alphabet):
    resultats = [''] 
    for repetitions in motif:
        nouveaux_resultats = []
        for mot in resultats:
            # Pour chaque lettre de l'alphabet
            for lettre in alphabet:
                if not mot or lettre != mot[-1]:
                    # Construire une nouvelle séquence et l'ajouter
                    nouveaux_resultats.append(mot + lettre * repetitions)
        resultats = nouveaux_resultats
    return resultats

def generer_chaines_alphanumeriques():
    max_length=5
    alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    resultats = []
    for longueur in range(1, max_length + 1):
        # Générer toutes les combinaisons de cette longueur
        combinaisons = mot_alphabet(longueur, alphabet)
        # Filtrer celles qui commencent par une lettre
        resultats.extend([mot for mot in combinaisons if mot[0].isalpha()])
    
    # Afficher les résultats
    print("Chaînes alphanumériques générées (longueur ≤ 5) :")
    for mot in resultats:
        print(mot)
    print(len(resultats))
    #pour  max_length  = 3 on a 203164 element comme  resultat
    #Pour max_length =4 on a 12596220 element comme resultat
    #et pour  max_length  =5 on une boucle infini  
