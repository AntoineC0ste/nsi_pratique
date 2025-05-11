# Exercice 1
def ajoute_dictionnaire(d1:dict, d2:dict) -> dict:
    '''Ajoute les deux dictionnaires en paramètre'''
    d3 = {}
    for cle, valeur in d1.items():
        if cle in d2:
            d3[cle] = valeur + d2[cle]
        else:
            d3[cle] = valeur
    for cle, valeur in d2.items():
        if cle not in d3:
            d3[cle] = valeur 
    
    return d3

print(ajoute_dictionnaire({1: 5, 2: 7}, {2: 9, 3: 11}))

# Exercice 2
from random import randint

def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    nécessaire de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0
    while nombre_cases_vues < nombre_cases: 
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nombre_cases 
        if not cases_vues[case_en_cours]: 
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues + 1 
        n = n + 1 
    return n

