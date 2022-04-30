# BlackJack Class
# Date:            2021/10/24
# Author:          TheScriptGuy
# Description:     Black Jack Class

import random


class BlackJack:
    """The BlackJack class controls all the dynamics of the game."""

    def printDeck(self, __deck__):
        """Display the contents of the deck"""
        print(__deck__)

    def initializeDeck(self, __numDecks__):
        """Initialize the deck"""
        counter = 0

        __deckOfCards__ = []

        while counter < __numDecks__:
            __deckOfCards__ += self.deckOfCards
            counter += 1

        # Randomize the deck
        random.shuffle(__deckOfCards__)

        return __deckOfCards__

    def printPlayerOrder(self, __playerOrder__):
        """Print the player order."""
        print(__playerOrder__)

    def definePlayerOrder(self, __numberOfPlayers__):
        """Define the player order"""
        playerOrder = []

        playerCounter = 0

        while playerCounter < __numberOfPlayers__:

            playerCounter += 1
            playerOrder.append("P" + str(playerCounter))

        playerOrder.append("D")

        return playerOrder

    def countValue(self, playerCards):
        """
        Count the value of the cards.
        Can this be improved?
        """
        __value__ = 0
        for card in playerCards:
            if card.startswith("A"):
                if __value__ + 11 <= 21:
                    __value__ += self.cardValues[card]
                else:
                    __value__ += 1
            else:
                __value__ += self.cardValues[card]
        return __value__

    def firstDeal(self, __deck__):
        """Perform the first deal of all the cards."""
        # Burn the first card
        __deck__.pop(0)
        counter = 1

        # Now deal the deck for the players.
        while counter <= (len(self.newPlayerOrder) * 2):
            currentPlayer = self.newPlayerOrder[0]
            self.playerDefinition[currentPlayer]["Cards"].append(__deck__.pop(0))
            self.playerDefinition[currentPlayer]["valueOfCards"] = self.countValue(self.playerDefinition[currentPlayer]["Cards"])

            self.newPlayerOrder.append(self.newPlayerOrder.pop(0))

            counter += 1

    def definePlayers(self):
        """Define all the players that will participate in the game."""
        __playerDefinition__ = {}

        for item in self.newPlayerOrder:
            __playerDefinition__[item] = {}
            __playerDefinition__[item]["Cards"] = []
            __playerDefinition__[item]["valueOfCards"] = 0

        return __playerDefinition__

    def printPlayerCards(self):
        """Print the player cards."""
        print(self.playerDefinition)

    def removeCurrentPlayer(self):
        """Remove the current player from the game."""
        self.newPlayerOrder.pop(0)

    def statsPlayerWins(self):
        """Update the statistics to reflect that player won the game"""
        self.stats["playerWins"] += 1

    def statsDealerWins(self):
        """Update the statistics to reflect that dealer won the game"""
        self.stats["dealerWins"] += 1

    def statsGamePlayed(self):
        """Update the number of games."""
        self.stats["gamesPlayed"] += 1

    def printStats(self):
        """Show the statistics."""
        print(self.stats)

    def playerPlays(self, __player__):
        """Player plays the cards based on logic of Black Jack."""
        __valueOfCards__ = self.playerDefinition[__player__]["valueOfCards"]
        while __valueOfCards__ <= 21 and __valueOfCards__ < 17:
            self.playerDefinition[__player__]["Cards"].append(self.newDeck.pop(0))
            self.playerDefinition[__player__]["valueOfCards"] = self.countValue(self.playerDefinition[__player__]["Cards"])
            __valueOfCards__ = self.playerDefinition[__player__]["valueOfCards"]

    def calculateTheWinner(self):
        """Calculate the winner of the game."""
        __dealerValueOfCards__ = self.playerDefinition["D"]["valueOfCards"]

        for player in self.playerDefinition:
            if player.startswith("P"):
                __valueOfCards__ = self.playerDefinition[player]["valueOfCards"]
                if __valueOfCards__ > 21:
                    # print(player + " BUST")
                    self.statsDealerWins()

                elif __valueOfCards__ > __dealerValueOfCards__ or __dealerValueOfCards__ > 21:
                    # print(player + " WINS")
                    self.statsPlayerWins()

                elif __valueOfCards__ < __dealerValueOfCards__:
                    # print(player + " LOSES")
                    self.statsDealerWins()

        self.statsGamePlayed()

    def setNumberOfPlayers(self, numberPlayers):
        """Set the number of players."""
        self.numberOfPlayers = numberPlayers

    def printNumberOfPlayers(self):
        """Print the number of players in the game."""
        print("Print number of players: ", self.numberOfPlayers)

    def printNumberOfDecks(self):
        """Print the number of the decks."""
        print("Print number of Decks: ", self.numberOfDecks)

    def setNumberOfDecks(self, numberDecks):
        """Define the number of decks to be included in the game."""
        self.numberOfDecks = numberDecks

    def setCardValues(self):
        """Define the card values."""
        self.cardValues = {
            "2H": 2, "3H": 3, "4H": 4, "5H": 5, "6H": 6, "7H": 7, "8H": 8, "9H": 9, "JH": 10, "QH": 10, "KH": 10, "AH": 1,
            "2C": 2, "3C": 3, "4C": 4, "5C": 5, "6C": 6, "7C": 7, "8C": 8, "9C": 9, "JC": 10, "QC": 10, "KC": 10, "AC": 1,
            "2S": 2, "3S": 3, "4S": 4, "5S": 5, "6S": 6, "7S": 7, "8S": 8, "9S": 9, "JS": 10, "QS": 10, "KS": 10, "AS": 1,
            "2D": 2, "3D": 3, "4D": 4, "5D": 5, "6D": 6, "7D": 7, "8D": 8, "9D": 9, "JD": 10, "QD": 10, "KD": 10, "AD": 1
        }

    def setDeckOfCards(self):
        """Set the deck of cards that will be played."""
        self.deckOfCards = [
            "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "JH", "QH", "KH", "AH",
            "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "JD", "QD", "KD", "AD",
            "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "JS", "QS", "KS", "AS",
            "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "JC", "QC", "KC", "AC"
        ]

    def setInitialStats(self):
        """Set the inital stats for the game."""
        self.stats = {
            "dealerWins": 0,
            "playerWins": 0,
            "gamesPlayed": 0
        }

    def __init__(self, __numberOfPlayers__, __numberOfDecks__):
        """Initialize the class."""
        self.setCardValues()
        self.setDeckOfCards()

        self.setNumberOfPlayers(__numberOfPlayers__)
        self.setNumberOfDecks(__numberOfDecks__)

        self.setInitialStats()

        self.playerDefinition = {}

        self.newDeck = self.initializeDeck(self.numberOfDecks)
        self.newPlayerOrder = self.definePlayerOrder(self.numberOfPlayers)
        self.playerDefinition = self.definePlayers()
