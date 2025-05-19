# Exercice 1
def tri_selection(tab:list[int]) -> list[int]:
    g = 0
    for _ in range(len(tab)):
        # On cherche l'indice du minimum
        mini = g
        for i in range(g, len(tab)):
            if tab[i] < tab[mini]:
                mini = i
        # On échange les valeurs
        temp = tab[g]
        tab[g] = tab[mini]
        tab[mini] = temp
        g += 1
    
tab = [1, 52, 6, -9, 12]
tri_selection(tab)
assert tab == [-9, 1, 6, 12, 52]

# Exercice 2
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 11: 
        compteur = compteur + 1
        if nb_mystere > nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere) 
        print("Nombre d'essais: ", compteur) 
    else:
        print ("Perdu ! Le nombre était ", nb_mystere) 

