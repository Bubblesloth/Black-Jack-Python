from Deck import *
class Player:

    def __init__(self):
        self.hand = []
        self.score = 0
        self.points = 50
        self.lendeck = 0

    def tirer(self,deck):
        carte = deck.defausser()
        print(carte)
        print(carte.value)
        self.hand.append(carte)
        self.lendeck += 1
        if carte.value != 'As':
            self.score += carte.value
        elif self.score + 11 <= 21:
            self.score += 11
        else: self.score += 1

    def getHand(self):
        return self.hand

    def resetHand(self):
        self.hand = []
        self.score = 0
        self.lendeck = 0




