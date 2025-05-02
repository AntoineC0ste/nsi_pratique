coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        un "*" , les 0 par une espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = []
    for elt in liste_depart : 
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois 
       ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k) 
        for i in range(k):
            grille_zoomee.append(ligne_zoomee) 
    return grille_zoomee

affiche(dessin_zoom(coeur, 10))

# Exercice 1

def moyenne(notes:list[tuple[float:float]]) -> float:
    '''Renvoie la moyenne des notes spécifiées sous la forme (note, coef).'''
    notes_coef = [note[0]*note[1] for note in notes]
    notes_tot = 0
    for note in notes_coef:
        notes_tot += note
    
    if notes_tot != 0:
        return notes_tot/sum([coef[1] for coef in notes])
    
    return None

print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))

print(moyenne([(3, 0), (5, 0)]))