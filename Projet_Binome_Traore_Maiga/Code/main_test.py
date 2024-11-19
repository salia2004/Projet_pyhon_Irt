
import test as t
def main():
    while True:
        print("\nFaites votre choix:")
        print("1 - Lancer la fonction de Test de l'exercice 1")
        print("2 - Lancer la fonction de Test de l'exercice 2")
        print("3 - Lancer la fonction de Test de l'exercice 3")
        print("4 - Lancer la fonction de Test de l'exercice 4")
        print("5 - Lancer toutes les fonctions de test")
        print("0 - Quitter")

        try:
            choix = int(input("Entrez votre choix : "))
            if choix == 1:
                t.test_exercice1()
            elif choix == 2:
                t.test_exercice2()
            elif choix == 3:
                t.test_exercice3()
            elif choix == 4:
                t.test_exercice4()
            elif choix == 5:
                t.All_test()
            elif choix == 0:
                print("Au revoir !")
                break
            else:
                print("Choix invalide, veuillez entrer un nombre entre 0 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
if __name__ == "__main__":
    main()
