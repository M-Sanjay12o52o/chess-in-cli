import random

def test():
  print("Welcome to CHESS-IN-CLI!")
  print("\n")
  players = ["human1", "human2"]
  game_type = "human"
  who_plays_white = random.choice(players)
  turn = "white" 
  board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],  # Rank 8
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],  # Rank 7
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 6
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 5
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 4
    ["--", "--", "--", "--", "--", "--", "--", "--"],  # Rank 3
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],  # Rank 2
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],  # Rank 1
    ] 

  ranks = list(range(8, 0, -1))
  files = [' a', ' b', ' c', ' d', ' e', ' f', ' g', ' h']

  for i, row in enumerate(board):
     print(f"{ranks[i]} "+ " ".join(row))

  print(" " + " ".join(files))

if __name__ == "__main__":
   test()  
