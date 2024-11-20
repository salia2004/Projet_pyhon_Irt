"""
Exercice 3 : Chiffrement et déchiffrement avec Vigenère

Ce programme implémente l'algorithme de chiffrement de Vigenère. Il permet :
- De chiffrer un texte clair avec une clé donnée.
- De déchiffrer un texte chiffré pour retrouver le texte original.

Fonctions principales :
- vigenere : Chiffre un texte avec la clé.
- vigenere_dechiffre : Déchiffre un texte chiffré avec la clé.
"""
def vigenere(texte_clair, cle):
    texte_clair=texte_clair.upper()
    cle=cle.upper()
    texte_crypter=""
    cle_repetee = (cle * ((len(texte_clair) // len(cle)) + 1))[:len(texte_clair)]
    indice=0
    for char in texte_clair:
        if char.isalpha():
            new_pos_text=ord(char)-ord('A')
            new_pos_cle=ord(cle_repetee[indice])-ord('A')
            texte_crypter+=chr(((new_pos_text + new_pos_cle) % 26 )+ ord('A'))
            indice=indice+1
        else:
            texte_crypter+=char
    return texte_crypter

def vigenere_dechiffre(texte_crypte, cle):
    cle = cle.upper()
    texte_crypte=texte_crypte.upper()
    cle_repetee = (cle * ((len(texte_crypte) // len(cle)) + 1))[:len(texte_crypte)]
    texte_clair = ""
    index_cle = 0

    for char in texte_crypte:
        if char.isalpha():
            pos_texte = ord(char) - ord('A')
            pos_cle = ord(cle_repetee[index_cle]) - ord('A')
            texte_clair += chr(((pos_texte - pos_cle) % 26 )+ ord('A'))
            index_cle =index_cle + 1
        else:
            texte_clair += char
    return texte_clair


