# Exercice 1
def recherche_motif(motif:str, texte:str) -> list[int]:
    occurences = []
    for i in range(len(texte)):
        is_in = True
        if len(motif) > len(texte) - i:
            return occurences
        for j in range(len(motif)):
            if motif[j] != texte[i+j]:
                is_in = False
        if is_in:
            occurences.append(i)
    return occurences

print(recherche_motif("ab", ""))

# Exercice 2
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc
 

