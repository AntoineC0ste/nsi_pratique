# Exercice 1
class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

def taille(abr:Noeud) -> int:
    if abr == None or abr.v == None:
        return 0
    
    return 1 + taille(abr.gauche) + taille(abr.droit)

def hauteur(abr:Noeud) -> int:
    if abr == None or (abr.droit == None and abr.gauche == None):
        return 0
    
    return 1 + hauteur(abr.gauche) + hauteur(abr.droit)
    

a = Noeud(1, Noeud(4, None, None),
    Noeud(0, None,
             Noeud(7, Noeud(9, None, None), None)))

assert taille(a) == 5
assert hauteur(a) == 3, f'{hauteur(a)}'


# Exercice 2
def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i] 
    tab_ins[indice] =  element
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1]
    return tab_ins


assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(0, 4, [7, 8, 9]) == [4, 7, 8, 9]