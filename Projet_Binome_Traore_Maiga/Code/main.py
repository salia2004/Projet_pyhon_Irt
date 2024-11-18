import exercice1 as ex1
import exercice2 as ex2
import exercice4 as ex4
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
    mdp_compromis="ParisFrance2024#"
    print("le mode de passe ",mdp1,"est t-il valide ?:",ex2.mots_de_passe_valide(mdp1))
    print("le mode de passe ",mdp2,"est t-il valide ?:",ex2.mots_de_passe_valide(mdp2))
    print("le mode de passe ",mdp3,"est t-il valide ?:",ex2.mots_de_passe_valide(mdp3))
    print("le mode de passe ",mdp4,"est t-il valide ?:",ex2.mots_de_passe_valide(mdp4))
    print("le mode de passe ",mdp5,"est t-il valide ?:",ex2.mots_de_passe_valide(mdp5))
    print("le mode de passe ",mdp_compromis,"est t-il valide ?:",ex2.mots_de_passe_valide(mdp_compromis))
    print("le mode de passe ",mdp_compromis," Est-il compromis ?:",ex2.mdp_compromis(mdp_compromis))


    # Tester l'Exercice 3



    # Tester l'Exercice 4
    #-----------------Question 1
    alphabet = ['a', 'b']
    k = 3
    resultat = ex4.mot_alphabet(k, alphabet)
    print(f"Tous les mots de longueur {k} définis sur l'alphabet {alphabet} sont :",resultat)
    alphabet = ['a', 'b','c']
    k = 4
    resultat = ex4.mot_alphabet(k, alphabet)
    print(f"Tous les mots de longueur {k} définis sur l'alphabet {alphabet} sont :",resultat)
    alphabet = ['a', 'b','b']
    print(len(alphabet))
    k = 4
    resultat = ex4.mot_alphabet(k, alphabet)
    print(f"Tous les mots de longueur {k} définis sur l'alphabet {alphabet} sont :",resultat)


    #-----------------Question 2
    #-----------------Question 2.1
    alphabet = ['a', 'b', 'c']
    motif = ['a', ' ', ' ']
    resultat_motif = ex4.mot_motif(alphabet, motif)
    print(f"Les mots correspondant au motif {motif} dans l'alphabet {alphabet} sont :")
    print(resultat_motif)
    alphabet = ['a', 'b', 'c']
    motif = [' ', ' ', ' ']
    resultat_motif = ex4.mot_motif(alphabet, motif)
    print(f"Les mots correspondant au motif {motif} dans l'alphabet {alphabet} sont :")
    print(resultat_motif)
    alphabet = ['a', 'b', 'c']
    motif = ['a', 'b', ' ']
    resultat_motif = ex4.mot_motif(alphabet, motif)
    print(f"Les mots correspondant au motif {motif} dans l'alphabet {alphabet} sont :")
    print(resultat_motif)

    #-----------------Question 2.2
    #---- Programme permetant d'affihcer toute les chaines alphanumerique commencant par une lettre et de logueur 5----
    


    #-----------------Question 3
    alphabet = '01'
    motif = ['0', '?', '1']
    mot = "011"
    mot1 = "010"

    resultat = ex4.mot_correspond_motif(motif, alphabet, mot)
    resultat1 = ex4.mot_correspond_motif(motif, alphabet, mot1)
    print(f"Le mot '{mot}' correspond-il au motif {motif} ? {resultat}")
    print(f"Le mot '{mot1}' correspond-il au motif {motif} ? {resultat1}")

    #-----------------Question 4
    alphabet = 'abc'
    # Une lettre répétée 2 fois, puis une autre 3 fois, puis une autre 1 fois
    motif = [2, 3, 1]  
    resultat = ex4.mots_par_repetition(motif, alphabet)
    print(f"Les mots correspondant au motif {motif} sont :")
    print(resultat)

if __name__ == "__main__":
    main()