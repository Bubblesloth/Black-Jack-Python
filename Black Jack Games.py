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

            print(f'|/| Player1 : {player1.score} pts |-| Croupier : {croupier.score} pts |/|')
            tirer = ''
            while tirer != 'tirer' and tirer != 'coucher' and coucher == False:
                tirer = str(input('\nEcrivez /tirer/ ou /coucher/ pour tirer une carte ou vous coucher : '))
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
        print(f'|/| Player1 : {player1.score} pts |-| Croupier : {croupier.score} pts |/|')
        #Qui a gagné
        if croupier.score > 21 and player1.score < 21:
            print('Vous avez gagné !')
        elif croupier.score <= 21 and player1.score < croupier.score:
            print('Vous avez perdu !')
        elif player1.score <= 21 and croupier.score < player.score:
            print('Vous avez gagné !')
        elif croupier.score == player1.score:
            print('Egalité !')

        print('Partie Finie')
        croupier.resetHand
        player1.resetHand


        coucher = False


        restart = str(input('Voulez-vous continuer ? oui/non '))
        if restart == 'oui':
            partie = True
        #else: qqchose





BlackJack()