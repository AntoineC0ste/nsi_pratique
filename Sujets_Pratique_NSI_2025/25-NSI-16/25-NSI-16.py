# Exercice 1
def moyenne(notes:list[tuple[float, int]]) -> float:
    '''Renvoie la moyenne pondérée des notes spécifiées dans le tableau composé de tuples (note, coef)'''
    moy = 0
    coefs = 0
    for note in notes:
        moy += note[0] * note[1] # On ajoute note*coef
        coefs += note[1] # On crée la somme pour le dénominateur
    return moy/coefs

assert moyenne([(15.0,2),(9.0,1),(12.0,3)]) == 12.5

# Exercice 2
def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1] # Chaque ligne commence par 1 
    for i in range(0, len(ligne)-1): 
        ligne_suiv.append(ligne[i]+ligne[i+1]) # On fait la somme des termes entre les 2
    ligne_suiv.append(1) # Et se finit par 1
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n): 
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle


assert  ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]