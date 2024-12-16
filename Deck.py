import random
import classe_pile
import Card

class Deck:

    def _init_(self):
        self.symbols = ['Trefle', 'Pique', 'Coeur', 'Carreau']
        self.ranks = ['2','3','4','5','6','7','8','9','10','Valet', 'Dame', 'Roi','As']
        self.cards = Pile()
        for symbol in symbols:
            for rank in ranks:
                self.cards.empiler(Card(rank,symbol))
        random.suffle(cards)