
def a_minuscule(p):
    for elem in p:
        if 'a'<= elem <= 'z':
            return True
    return False
def a_majuscule(p):
    for elem in p:
        if 'A'<= elem <= 'Z':
            return True
    return False

def a_chiffre(p):
    for elem in p:
        if elem.isdigit():  # Vérifie si le caractère est un chiffre
            return True
    return False
def a_caractere(p):
    car=['!','@','#','$','%','^','&','*']
    for elem in p:
        if elem in car:
            return True
    return False

def mots_de_passe_valide(password):
    if a_minuscule(password) and a_majuscule(password) and a_chiffre(password) and a_caractere(password) and len(password)>=12:
        return True
    return False

def mdp_compromis(password):
    #faire une liste de mot de passe compromis
    return True