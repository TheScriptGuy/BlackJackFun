from multiprocessing import Pool
import os

from games import BlackJackNumpy

numberOfPlayers = 5
numberOfGames = 100000000
batchGames = 2000000
numberOfProcesses = 10

"""DO NOT EDIT BELOW THIS LINE"""

def _worker(args):
    num_games, num_players, batch_games, seed = args
    return BlackJackNumpy.simulate_games(num_games, num_players, batch_games=batch_games, seed=seed)


def _merge_stats(stats_list):
    merged = {
        "handDealerWins": 0,
        "handPlayerWins": 0,
        "handPushes": 0,
        "gameDealerWins": 0,
        "gamePlayerWins": 0,
        "gamePushes": 0,
        "gamesPlayed": 0,
    }
    for stats in stats_list:
        for key in merged:
            merged[key] += stats[key]
    return merged


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

    print("Number of Players: {}, Number of Games: {}, Processes: {}".format(
        numberOfPlayers, numberOfGames, numberOfProcesses))
    print("PH inc win {:.2f}% loss {:.2f}% push {:.2f}% | PH decided win {:.2f}%".format(
        hand_win_inc, hand_loss_inc, hand_push, hand_win_dec))
    print("PG inc win {:.2f}% loss {:.2f}% push {:.2f}% | PG decided win {:.2f}%".format(
        game_win_inc, game_loss_inc, game_push, game_win_dec))


if __name__ == "__main__":
    base_games = numberOfGames // numberOfProcesses
    remainder = numberOfGames % numberOfProcesses
    work = []
    for i in range(numberOfProcesses):
        games_for_worker = base_games + (1 if i < remainder else 0)
        if games_for_worker == 0:
            continue
        work.append((games_for_worker, numberOfPlayers, batchGames, 1000 + i))

    with Pool(processes=numberOfProcesses) as pool:
        results = pool.map(_worker, work)

    merged = _merge_stats(results)
    print_stats(merged, numberOfPlayers, numberOfGames)
