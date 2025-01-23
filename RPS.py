import random

def detect_pattern(opponent_history):
    if len(opponent_history) >= 3:
        last_three = opponent_history[-3:]
        if last_three[0] == last_three[1] == last_three[2]:
            return last_three[0]  # The opponent is repeating the same move
    return None

def counter_move(move):
    if move == "R":
        return "P"  # Paper beats Rock
    elif move == "P":
        return "S"  # Scissors beats Paper
    elif move == "S":
        return "R"  # Rock beats Scissors
    return random.choice(["R", "P", "S"])  # Random move if no pattern detected

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    predicted_move = detect_pattern(opponent_history)
    
    if predicted_move:
        return counter_move(predicted_move)
    
    return random.choice(["R", "P", "S"])  # Random move if no pattern detected
