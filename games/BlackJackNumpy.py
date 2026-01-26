import numpy as np

CARD_VALUES = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], dtype=np.int8)


def _hand_totals(num_hands, rng):
    """Simulate blackjack hands (hit until 17) and return final totals."""
    cards = rng.integers(0, 13, size=(num_hands, 2), dtype=np.int8)
    values = CARD_VALUES[cards]
    total_low = values.sum(axis=1).astype(np.int16)
    has_ace = (cards == 0).any(axis=1)
    total = total_low + ((has_ace & (total_low + 10 <= 21)) * 10).astype(np.int16)

    active = total < 17
    while active.any():
        draw = rng.integers(0, 13, size=active.sum(), dtype=np.int8)
        total_low[active] += CARD_VALUES[draw]
        has_ace[active] |= (draw == 0)
        total_active = total_low[active]
        ace_active = has_ace[active]
        total[active] = total_active + ((ace_active & (total_active + 10 <= 21)) * 10).astype(np.int16)
        active = total < 17

    return total


def simulate_games(num_games, num_players, batch_games=100000, seed=None):
    """Simulate blackjack with an infinite shoe using vectorized NumPy operations."""
    rng = np.random.default_rng(seed)
    stats = {
        "handDealerWins": 0,
        "handPlayerWins": 0,
        "handPushes": 0,
        "gameDealerWins": 0,
        "gamePlayerWins": 0,
        "gamePushes": 0,
        "gamesPlayed": 0,
    }

    remaining = num_games
    while remaining > 0:
        batch = min(batch_games, remaining)
        dealer_total = _hand_totals(batch, rng)
        player_total = _hand_totals(batch * num_players, rng).reshape(batch, num_players)

        dealer_total_b = dealer_total[:, None]
        player_bust = player_total > 21
        dealer_bust = dealer_total > 21

        player_win = (~player_bust) & (dealer_bust[:, None] | (player_total > dealer_total_b))
        player_loss = player_bust | ((~dealer_bust[:, None]) & (player_total < dealer_total_b))
        push = (~player_bust) & (~dealer_bust[:, None]) & (player_total == dealer_total_b)

        hand_player_wins = int(player_win.sum())
        hand_dealer_wins = int(player_loss.sum())
        hand_pushes = int(push.sum())

        wins_per_game = player_win.sum(axis=1)
        losses_per_game = player_loss.sum(axis=1)

        game_player_wins = int((wins_per_game > losses_per_game).sum())
        game_dealer_wins = int((wins_per_game < losses_per_game).sum())
        game_pushes = batch - game_player_wins - game_dealer_wins

        stats["handDealerWins"] += hand_dealer_wins
        stats["handPlayerWins"] += hand_player_wins
        stats["handPushes"] += hand_pushes
        stats["gameDealerWins"] += game_dealer_wins
        stats["gamePlayerWins"] += game_player_wins
        stats["gamePushes"] += game_pushes
        stats["gamesPlayed"] += batch

        remaining -= batch

    return stats
