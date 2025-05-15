# Exercice 1
def selection_enclos(animaux:list[dict], num_enclos:int) -> list:
    selection = []
    for animal in animaux:
        if animal['enclos'] == num_enclos:
            selection.append(animal)

    return selection

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
{'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
{'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

assert selection_enclos(animaux, 5) == [{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
assert selection_enclos(animaux, 2) == [{'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2}]
assert selection_enclos(animaux, 7) == []

def trouver_intrus(tab, g, d):
    """Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans le tableau tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3."""
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1]: 
            return trouver_intrus(tab, indice, d)
        else:
            return trouver_intrus(tab, g, indice+1)

assert  trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8, 8], 0, 18) == 7
