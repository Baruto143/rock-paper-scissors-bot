import random

# Define predefined bots
def quincy(prev_play, opponent_history=[]):
    # Quincy plays rock every time (simple bot)
    return "R"

def random_bot(prev_play, opponent_history=[]):
    # Random bot that picks any move randomly
    return random.choice(["R", "P", "S"])

# Function to determine the winner of a round
def round_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return "Tie"
    if (player1_move == "R" and player2_move == "S") or \
       (player1_move == "P" and player2_move == "R") or \
       (player1_move == "S" and player2_move == "P"):
        return "Player 1"
    else:
        return "Player 2"

# Function to play a match between two players
def play(player1, player2, num_games, verbose=False):
    player1_score = 0
    player2_score = 0
    player1_history = []  # Initialize history for player 1
    player2_history = []  # Initialize history for player 2
    
    for _ in range(num_games):
        # Get moves from both players
        player1_move = player1("", player1_history) if _ == 0 else player1(player2_move, player1_history)
        player2_move = player2("", player2_history) if _ == 0 else player2(player1_move, player2_history)
        
        # Append the moves to each player's history
        player1_history.append(player1_move)
        player2_history.append(player2_move)
        
        # Determine the winner of the round
        winner = round_winner(player1_move, player2_move)
        
        if winner == "Player 1":
            player1_score += 1
        elif winner == "Player 2":
            player2_score += 1
        
        # Optionally display each round
        if verbose:
            print(f"Round {_ + 1}: Player 1 chose {player1_move}, Player 2 chose {player2_move} -> Winner: {winner}")
    
    print(f"\nFinal Score: Player 1 - {player1_score}, Player 2 - {player2_score}")
    
    if player1_score > player2_score:
        return "Player 1 wins"
    elif player2_score > player1_score:
        return "Player 2 wins"
    else:
        return "It's a tie"

# Sample call to play the game (for testing)
# play(player, quincy, 1000, verbose=True)