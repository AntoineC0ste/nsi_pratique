# Exercice 1
def moyenne(tab:list[float]) -> float:
    numerateur = 0
    denominateur = len(tab)
    for nombre in tab:
        numerateur += nombre
    
    return numerateur/denominateur

assert moyenne([1.0]) == 1.0
print(moyenne([1.0, 2.0, 4.0]))


# Exercice 2
def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0 : 
        bin_a = str(a % 2) + bin_a 
        a = a // 2
    return bin_a


assert binaire(83) == '1010011'
assert binaire(6) == '110'
assert binaire(127) == '1111111'
assert binaire(0) == '0'