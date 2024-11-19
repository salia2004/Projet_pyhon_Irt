
#Fonction qui à partir d’un alphabet et d’une longueur k, générer toutes 
# les combinaisons possibles de longueur k avec les éléments de l'alphabet.
def mot_alphabet(k,alphabet):
    """    
    :param motif: decrit la structure des mots rechercher 
    :param alphabet: Alphabet utilisé pour générer les mots.
    :param mot: Mot a verifier
    :return:si le mot donner correspond ou pas au motif .
    """
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

#Fonction qui prend en parametre un alphabet et un motif et 
# retourne tout les mots de l'alphabet ayant ce motif 
def mot_motif(alphabet,motif):
    """    
    :param motif: decrit la structure des mots rechercher 
    :param alphabet: Alphabet utilisé pour générer les mots.
    :return: La liste des mots de ce motif construit avec l'alphabet.
    """
    mots=[]
    taille_mot=len(motif)
    structure_motif=[]
    # Recense la structure du motif (caractères fixes et leurs positions)
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


# Vérifie si un mot correspond à un motif donné
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

#Génère tous les mots correspondant à un motif
# Chaque élément du motif indique le nombre de répétitions consécutives de lettres
# Les lettres doivent être différentes les unes des autres
def mots_par_repetition(motif, alphabet):
    """    
    :param motif: Liste d'entiers décrivant les répétitions des lettres.
    :param alphabet: Alphabet utilisé pour générer les mots.
    :return: Liste de mots correspondant au motif.
    """
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
    """
    Génère et affiche toutes les chaînes alphanumériques commençant par une lettre et de longueur ≤ max_length.
    :param max_length: Longueur maximale des chaînes à générer.
    """
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
    #pour maxlenth=3 on a 203164 comme  resultat
    #Pour n=4 on a 12596220 comme resultat
    #et pour len=5 on une boucle infini  
