
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

#Liste non exhaustive de mot de passe valide mai compromis 
mots_de_passe_compromis = [
    "P@ss3Moi1234!",
    "J@imeLaSécur1té",
    "F0rt&Invi$ibl3",
    "S0usL@Cl3f22!",
    "T0ujoursPr3$ent",
    "Sécur1t3Max!!",
    "Pr0tégez-Vous!",
    "P@sDAcc3ss2023",
    "V!veL3C@fé22",
    "R3ndezM0nArg$",
    "UnCl3fP@rfaite",
    "M@isonF0rt3$$",
    "B0nJ0urSécur!",
    "M3ttreUneC0dé$",
    "F@it3sMoiP@ss",
    "T3rr3DAs!le22",
    "J@am@isT0uché!",
    "Cl3fEnMain!!",
    "R!enÀC@ss3r99",
    "M@gn!fiqueClé",
    "Ch@tDuSo!r11$",
    "V3nteD'Acc3s!",
    "T0uj0ursV!g!l",
    "UnC@deau2023!",
    "M0ntagneD0rée",
    "P@r0lE$Sécur!",
    "S@nsTr0u3ble$",
    "N0ublieP@rF!t",
    "L3C0ffreF0rt!",
    "V3ryS@feCl3f",
    "L@VieSécurée",
    "L!brair!3Déf$",
    "Ch@mbreSecrète",
    "R3p0s@ssur@nt",
    "F0r3tDeC0d3!",
    "UnP@ss3M@gik",
    "M3sB!jouX$$",
    "J@rd!nSecret3",
    "Tr3sC0mpl3x!!",
    "Sécur!téL3git",
    "B@liseDuWeb1",
    "UnTrés0rL0ck",
    "B@teauDArg3nt",
    "Cl@rtéDeP@$$",
    "F0rmuleIdéal!",
    "G!g@B!teC0dé",
    "M0nneie123!$",
    "Préc@ution!!1",
    "D@ngerL3ss$",
    "ParisFrance2024#"
]
def mdp_compromis(password):
    #faire une liste de mot de passe compromis
    if password in mots_de_passe_compromis:
        return True
    return False