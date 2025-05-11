# Exercice 1
def recherche(tab:list[int], n:int) -> int:
    '''Effectue une recherche dichotomique de l'entier n dans le tableau tab'''
    if n not in tab:
        return None
    l = len(tab)//2
    # Cas de base
    if tab[l] == n:
        return l
    # Cas récursif, on cherche dans la moitié de la liste correspondante
    if tab[l] > n:
        return recherche(tab[:l], n)
    else:
        return l + recherche(tab[l:],n)

assert recherche([2, 3, 4, 5, 6], 5) == 3
assert  recherche([2, 3, 4, 6, 7], 5) == None

# Exercice 2
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for c in message: 
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26 
            resultat = resultat + alphabet[indice]
        else:
            resultat = resultat + c 
    return resultat

assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) == 'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5) == 'BONJOUR A TOUS. VIVE LA MATIERE NSI !'

