
#Fonction qui à partir d’un alphabet et d’une longueur k, générer toutes 
# les combinaisons possibles de longueur k avec les éléments de l'alphabet.
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


#Vérifie si un mot correspond à un motif donné sur un alphabet
def mot_correspond_motif(motif, alphabet, mot):
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

#Génère tous les mots correspondant au motif fourni où les lettres sont répétées
# selon le tableau d'entiers `motif`.
def mots_par_repetition(motif, alphabet):
    liste=[]
    #nous représentons les mots par un tableau d’entiers Nb_carac qui décrit la taille des séquences de lettres identiques.

    return liste