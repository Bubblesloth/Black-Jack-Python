import random
import pile
import Card

class Deck:

    def __init__(self):
        self.symbols = ['Trefle', 'Pique', 'Coeur', 'Carreau']
        self.ranks = ['2','3','4','5','6','7','8','9','10','Valet', 'Dame', 'Roi','As']
        self.cards = pile.Pile()
        liste_cartes = []
        for symbol in self.symbols:
            for rank in self.ranks:
                liste_cartes.append(Card.Card(rank,symbol))
        random.shuffle(liste_cartes)
        for carte in liste_cartes:
            self.cards.empiler(carte)

    def getCards(self):
        return self.cards