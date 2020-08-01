import random
import time

"""" BLACKJACK by d6ta"""
""""Face cards worth 10, aces worth 1 or 11 (gahh crap, how am I gonna code that!?!?)"""
""" Trying to figure out how to code aces... """

class Dealer:
    card1 = 0
    card2 = 0
    card3 = 0
    card4 = 0
    totalHand = (card1+card2+card3+card4)

class Player:
    card1 = 0
    card2 = 0
    card3 = 0
    card4 = 0
    totalHand = (card1 + card2 + card3 + card4)

def printDelay(delay):
    time.sleep(delay)

def newHand():  # Generates a new random 1-11 value for dealer and player hand
    Dealer.card1 = random.randint(1, 11)
    Dealer.card2 = random.randint(1, 11)
    Dealer.card3 = 0
    Dealer.card4 = 0
    Dealer.totalHand = (Dealer.card1 + Dealer.card2 + Dealer.card3 + Dealer.card4)

    Player.card1 = random.randint(1, 11)
    Player.card2 = random.randint(1, 11)
    Player.card3 = 0
    Player.card4 = 0
    Player.totalHand = (Player.card1 + Player.card2 + Player.card3 + Player.card4)

def hit(whoIsHitting):
    if whoIsHitting.card3 > 0:  # If the hitters' 3rd card isn't 0, give them a 4th. Else, give them a 3rd.
        whoIsHitting.card4 = random.randint(1, 11)
    else:
        whoIsHitting.card3 = random.randint(1, 11)

    whoIsHitting.totalHand = (whoIsHitting.card1 + whoIsHitting.card2 + whoIsHitting.card3 + whoIsHitting.card4)

def printHands():  # Print both users' hands to the console
    print("Your hand: ", Player.card1, Player.card2, Player.card3, Player.card4, "Total hand: ", Player.totalHand)
    print("Dealer's hand: ", Dealer.card1, " ?", Dealer.card3, Dealer.card4, "Total hand: ?")
    printDelay(1)

def printAllHands():  # Print hands, don't hide dealer's hand
    print("Your hand: ", Player.card1, Player.card2, Player.card3, Player.card4, "Total hand: ", Player.totalHand)
    print("Dealer's hand: ", Dealer.card1, Dealer.card2, Dealer.card3, Dealer.card4, "Total hand: ", Dealer.totalHand)
    printDelay(1)

def turn():
    newHand()

    # Show the players hand first, then the dealer's 1st card
    # Then ask the player what to do (hit, stand)
    # After hit/stand, make the dealer cpu hit/stand based on their hand based on the value of their hand.

    printHands()

    #### Players Turn ####
    action = input("Hit or stand? Say 'hit' or 'stand': ")  # Prompt the user for their action
    if action == "hit":
        print("You will HIT.")
        hit(Player)
        printHands()
        hitAgain = input("Would you like to hit again? (y/n): ")
        if hitAgain == "y":
            hit(Player)
            printHands()

        else:
            print("You will not hit again.")


    elif action == "stand":
        print("You will STAND.")
        printHands()

    printDelay(1)
    #### Dealer's Turn ####
    if Dealer.totalHand < 15:
        hit(Dealer)
        print("Dealer HITS.")
        printAllHands()
        if Dealer.totalHand < 15:
            hit(Dealer)
            print("Dealer HITS again.")
            printAllHands()
    elif Dealer.totalHand == 15 or Dealer.totalHand > 15:
        print("Dealer STANDS.")
        printAllHands()

    #### Check who's card is closer ####
    if Dealer.totalHand == 21:  # Dealer blackjack
        printDelay(3)
        print("DEALER has blackjack, DEALER wins.")
    elif Player.totalHand == 21:  # Player blackjack
        printDelay(3)
        print("PLAYER has blackjack, PLAYER wins.")
    elif Player.totalHand > 21:  # Player bust
        printDelay(3)
        print("PLAYER busts, DEALER wins.")
    elif Dealer.totalHand > 21:  # Dealer bust
        printDelay(3)
        print("DEALER busts, PLAYER wins.")
    elif Player.totalHand < Dealer.totalHand:  # PLAYER hand LESS than DEALER hand
        printDelay(3)
        print("DEALER has higher hand than PLAYER, DEALER wins.")
    elif Dealer.totalHand < Player.totalHand:  # DEALER hand LESS than PLAYER hand.
        printDelay(3)
        print("PLAYER has higher hand than DEALER, PLAYER wins.")
    elif Dealer.totalHand == Player.totalHand:
        printDelay(3)
        print("DEALER and PLAYER have same hand, DEALER wins.")


while True:
    time.sleep(.1)
    playAgain = input("Would you like to play a new hand? (y/n): ")
    if playAgain == "y":
        turn()
    else:
        print("Okay then. See you soon!")
        exit()
