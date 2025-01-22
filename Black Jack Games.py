from Deck import *
from Player import *

class BlackJack:

    #Init
    croupier = Player()
    player1 = Player()
    deck = Deck()
    partie = True
    mise = input(f"combien voulez vous miser? Votre solde actuel est de {player1.points}$.")
    #Tests
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

    #Game
    while partie==True :
        print('Début de la partie\n')

        while croupier.score < 17:
            croupier.tirer(deck)
            print(f'La croupier a tiré {croupier.getHand()[croupier.lendeck-1]}, il a désormais {croupier.score} points\n')

        if croupier.score > 21:
            partie = False

    print('Partie Finie')





BlackJack()