def vigenere_chiffre(texte_clair,cle):
    #Si la longueur de la clé est inférierieure à la longueur du texte clair, le répéter jusqu'à ce qu'il ait la même longueur
    if len(cle)<len(texte_clair):
        #// pour donner cbm de fois la clé peu être répétée
        #Garantie de la clé aura exactement la meme longueur que le texte clair
        cle = (cle * ((len(texte_clair) // len(cle)) + 1))[:len(texte_clair)]
    #initalisation message crypté
    cryptogramme=""
    #parcourir le texte en clair
    for i in range (len(texte_clair)):
        lettre_texte=texte_clair[i]
        lettre_cle=cle[i]
        if lettre_texte.isalpha():
            #Trouver la position des lettre
            #avec cette opération postion entre 0(A) et 25 (Z)
            position_texte=ord(lettre_texte.upper())-ord('A')
            position_cle=ord(lettre_cle.upper())-ord('A')

            #calcul de la postion du message crypté
            position_chiffree= (position_texte+position_cle)%26
            # Convertir la position obtenue en lettre
            if lettre_texte.isupper():
                    cryptogramme += chr(position_chiffree + ord('A'))
            else :
                    cryptogramme += chr(position_chiffree + ord('a'))
        else:
            # Si ce n'est pas une lettre, on l'ajoute directement au cryptogramme
            cryptogramme += lettre_texte
    return cryptogramme

def vigenere_dechiffre(texte_crypte,cle) :
     #Si la longueur de la clé est inférierieure à la longueur du texte clair, le répéter jusqu'à ce qu'il ait la même longueur
    if len(cle)<len(texte_crypte):
        #// pour donner cbm de fois la clé peu être répétée
        #Garantie de la clé aura exactement la meme longueur que le texte clair
        cle = (cle * ((len(texte_crypte) // len(cle)) + 1))[:len(texte_crypte)]
    #initalisation message crypté
    texte_clair=""
    #parcourir le texte en clair
    for i in range (len(texte_crypte)):
        lettre_texte=texte_crypte[i]
        lettre_cle=cle[i]
        if lettre_texte.isalpha():
            #Trouver la position des lettre
            #avec cette opération postion entre 0(A) et 25 (Z)
            position_texte=ord(lettre_texte.upper())-ord('A')
            position_cle=ord(lettre_cle.upper())-ord('A')

            #calcul de la postion du message crypté
            position_dechiffree= (position_texte-position_cle)%26
            # Convertir la position obtenue en lettre
            if lettre_texte.isupper():
                    texte_clair += chr(position_dechiffree + ord('A'))
            else :
                    texte_clair+= chr(position_dechiffree + ord('a'))
        else:
            # Si ce n'est pas une lettre, on l'ajoute directement au cryptogramme
            texte_clair += lettre_texte
    return texte_clair
