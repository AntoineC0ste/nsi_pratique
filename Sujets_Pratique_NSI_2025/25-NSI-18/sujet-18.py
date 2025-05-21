# Exercice 1
def moyenne(tab:list) -> float:
    num = 0
    denum = len(tab)

    for elt in tab:
        num += elt
    
    return num/denum

assert moyenne([1])
assert  moyenne([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert moyenne([1, 2]) == 1.5



# Exercice 2
def dichotomie(tab, x):
    """applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = len(tab[debut:fin])
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False


assert  dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
assert not  dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27)
assert not dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 1)
assert not  dichotomie([], 28)