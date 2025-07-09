import random

players = ["human1", "human2"] # variable 1
game_type = "human" # variable 2
who_plays_white = random.choice(players) # variable 3
turn = "white" # variable 4

def test():
  print("Welcome to CHESS-IN-CLI!")
  print("\n")
    # variable 5
  white_board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],  # Rank 8
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],  # Rank 7
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 6
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 5
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 4
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 3
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],  # Rank 2
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],  # Rank 1
    ] 

  black_board = [
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],  # Rank 1
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],  # Rank 2
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 6
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 5
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 4
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 3
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],  # Rank 7
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],  # Rank 8
    ] 


  ranks_one = list(range(8, 0, -1)) # variable 6
  files = [' a', ' b', ' c', ' d', ' e', ' f', ' g', ' h'] # variable 7

  print("---White's view point---\n")
  for i, row in enumerate(white_board):
    print(f"{ranks_one[i]} "+ " ".join(row))

  print(" " + " ".join(files))

  print("\n")

  ranks_two = list(range(1, 9, 1)) # variable 6
  files = [' a', ' b', ' c', ' d', ' e', ' f', ' g', ' h'] # variable 7

  print("---Black's view point---\n")
  for i, row in enumerate(black_board):
    print(f"{ranks_two[i]} "+ " ".join(row))

  print(" " + " ".join(files))

def get_user_input():
  input = input("Your move: ")
  return input

if __name__ == "__main__":
   test()  
