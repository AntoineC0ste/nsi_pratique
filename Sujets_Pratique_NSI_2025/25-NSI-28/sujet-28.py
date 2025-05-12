# Exercice 1
def a_doublon(tab:list) -> bool:
    '''Renvoie un booléen indiquant s'il y a un nombre en double'''
    for i in range(len(tab)-1):
        if tab[i] == tab[i+1]:
            return True
    
    return False

assert not a_doublon([1])
assert a_doublon([1,2,3,4,6,6])

# Exercice 2
def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) dans un grille de taille n x n,
    en tenant compte des cases sur les bords. """
    voisins = []
    for dl in range(-1, 2):
        for dc in range(-1, 2):
            l = ligne + dl
            c = colonne + dc
            if (l, c) != (ligne, colonne) \
                    and 0 <= l < n and 0 <= c < n:
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = voisinage(len(grille), ligne, colonne) 
    for l, c in voisins:
        if grille[l][c] != -1: # si ce n'est pas une bombe 
            grille[l][c] += 1  # on ajoute 1 à sa valeur 

def genere_grille(bombes):
    """ Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1 # place la bombe 
        incremente_voisins(grille, ligne, colonne)  # incrémente ses voisins 
    return grille

grille =[[1, 1, 1, 0, 0],
        [1, -1, 1, 1, 1],
        [2, 2, 3, 2, -1],
        [1, -1, 2, -1, 3],
        [1, 1, 2, 2, -1]]

assert genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]) == grille