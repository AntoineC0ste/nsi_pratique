# Exercice 1
def fusion(tab1:list[int], tab2:list[int]) -> list[int]:
    tab3 = []
    i = 0
    j = 0
    
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            tab3.append(tab1[i])
            i += 1
        else:
            tab3.append(tab2[j])
            j += 1
    
    if i < len(tab1):
        while i < len(tab1):
            tab3.append(tab1[i])
            i += 1
    else:
        while j < len(tab2):
            tab3.append(tab2[j])
            j += 1
    
    return tab3

assert  fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert  fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert  fusion([4], [2, 6]) == [2, 4, 6]
assert  fusion([], []) == []
assert  fusion([1, 2, 3], []) == [1, 2, 3]


def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]: 
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]


assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIV") == 2024