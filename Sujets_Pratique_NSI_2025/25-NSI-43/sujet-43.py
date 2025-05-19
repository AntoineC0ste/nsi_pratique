# Exercice 1
def couples_consecutifs(tab:list[int]):
    couples = []
    for i in range(len(tab)-1):
        if tab[i] + 1 == tab[i+1]:
            couples.append((tab[i], tab[i+1]))

    return couples

assert  couples_consecutifs([1, 4, 3, 5]) == []
assert  couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

# Exercice 2
def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage en bas 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0: # propage à gauche 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]): # propage à droite 
        colore_comp1(M, i, j+1, val) 

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]