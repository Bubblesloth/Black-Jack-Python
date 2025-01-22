from Deck import *
from Player import *

class BlackJack:

    #Init
    croupier = Player()
    player1 = Player()
    deck = Deck()
    partie = True
    mise = int(input(f"combien voulez vous miser? Votre solde actuel est de {player1.points}$."))
    #Tests
    '''
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
    print(player1.getHand()[1])'''

    #Game
    print('\nDébut de la partie\n')
    coucher = False

    while partie==True :

        if croupier.score < 17:
            croupier.tirer(deck)
            print(f'La croupier a tiré {croupier.getHand()[croupier.lendeck-1]}, il a désormais {croupier.score} points\n')

        if croupier.score > 21:
            partie = False
        else:

            tirer = ''
            print(player1.score)
            while tirer != 'tirer' and tirer != 'coucher' and coucher == False:
                tirer = str(input('Ecrivez /tirer/ ou /coucher/ pour tirer une carte ou vous coucher : '))
            if tirer == 'tirer':
                player1.tirer(deck)
                print(f'\nVous avez tiré {player1.getHand()[player1.lendeck-1]}, vous avez désormais {player1.score} points\n')
            else:
                print('Vous vous êtes couché')
                coucher = True

            if player1.score > 21:
                partie = False

        # Cas où le joueur est couché [fin de partie]
            if coucher == True and croupier.score >= 17:
                partie = False





    if partie == False:
        #Qui a gagné
        if croupier.score > 21 and player1.score < 21:
            player1.points += mise
            print(f'Vous avez gagné ! Solde : {player1.points}')
        elif croupier.score <= 21 and player1.score < croupier.score:
            player1.points -= mise
            print(f'Vous avez perdu ! Solde : {player1.points}')
        elif player1.score <= 21 and croupier.score < player1.score:
            player1.points += mise
            print(f'Vous avez gagné ! Solde : {player1.points}')
        elif croupier.score == player1.score:
            print(f'Egalité ! Solde : {player1.points}')

        print('Partie Finie')
        croupier.resetHand
        player1.resetHand


        coucher = False


        restart = str(input('Voulez-vous recommencer ? oui/non '))
        if restart == 'oui':
            partie = True
        #else: qqchose





BlackJack()