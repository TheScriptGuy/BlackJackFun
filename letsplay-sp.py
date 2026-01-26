from games import BlackJack


numberOfPlayers = 5
numberOfDecks = 5
numberOfGames = 1000

"""DO NOT EDIT BELOW THIS LINE"""
gameStats = {
    "handDealerWins": 0,
    "handPlayerWins": 0,
    "handPushes": 0,
    "gameDealerWins": 0,
    "gamePlayerWins": 0,
    "gamePushes": 0,
    "gamesPlayed": 0
}

def updateStats(__gameStats__):
    """Update the gameStats variable with the last game results."""
    gameStats["handDealerWins"] += __gameStats__["handDealerWins"]
    gameStats["handPlayerWins"] += __gameStats__["handPlayerWins"]
    gameStats["handPushes"] += __gameStats__["handPushes"]
    gameStats["gameDealerWins"] += __gameStats__["gameDealerWins"]
    gameStats["gamePlayerWins"] += __gameStats__["gamePlayerWins"]
    gameStats["gamePushes"] += __gameStats__["gamePushes"]
    gameStats["gamesPlayed"] += __gameStats__["gamesPlayed"]

def playGame(__numberOfPlayers, __numberOfDecks):
    """This subroutine will play a game of Black Jack."""
    # Start a game.
    bjGame = BlackJack.BlackJack(__numberOfPlayers, __numberOfDecks)

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
    """This will iterate through all number of games to be played."""
    __counter = 0
    while __counter < __numberOfGames:
        playGame(numberOfPlayers, numberOfDecks)
        __counter += 1

if __name__ == "__main__":
    # Let the games begin
    startGames(numberOfGames)

    __handDecided = gameStats["handPlayerWins"] + gameStats["handDealerWins"]
    __handTotal = __handDecided + gameStats["handPushes"]
    __gameDecided = gameStats["gamePlayerWins"] + gameStats["gameDealerWins"]
    __gameTotal = __gameDecided + gameStats["gamePushes"]

    if __handTotal == 0 or __gameTotal == 0:
        print("Could not deal")
    else:
        __handWinRateInclusive = gameStats["handPlayerWins"] / __handTotal * 100
        __handLossRateInclusive = gameStats["handDealerWins"] / __handTotal * 100
        __handPushRate = gameStats["handPushes"] / __handTotal * 100
        __handWinRateDecided = gameStats["handPlayerWins"] / __handDecided * 100 if __handDecided else 0.0

        __gameWinRateInclusive = gameStats["gamePlayerWins"] / __gameTotal * 100
        __gameLossRateInclusive = gameStats["gameDealerWins"] / __gameTotal * 100
        __gamePushRate = gameStats["gamePushes"] / __gameTotal * 100
        __gameWinRateDecided = gameStats["gamePlayerWins"] / __gameDecided * 100 if __gameDecided else 0.0

        print("Number of Players: {}, Number of Decks: {}, Number of Games: {}".format(numberOfPlayers, numberOfDecks, numberOfGames))
        print("PH inc win {:.2f}% loss {:.2f}% push {:.2f}% | PH decided win {:.2f}%".format(
            __handWinRateInclusive, __handLossRateInclusive, __handPushRate, __handWinRateDecided))
        print("PG inc win {:.2f}% loss {:.2f}% push {:.2f}% | PG decided win {:.2f}%".format(
            __gameWinRateInclusive, __gameLossRateInclusive, __gamePushRate, __gameWinRateDecided))
