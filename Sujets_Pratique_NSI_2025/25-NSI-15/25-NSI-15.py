# Exercice 1
def multiplication(n1:int, n2:int) -> int:
    '''Renvoie le produit de ces deux nombres'''
    if n1 == 0 or n2 == 0: # Un produit comportant 0 vaut zéro
        return 0

    rslt = abs(n1)
    for i in range(abs(n2)-1): # On ajoute n1 à lui même n2 fois
        rslt += abs(n1)
    
    if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0): # Si un seul terme est négatif,
        return -rslt
    else:
        return rslt
    

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0

# Exercice 2
def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 # Milieu de la liste
 
    if tab[m] < x: # Si le milieu est plus petit que le nombre cherché,
        return chercher(tab, x, m+1, j) # On regarde à droite
    elif tab[m] > x: # Sinon, 
        return chercher(tab, x, i , m-1) # On regarde à gauche
    else: # Si c'est égal,
        return m 

assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2
assert chercher([1], 0, 0, 0) == None
assert chercher([1], 1, 0, 0) == 0

