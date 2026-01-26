from games import BlackJackNumpy

numberOfPlayers = 5
numberOfGames = 100000
batchGames = 200000
seed = None

"""DO NOT EDIT BELOW THIS LINE"""

def print_stats(gameStats, numberOfPlayers, numberOfGames):
    hand_decided = gameStats["handPlayerWins"] + gameStats["handDealerWins"]
    hand_total = hand_decided + gameStats["handPushes"]
    game_decided = gameStats["gamePlayerWins"] + gameStats["gameDealerWins"]
    game_total = game_decided + gameStats["gamePushes"]

    if hand_total == 0 or game_total == 0:
        print("Could not deal")
        return

    hand_win_inc = gameStats["handPlayerWins"] / hand_total * 100
    hand_loss_inc = gameStats["handDealerWins"] / hand_total * 100
    hand_push = gameStats["handPushes"] / hand_total * 100
    hand_win_dec = gameStats["handPlayerWins"] / hand_decided * 100 if hand_decided else 0.0

    game_win_inc = gameStats["gamePlayerWins"] / game_total * 100
    game_loss_inc = gameStats["gameDealerWins"] / game_total * 100
    game_push = gameStats["gamePushes"] / game_total * 100
    game_win_dec = gameStats["gamePlayerWins"] / game_decided * 100 if game_decided else 0.0

    print("Number of Players: {}, Number of Games: {}".format(numberOfPlayers, numberOfGames))
    print("PH inc win {:.2f}% loss {:.2f}% push {:.2f}% | PH decided win {:.2f}%".format(
        hand_win_inc, hand_loss_inc, hand_push, hand_win_dec))
    print("PG inc win {:.2f}% loss {:.2f}% push {:.2f}% | PG decided win {:.2f}%".format(
        game_win_inc, game_loss_inc, game_push, game_win_dec))


if __name__ == "__main__":
    stats = BlackJackNumpy.simulate_games(numberOfGames, numberOfPlayers, batch_games=batchGames, seed=seed)
    print_stats(stats, numberOfPlayers, numberOfGames)
