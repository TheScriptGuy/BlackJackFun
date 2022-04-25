from games import BlackJack

from multiprocessing import Process, Pool, Value, Manager, TimeoutError
import os
import random


upperRangeOfGames = 100000
upperRangeOfDecks = 8
upperRangeOfPlayers = 6

numberOfProcesses = 20

"""
DO NOT EDIT BELOW THIS LINE
"""
manager = Manager()
mGameStats = manager.list()


class BJ():
    """ Define the BlackJack class """

    # Game stats for this particular process.
    gameStats = {
        "myPID": os.getpid(),
        "dealerWins": 0,
        "playerWins": 0,
        "gamesPlayed": 0
    }


    def updateStats(self,__gameStats__):
        # update the local gameStats variable with the results of the latest game played.
        self.gameStats["dealerWins"] += __gameStats__["dealerWins"]
        self.gameStats["playerWins"] += __gameStats__["playerWins"]
        self.gameStats["gamesPlayed"] += __gameStats__["gamesPlayed"]

    def playGame(self,__numberOfPlayers,__numberOfDecks):
        # Play a game of Black Jack
        bjGame = BlackJack.BlackJack(__numberOfPlayers,__numberOfDecks)
        
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


    def startGames(self,__numberOfGames):
        # Iterate through all the games that need to be played.
        __counter = 0
        while __counter < __numberOfGames:
            self.playGame(self.numberOfPlayers,self.numberOfDecks)
            __counter += 1
    
    def run(self):
        self.startGames(self.numberOfGames)
        if self.gameStats["dealerWins"] != 0:
            __playerWinRate = self.gameStats["playerWins"] / self.gameStats["dealerWins"] * 100
            print(f"Process ID: {self.myPID}, Player win rate: {__playerWinRate:.2f}")
        else:
            print("Could not deal")
    
    def __init__(self,__numberOfPlayers,__numberOfDecks,__numberOfGames):
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
    with Pool(processes = numberOfProcesses) as pool:
        
        # Arguments for BJ Class
        # numberOfPlayers = random.randint(2,6)
        # numberOfDecks = random.randint(2,8)
        # numberOfGames = random.randint(1000,10000)

        multiple_results = [pool.apply_async(BJ, (random.randint(2,upperRangeOfPlayers),random.randint(2,upperRangeOfDecks),random.randint(1000,upperRangeOfGames))) for i in range(numberOfProcesses)]
        [res.get(timeout=60) for res in multiple_results]
    
    # Gather all the details and sum all the playerWins, dealerWins, and gamesPlayed
    totalPlayerWins = sum([item["playerWins"] for item in mGameStats])
    totalDealerWins = sum([item["dealerWins"] for item in mGameStats])
    totalGamesPlayed = sum([item["gamesPlayed"] for item in mGameStats])

    # Display the results.
    print('Total Player Wins: {}'.format(totalPlayerWins))
    print('Total Dealer Wins: {}'.format(totalDealerWins))
    print('Total Games Played: {}'.format(totalGamesPlayed))
    
    # Calculate the win rate
    totalPlayerWinRate = totalPlayerWins / totalDealerWins * 100

    print(f'Overall player win rate: {totalPlayerWinRate:.3f}')


