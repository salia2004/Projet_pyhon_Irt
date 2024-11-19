import sys
import os

# Ajouter le répertoire parent au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# Importer exercice1
import exercice1 as ex1

def test_exercice1():
    print("\nDébut des tests pour l'Exercice 1 : Vérification des balises HTML\n")
    
    # Base du chemin pour ce script
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Chemins vers les fichiers HTML
    fichiers_html = {
        "code.html": os.path.join(base_path, "code.html"),
        "absence_body.html": os.path.join(base_path, "absence_body.html"),
        "balise_auto_fermante.html": os.path.join(base_path, "balise_auto_fermante.html"),
        "balise_nom_equilibre.html": os.path.join(base_path, "balise_nom_equilibre.html")
    }
    
    for nom_fichier, chemin_fichier in fichiers_html.items():
        print(f"\n--- Test pour {nom_fichier} ---")
        
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                texte = fichier.read()
            
            # Test de `verifier_balises`
            print("\nTest de la fonction `verifier_balises`")
            resultat_equilibre = ex1.verifier_balises(texte)
            print("✔ La vérification des balises est correcte.")
            
            # Test de `compter_occurrences_balises`
            print("\nTest de la fonction `compter_occurrences_balises`")
            resultat_occurrences = ex1.compter_occurrences_balises(chemin_fichier)
            print("✔ Le comptage des balises est correct.")
            
            # Test de `compter_balises_p`
            print("\nTest de la fonction `compter_balises_p`")
            resultat_p = ex1.compter_balises_p(chemin_fichier)
            print(f"✔ Le nombre de balises <p> est correct ({resultat_p}).")
            
            # Test de `balises_dans_body`
            print("\nTest de la fonction `balises_dans_body`")
            resultat_body = ex1.balises_dans_body(chemin_fichier)
            print("✔ La liste des balises dans <body> est correcte.")
        
        except FileNotFoundError:
            print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
        except AssertionError as e:
            print(f"❌ {e}")
    
    print("\nFin des tests pour l'Exercice 1 : Tous les tests terminés.\n")

if __name__ == "__main__":
    test_exercice1()
