from games import BlackJack


numberOfPlayers = 5
numberOfDecks = 5
numberOfGames = 1000

"""
DO NOT EDIT BELOW THIS LINE
"""
gameStats = {
    "dealerWins": 0,
    "playerWins": 0,
    "gamesPlayed": 0
}

def updateStats(__gameStats__):
    # update the gameStats variable with the last game results.
    gameStats["dealerWins"] += __gameStats__["dealerWins"]
    gameStats["playerWins"] += __gameStats__["playerWins"]
    gameStats["gamesPlayed"] += __gameStats__["gamesPlayed"]

def playGame(__numberOfPlayers,__numberOfDecks):
    # This subroutine will play a game of Black Jack

    # Start a game.
    bjGame = BlackJack.BlackJack(__numberOfPlayers,__numberOfDecks)

    # Deal the first set of cards to all players.
    bjGame.firstDeal(bjGame.newDeck)


    # Deal out the players.
    while len(bjGame.newPlayerOrder) >= 2:
        bjGame.playerPlays(bjGame.newPlayerOrder[0])
        bjGame.removeCurrentPlayer()


    # Deal out the dealer.
    bjGame.playerPlays(bjGame.newPlayerOrder[0])
    bjGame.removeCurrentPlayer()

    # Calculate the winner from the game played.
    bjGame.calculateTheWinner()

    # Update the gameStats with the latest results.
    updateStats(bjGame.stats)


def startGames(__numberOfGames):
    # This will iterate through all number of games to be played.

    __counter = 0
    while __counter < __numberOfGames:
        playGame(numberOfPlayers,numberOfDecks)
        __counter += 1


if __name__ == "__main__":

    startGames(numberOfGames)

    if gameStats["dealerWins"] != 0:
        __playerWinRate = gameStats["playerWins"] / gameStats["dealerWins"] * 100
        print("Number of Players: {}, Number of Decks: {}, Number of Games: {}, Player win rate: {:.2f}".format(numberOfPlayers,numberOfDecks,numberOfGames,__playerWinRate))
    else:
        print("Could not deal")




