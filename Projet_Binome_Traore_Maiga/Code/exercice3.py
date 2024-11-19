def vigenere(texte_clair, cle):
    texte_clair=texte_clair.upper()
    cle=cle.upper()
    texte_crypter=""
    indice=0
    for char in texte_clair:
        if char.isalpha():
            new_pos_text=ord(char)-ord('A')
            new_pos_cle=ord(cle[indice%len(cle)])-ord('A')
            texte_crypter+=chr(((new_pos_text + new_pos_cle) % 26 )+ ord('A'))
            indice=indice+1
        else:
            texte_crypter+=char
    return texte_crypter

def vigenere_dechiffre(texte_crypte, cle):
    cle = cle.upper()
    texte_crypte=texte_crypte.upper()
    #cle_repetee = (cle * ((len(texte_crypte) // len(cle)) + 1))[:len(texte_crypte)]
    texte_clair = ""
    index_cle = 0

    for char in texte_crypte:
        if char.isalpha():
            pos_texte = ord(char) - ord('A')
            pos_cle = ord(cle[index_cle%len(cle)]) - ord('A')
            texte_clair += chr(((pos_texte - pos_cle) % 26 )+ ord('A'))
            index_cle =index_cle + 1
        else:
            texte_clair += char
    return texte_clair


