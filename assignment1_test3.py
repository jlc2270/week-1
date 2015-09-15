import random

# First we will establish some general variables for our game, including the 'stake' of the game 
# (how much money each play is worth), as well as a list representing the cards used in the game.
# To make things easier, we will just use a list 0-9 for the cards.

gameStake = 50  
cards = range(10)

# Next, let's define a new class to represent each player in the game.

class Player:
    
    # create here two local variables to store a unique ID for each player and the player's current 'pot' of money
    # [FILL IN YOUR VARIABLES HERE]

    playerID=[]
    startingPot=500
    
    # in the __init__() function, use the two input variables to initialize the ID and starting pot of each player
    
    def __init__(self, playerID, startingPot):
        # [CREATE YOUR INITIALIZATIONS HERE]
        i=0
        self.playerID= 'playerID' + str(i)
        self.playerID+=i
        self.playerPot=startingPot
    # create a function for playing the game. This function should take on input for the card of the dealer.
    # it should then take a random card from 
    
    def play(self, dealerCard):
        # [CREATE CODE FOR SELECTING A RANDOM CARD]
        dealerCard=random.choice(cards)
        playerCard=random.choice(cards)
        # here we should have a conditional that tests the player's card value against the dealer card
        # and returns a statement saying whether the player won or lost the hand
        # before return the statement, make sure to either add or subtract the stake from the player's pot so that
        # the 'pot' variable tracks the player's money
        
        if playerCard < dealerCard:
            # [INCREMENT THE PLAYER'S POT, AND RETURN A MESSAGE]
            self.playerPot=[startingPot]-[gameStake]
            print 'Player loses'
        else:
            # [INCREMENT THE PLAYER'S POT, AND RETURN A MESSAGE]
            self.playerPot=[startingPot]+[gameStake]
            print 'Player wins'
        
    # create an accessor function to return the current value of the player's pot
    def returnPot(self):
        # [FILL IN THE RETURN STATEMENT]
        return self.playerPot
        print playerPot
        
    # create an accessor function to return the player's ID
    def returnID(self):
        # [FILL IN THE RETURN STATEMENT]
        return self.playerID
        print playerID