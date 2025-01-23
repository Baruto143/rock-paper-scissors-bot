import random

def player(prev_play, opponent_history=[]):
    # If it's the first round, choose randomly
    if not prev_play:
        return random.choice(["R", "P", "S"])
    
    # Track the history of moves from the opponent
    opponent_history.append(prev_play)
    
    # Logic to adapt based on the opponent's last move
    if prev_play == "R":
        return "P"  # Paper beats Rock
    elif prev_play == "P":
        return "S"  # Scissors beats Paper
    elif prev_play == "S":
        return "R"  # Rock beats Scissors
    else:
        return random.choice(["R", "P", "S"])  # Fallback to random if there's an issue

