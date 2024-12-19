from Deck import *
from Player import *

class BlackJack:

    croupier = Player()
    player1 = Player()
    deck = Deck()

    print(player1.getHand())

    player1.tirer(deck)

    print(player1.getHand())

    player1.tirer(deck)

    print(player1.getHand())

    print(player1.getHand()[0])
    print(player1.getHand()[1])



BlackJack()