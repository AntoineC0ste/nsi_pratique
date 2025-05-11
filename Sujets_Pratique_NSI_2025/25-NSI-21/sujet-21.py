# Exercice 1
def indices_max(tab:list) -> tuple:
    maxi = tab[0]
    occurences = []
    for nombre in tab:
        if nombre > maxi:
            maxi = nombre
    for i in range(len(tab)):
        if tab[i] == maxi:
            occurences.append(i)

    return (maxi, occurences)

# Exercice 2
def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse 


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        entier = pile.pop() 
        if entier >= 0: 
            pile_positifs.append(entier)
    return pile_positifs

L = renverse([1,2,3, -6])
print(L)
print(positifs(L))
