import random

def player(prev_play):
  """
  This function defines the core strategy of your RPS program.

  Args:
      prev_play (str): The opponent's previous move ("R", "P", or "S").
                     If it's the first game, prev_play will be an empty string.

  Returns:
      str: Your next move ("R", "P", or "S").
  """

  # Simple strategy: Cycle through moves
  if prev_play == "":
    return "R"  # Start with Rock
  elif prev_play == "R":
    return "P"
  elif prev_play == "P":
    return "S"
  else:
    return "R"

  # You can implement more sophisticated strategies here, 
  # such as:
  # - Tracking opponent's move frequencies
  # - Using machine learning models