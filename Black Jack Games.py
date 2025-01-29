from Deck import *
from Player import *

class BlackJack:

    #Init
    croupier = Player()
    player1 = Player()
    deck = Deck()
    partie = True
    starting = True

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

    while True: #(step event)

        mise = int(input(f"combien voulez vous miser? Votre solde actuel est de {player1.points}$."))

        #Game
        print('\nDébut de la partie\n')
        coucher = False

        while partie==True :

            if starting == True:

                croupier.tirer(deck)
                player1.tirer(deck)
                player1.tirer(deck)
                print(f'|/| Player1 : {player1.getHand()[0]} // {player1.getHand()[1]} |-| Croupier : {croupier.getHand()[0]} // Carte cachée')
                print(f'|/| Player1 : {player1.score} pts |-| Croupier : {croupier.score} pts |/|\n')
                if player1.score > 21: partie = False

            if starting != True: print(f'|/| Player1 : {player1.score} pts |-| Croupier : {croupier.score} pts |/|\n')
            tirer = ''
            while tirer != 'tirer' and tirer != 'coucher' and coucher == False:
                tirer = str(input('\nEcrivez /tirer/ ou /coucher/ pour tirer une carte ou vous coucher : '))

            if tirer == 'tirer':
                player1.tirer(deck)
                print(f'\nVous avez tiré {player1.getHand()[player1.lendeck-1]}, vous avez désormais {player1.score} points\n')
            else:
                print('Vous vous êtes couché\n')
                coucher = True

            if player1.score > 21:
                partie = False

            # Cas où le joueur est couché [fin de partie]
            if coucher == True and starting == False:
                partie = False
            elif coucher == True:
                croupier.tirer(deck)
                print(f'La croupier a tiré {croupier.getHand()[croupier.lendeck-1]}, il a désormais {croupier.score} points\n')
                starting = False
                partie = False
            else:
                if croupier.score < 17:
                    croupier.tirer(deck)
                    print(f'La croupier a tiré {croupier.getHand()[croupier.lendeck-1]}, il a désormais {croupier.score} points\n')
                    starting = False

                if croupier.score > 21:
                    partie = False





        if partie == False:
            print(f'|/| Player1 : {player1.score} pts |-| Croupier : {croupier.score} pts |/|')
            #Qui a gagné
            if croupier.score > 21 and player1.score < 21:
                player1.points += mise
                print(f'Vous avez gagné ! Solde : {player1.points}')
            elif croupier.score <= 21 and player1.score < croupier.score:
                player1.points -= mise
                print(f'Vous avez perdu ! Solde : {player1.points}')
            elif player1.score > 21 and croupier.score < 21:
                player1.points -= mise
                print(f'Vous avez perdu ! Solde : {player1.points}')
            elif player1.score <= 21 and croupier.score < player1.score:
                player1.points += mise
                print(f'Vous avez gagné ! Solde : {player1.points}')
            elif player1.score == 21 and croupier.score > 21:
                player1.points += mise
                print(f'Vous avez gagné ! Solde : {player1.points}')
            elif croupier.score == player1.score:
                print(f'Egalité ! Solde : {player1.points}')

            print('Partie Finie')
            croupier.resetHand()
            player1.resetHand()
            starting = True


            coucher = False

            restart = str(input('Voulez-vous continuer ? oui/non '))
            if restart == 'oui' and player1.points > 0:
                partie = True
            else:
                print(f'Fin de partie, vous finissez avec {player1.points} $')
                break




BlackJack()