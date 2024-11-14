import exercice1 as ex1
import exercice2 as ex2
fichier_html="code.html"
def main():
    # Tester l'Exercice 1
    #-----------------Question 1
    with open(fichier_html, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()  # Lire le contenu du fichier
    print("Test de l'équilibrage des balises HTML :", ex1.verifier_balises(texte))
    print("Comptage des balises dans le fichier HTML :", ex1.compter_occurrences_balises(fichier_html))
    #-----------------Question 2
    print("Nombre de balises <p> dans le code HTML {fichier_html}:", ex1.compter_balises_p(fichier_html))
    print("Balises dans la section <body> :", ex1.balises_dans_body(fichier_html))




    # Tester l'Exercice 2
    #-----------------Question 
    mdp1="Paul09@"
    mdp2="jgfihgijb0ihvhiKgf"
    mdp3="PaulSabation#@#"
    mdp4="PAULSABTIET67#@"
    mdp5="PaulSabatier2024#"
    print("le mode de passe ",mdp1,":",ex2.mots_de_passe_valide(mdp1))
    print("le mode de passe ",mdp2,":",ex2.mots_de_passe_valide(mdp2))
    print("le mode de passe ",mdp3,":",ex2.mots_de_passe_valide(mdp3))
    print("le mode de passe ",mdp4,":",ex2.mots_de_passe_valide(mdp4))
    print("le mode de passe ",mdp5,":",ex2.mots_de_passe_valide(mdp5))
    # Tester l'Exercice 3



    # Tester l'Exercice 4

if __name__ == "__main__":
    main()