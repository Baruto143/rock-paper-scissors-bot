import random

def rock(prev_play):
    """Opponent always plays rock."""
    return "R"

def random_player(prev_play):
    """Opponent plays randomly."""
    return random.choice(["R", "P", "S"])

def play(player1, player2, num_games, verbose=False):
    """
    Plays a game of Rock, Paper, Scissors between two players.

    Args:
      player1: A function representing the first player's strategy.
      player2: A function representing the second player's strategy.
      num_games: The number of games to play.
      verbose: Whether to print detailed game logs.

    Returns:
      float: The win rate of player1.
    """
    p1_wins = 0
    p2_wins = 0
    prev_play = ""

    for _ in range(num_games):
        p1_play = player1(prev_play)
        p2_play = player2(prev_play)

        if (p1_play == "R" and p2_play == "S") or \
           (p1_play == "P" and p2_play == "R") or \
           (p1_play == "S" and p2_play == "P"):
            p1_wins += 1
        elif p1_play != p2_play:
            p2_wins += 1

        prev_play = p2_play

        if verbose:
            print(f"Player 1: {p1_play} | Player 2: {p2_play}")

    win_rate = p1_wins / num_games
    print(f"Player 1 win rate: {win_rate:.2f}")
    return win_rate

# Import your player function
from RPS import player

# Play against different opponents
play(player, rock, 1000)
play(player, random_player, 1000)
