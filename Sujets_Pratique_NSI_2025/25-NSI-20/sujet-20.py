# Exercice 1

def min_et_max(tab:list) -> dict:
    min = tab[0]
    max = tab[0]
    for valeur in tab:
        if valeur < min:
            min = valeur
            
        if valeur > max:
            max = valeur

    return {'min':min, 'max':max}

# Exercice 2
class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        self.contenu = []
        for c in range(1, 5): # Pour chaque couleur,
            for v in range(1, 14): # Et chaque valeur,
                self.contenu.append(Carte(c, v)) # On ajoute la carte.

    def recuperer_carte(self, pos) -> Carte:
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        assert 0 <= pos <= 51, f"Le paramètre pos est invalide: {pos}"
        return self.contenu[pos]
    
jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)
print(carte1.recuperer_valeur())
carte2 = jeu.recuperer_carte(0)
print(carte2.recuperer_couleur())
# carte3 = jeu.recuperer_carte(52)
