from RPS import player
from RPS_game import quincy, play  # Import the predefined bots and the play function

# Play the game between your bot (player) and quincy for 1000 rounds
play(player, quincy, 1000, verbose=True)

