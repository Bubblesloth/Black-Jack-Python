import random
import pile
import Card

class Deck:

    def __init__(self):
        self.symbols = ['Trefle', 'Pique', 'Coeur', 'Carreau']
        self.ranks = ['2','3','4','5','6','7','8','9','10','Valet', 'Dame', 'Roi','As']
        self.cards = pile.Pile()
        for symbol in self.symbols:
            for rank in self.ranks:
                self.cards.empiler(Card.Card(rank,symbol))

    def getCards(self):
        return self.cards

deck = Deck()
print(deck.getCards())
pile.afficher(deck.cards)