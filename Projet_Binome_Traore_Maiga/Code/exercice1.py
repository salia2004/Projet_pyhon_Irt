#_________Question 1 ______________
#Équilibrage des Balises HTML

liste_balise = [
    # Balises ouvrante avec fermeture obligatoire
    "html", "head", "title", "body", "h1", "h2", "h3", "h4", "h5", "h6",
    "p", "div", "span", "a", "ul", "ol", "li", "table", "tr", "td", "th",
    "form", "label", "button", "strong", "em", "b", "i", "small",
    "blockquote", "pre", "code", "nav", "header", "footer", "section",
    "article", "aside", "main", "figure", "figcaption", "video", "audio",
    "canvas", "svg", "iframe", "object", "script", "style", "map",
    "noscript",
    # Balises fermante
    "/html", "/head", "/title", "/body", "/h1", "/h2", "/h3", "/h4", "/h5", "/h6",
    "/p", "/div", "/span", "/a", "/ul", "/ol", "/li", "/table", "/tr", "/td", "/th",
    "/form", "/label", "/button", "/strong", "/em", "/b", "/i", "/small",
    "/blockquote", "/pre", "/code", "/nav", "/header", "/footer", "/section",
    "/article", "/aside", "/main", "/figure", "/figcaption", "/video", "/audio",
    "/canvas", "/svg", "/iframe", "/object", "/script", "/style", "/map",
    "/noscript",
]
balise_auto_fermante=[ # Balises auto-fermantes (sans fermeture obligatoire)
    "img", "br", "hr", "input", "meta", "link", "source", "area",
    "base", "col", "embed", "param", "track", "wbr"]

# Fonction pour extraire les balises d'un texte HTML
def extraire_balise(text):
    liste = []
    i = 0
    while i < len(text): 
        balise = ""
        if text[i] == '<':
            j = i + 1
            while j < len(text) and text[j] != '>':
                balise += text[j]
                j += 1
            # Isoler uniquement le nom de la balise (avant les espaces ou attributs)
            balise_nom = balise.split()[0]  # Garde tout avant le premier espace
            if balise_nom in liste_balise or balise_nom in balise_auto_fermante:  # Vérifie dans les listes de balises
                liste.append(balise_nom)
            i = j
        else:
            i += 1  # Avancer si on n'est pas sur une balise
    return liste


#retourne vrai si les balise d'un code html sont bien equilibrée
def verifier_balises(text_html):
    liste_balise=extraire_balise(text_html)
    pile_balise=[]
    for balise in liste_balise:
        balise_nom = balise.split()[0]
        if (not balise_nom.startswith('/')) and (balise_nom not in balise_auto_fermante):
            pile_balise.append(balise_nom)
        else:
            # Cas d'une balise fermante
            if balise_nom.startswith('/'):
                balise_fermant = balise_nom[1:]  # Nom sans le "/"
                if not pile_balise or pile_balise[-1] != balise_fermant:
                    return False  # Balise fermante ne correspond pas
                pile_balise.pop()
    return len(pile_balise) == 0

#fonction qui ocmpte les occurence d'un balise dans texte HTML et renvoi un dictionnaire qui a chaque balise fait correspondre son occcurence
def compter_occurrences_balises(fichier_html):
    compteur = {}  # Dictionnaire pour stocker les occurrences des balises
    try:
        # Ouvrir et lire le contenu du fichier HTML
        with open(fichier_html, 'r', encoding='utf-8') as fichier:
            texte = fichier.read()  # Lire le contenu du fichier
        #verifier la validite du texte
        if verifier_balises(texte):
            liste_balises = extraire_balise(texte)  
            # Parcourir la liste des balises et compter les occurrences des balises ouvrantes
            for tag in liste_balises:
                tag = tag.split()[0]  # Prendre uniquement le nom de la balise
                if not tag.startswith('/'):  # Vérifie si c'est une balise ouvrante
                    if tag in compteur:
                        compteur[tag] += 1
                    else:
                        compteur[tag] = 1
        return compteur
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_html} est introuvable.")
        return {}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {}
#_________Question 2 ______________

def compter_balises_p(fichier_html):
    compte=0#compter du nombre de balise <p>
    try:
        with open(fichier_html, 'r', encoding='utf-8') as fichier:
            texte = fichier.read()  # Lire le contenu du fichier
        liste_balises = extraire_balise(texte)  
        # Parcourir la liste des balises et compter les occurrences des balises ouvrantes
        for tag in liste_balises:
            if tag=='p':
                compte+=1
        return compte
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_html} est introuvable.")
        return {}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return 0

def balises_dans_body(fichier_html):
    try:
        with open(fichier_html, 'r', encoding='utf-8') as fichier:
            texte = fichier.read()  # Lire le contenu du fichier
        liste_balises = extraire_balise(texte) 
        if 'body' not in liste_balises or '/body' not in liste_balises:
            print("Erreur : La balise <body> ou </body> est absente.")
            return []
        i=0 
        retour=[]
        while liste_balises[i]!='body':
            i+=1
        j=i+1
        while liste_balises[j]!='/body':
            retour.append(liste_balises[j])
            j+=1
        return retour
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_html} est introuvable.")
        return [ ]
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return [ ]