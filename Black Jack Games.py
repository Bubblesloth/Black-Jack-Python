from Deck import *
from Player import *

class BlackJack:

    croupier = Player()
    player1 = Player()
    deck = Deck()

    print('------')
    print(player1.getHand())
    player1.tirer(deck)
    print(player1.getHand())
    print('------')
    player1.tirer(deck)
    print(player1.getHand())
    print('------')
    print(player1.getHand()[0])
    print('------')
    print(player1.getHand()[1])

    print('Début de la partie\n')

    while croupier.score < 17:
        croupier.tirer(deck)
        print(f'La croupier a tiré {croupier.getHand()[croupier.lendeck-1]}, il a désormais {croupier.score} points\n')



BlackJack()