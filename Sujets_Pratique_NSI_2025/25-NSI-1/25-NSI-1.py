def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + s[i-1]
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + s[-1] 
    resultat += lecture_chiffre
    return resultat

def voisins_entrants(adj:list[int], x:int) -> list[int]:
    '''Renvoie les voisins entrants du sommet x spécifié.
    `adj` est une liste d'adjacence composée d'entiers
    `x` est le sommet dont on cherche les voisins entrants.
    '''
    liste_voisins = []
    for i in range(len(adj)):
        if x in adj[i]:
            liste_voisins.append(i)

    return liste_voisins

# print(voisins_entrants([[1, 2], [2], [0], [0]], 0))
print(nombre_suivant('311'))