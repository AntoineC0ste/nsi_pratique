# Exercice 1
def occurences(caractere:str, chaine:str) -> int:
    occ = 0
    for i in range(len(chaine)):
        if chaine[i] == caractere:
            occ += 1

    return occ

assert occurences("e", "sciences") == 2
assert occurences("i", "mississipi") == 4
assert occurences("a", "mississipi") == 0


# Exercice 2
valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre: 
        return [valeurs[rang]] + rendu_glouton(a_rendre - v, rang) 
    else:
        return rendu_glouton(a_rendre, rang + 1) 


assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291, 1) == [50, 50, 50, 50, 50, 20, 20, 1]