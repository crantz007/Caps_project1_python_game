# ******* BLACKJACK ******

import random


def main():
    players = getInput()

    # keep track of which player is being dealt card

    playerNumber = 1
    while players != 0:
        # Assign variables by calling functions
        card1, face1, card2, face2 = compute(players)
        output(playerNumber, card1, face1, card2, face2)

        # Maintain loop variables , update player number

        players -= 1
        playerNumber += 1
    return


def getInput():
    while True:
        # exception handling
        try:
            # request player count
            players = int(input('How many people are playing ?'))
            break
        except ValueError:
            # exception message
            print("Oops!  numbers are required.  Try again...")
    return players


def compute(playerCount):
    # deal card randomly
    card1 = random.randint(1, 13)
    face1 = random.randint(0, 3)
    card2 = random.randint(1, 13)
    face2 = random.randint(0, 3)
    # return variables to main()
    return card1, face1, card2, face2


def output(playerNumber, card1, face1, card2, face2):
    # Array of faces
    faces = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    # Correct and card 1 in special case
    if card1 == 1:
        card1 = 'Ace'
    elif card1 == 11:
        card1 = 'Jack'
    elif card1 == 12:
        card1 = 'Queen'
    elif card1 == 13:
        card1 = 'King'

    # Correct card 2 in special case
    if card2 == 1:
        card2 = 'Ave'
    elif card2 == 11:
        card2 = 'Jack'
    elif card2 == 12:
        card2 = 'Queen'
    elif card2 == 13:
        card2 = 'King'

    # Output
    print(f'Player{playerNumber} : {card1} of {faces[face1]} {card2} of {faces[face2]}')
    return


main()
