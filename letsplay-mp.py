from games import BlackJack

from multiprocessing import Process, Pool, Value, Manager, TimeoutError
import os
import random

upperRangeOfGames = 1000000
upperRangeOfDecks = 8
upperRangeOfPlayers = 6

numberOfProcesses = 20

"""DO NOT EDIT BELOW THIS LINE"""
manager = Manager()
mGameStats = manager.list()


class BJ():
    """Define the BlackJack class."""

    # Game stats for this particular process.
    gameStats = {
        "myPID": os.getpid(),
        "handDealerWins": 0,
        "handPlayerWins": 0,
        "handPushes": 0,
        "gameDealerWins": 0,
        "gamePlayerWins": 0,
        "gamePushes": 0,
        "gamesPlayed": 0
    }

    def updateStats(self, __gameStats__):
        """Update the local gameStats variable with the results of the latest game played."""
        self.gameStats["handDealerWins"] += __gameStats__["handDealerWins"]
        self.gameStats["handPlayerWins"] += __gameStats__["handPlayerWins"]
        self.gameStats["handPushes"] += __gameStats__["handPushes"]
        self.gameStats["gameDealerWins"] += __gameStats__["gameDealerWins"]
        self.gameStats["gamePlayerWins"] += __gameStats__["gamePlayerWins"]
        self.gameStats["gamePushes"] += __gameStats__["gamePushes"]
        self.gameStats["gamesPlayed"] += __gameStats__["gamesPlayed"]

    def playGame(self, __numberOfPlayers, __numberOfDecks):
        """Play a game of Black Jack."""
        bjGame = BlackJack.BlackJack(__numberOfPlayers, __numberOfDecks)

        # Deal out all the cards to all the players.
        bjGame.firstDeal(bjGame.newDeck)

        # Deal out the players
        while len(bjGame.newPlayerOrder) >= 2:
            bjGame.playerPlays(bjGame.newPlayerOrder[0])
            bjGame.removeCurrentPlayer()

        # Deal out the dealer
        bjGame.playerPlays(bjGame.newPlayerOrder[0])
        bjGame.removeCurrentPlayer()

        # Calculate the winner of the game.
        bjGame.calculateTheWinner()

        # Update the local gameStats variable.
        self.updateStats(bjGame.stats)

    def startGames(self, __numberOfGames):
        """Iterate through all the games that need to be played."""
        __counter = 0
        while __counter < __numberOfGames:
            self.playGame(self.numberOfPlayers, self.numberOfDecks)
            __counter += 1

    def run(self):
        """Start the game."""
        self.startGames(self.numberOfGames)
        __handDecided = self.gameStats["handPlayerWins"] + self.gameStats["handDealerWins"]
        __handTotal = __handDecided + self.gameStats["handPushes"]
        __gameDecided = self.gameStats["gamePlayerWins"] + self.gameStats["gameDealerWins"]
        __gameTotal = __gameDecided + self.gameStats["gamePushes"]

        if __handTotal == 0 or __gameTotal == 0:
            print("Could not deal")
            return

        __handWinRateInclusive = self.gameStats["handPlayerWins"] / __handTotal * 100
        __handLossRateInclusive = self.gameStats["handDealerWins"] / __handTotal * 100
        __handPushRate = self.gameStats["handPushes"] / __handTotal * 100
        __handWinRateDecided = self.gameStats["handPlayerWins"] / __handDecided * 100 if __handDecided else 0.0

        __gameWinRateInclusive = self.gameStats["gamePlayerWins"] / __gameTotal * 100
        __gameLossRateInclusive = self.gameStats["gameDealerWins"] / __gameTotal * 100
        __gamePushRate = self.gameStats["gamePushes"] / __gameTotal * 100
        __gameWinRateDecided = self.gameStats["gamePlayerWins"] / __gameDecided * 100 if __gameDecided else 0.0

        print(f"Process ID: {self.myPID}")
        print("PH inc win {:.2f}% loss {:.2f}% push {:.2f}% | PH decided win {:.2f}%".format(
            __handWinRateInclusive, __handLossRateInclusive, __handPushRate, __handWinRateDecided))
        print("PG inc win {:.2f}% loss {:.2f}% push {:.2f}% | PG decided win {:.2f}%".format(
            __gameWinRateInclusive, __gameLossRateInclusive, __gamePushRate, __gameWinRateDecided))

    def __init__(self, __numberOfPlayers, __numberOfDecks, __numberOfGames):
        """Initialize the class."""
        self.initialized = True
        self.numberOfPlayers = __numberOfPlayers
        self.numberOfDecks = __numberOfDecks
        self.numberOfGames = __numberOfGames
        self.myPID = os.getpid()
        self.bjInfo = 'Process ID: {}, Number Of Players: {}, Number of Decks: {}, Number of Games: {}'
        print(self.bjInfo.format(self.myPID, self.numberOfPlayers, self.numberOfDecks, self.numberOfGames))
        self.run()
        mGameStats.append(self.gameStats)


if __name__ == "__main__":
    # Create a pool of workers
    with Pool(processes=numberOfProcesses) as pool:

        # Arguments for BJ Class
        # numberOfPlayers = random.randint(2,6)
        # numberOfDecks = random.randint(2,8)
        # numberOfGames = random.randint(1000,10000)

        multiple_results = [pool.apply_async(BJ, (random.randint(2, upperRangeOfPlayers), random.randint(2, upperRangeOfDecks), random.randint(1000, upperRangeOfGames))) for i in range(numberOfProcesses)]
        [res.get(timeout=60) for res in multiple_results]

    # Gather all the details and sum all the stats.
    totalHandPlayerWins = sum([item["handPlayerWins"] for item in mGameStats])
    totalHandDealerWins = sum([item["handDealerWins"] for item in mGameStats])
    totalHandPushes = sum([item["handPushes"] for item in mGameStats])
    totalGamePlayerWins = sum([item["gamePlayerWins"] for item in mGameStats])
    totalGameDealerWins = sum([item["gameDealerWins"] for item in mGameStats])
    totalGamePushes = sum([item["gamePushes"] for item in mGameStats])
    totalGamesPlayed = sum([item["gamesPlayed"] for item in mGameStats])

    # Display the results.
    print('Total Hand Player Wins: {}'.format(totalHandPlayerWins))
    print('Total Hand Dealer Wins: {}'.format(totalHandDealerWins))
    print('Total Hand Pushes: {}'.format(totalHandPushes))
    print('Total Game Player Wins: {}'.format(totalGamePlayerWins))
    print('Total Game Dealer Wins: {}'.format(totalGameDealerWins))
    print('Total Game Pushes: {}'.format(totalGamePushes))
    print('Total Games Played: {}'.format(totalGamesPlayed))

    totalHandDecided = totalHandPlayerWins + totalHandDealerWins
    totalHand = totalHandDecided + totalHandPushes
    totalGameDecided = totalGamePlayerWins + totalGameDealerWins
    totalGame = totalGameDecided + totalGamePushes

    if totalHand == 0 or totalGame == 0:
        print('Could not deal')
    else:
        totalHandWinRateInclusive = totalHandPlayerWins / totalHand * 100
        totalHandLossRateInclusive = totalHandDealerWins / totalHand * 100
        totalHandPushRate = totalHandPushes / totalHand * 100
        totalHandWinRateDecided = totalHandPlayerWins / totalHandDecided * 100 if totalHandDecided else 0.0

        totalGameWinRateInclusive = totalGamePlayerWins / totalGame * 100
        totalGameLossRateInclusive = totalGameDealerWins / totalGame * 100
        totalGamePushRate = totalGamePushes / totalGame * 100
        totalGameWinRateDecided = totalGamePlayerWins / totalGameDecided * 100 if totalGameDecided else 0.0

        print('Overall PH inc win {:.2f}% loss {:.2f}% push {:.2f}% | PH decided win {:.2f}%'.format(
            totalHandWinRateInclusive, totalHandLossRateInclusive, totalHandPushRate, totalHandWinRateDecided))
        print('Overall PG inc win {:.2f}% loss {:.2f}% push {:.2f}% | PG decided win {:.2f}%'.format(
            totalGameWinRateInclusive, totalGameLossRateInclusive, totalGamePushRate, totalGameWinRateDecided))
