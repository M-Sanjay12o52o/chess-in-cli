import os
import chess
from board import create_board, print_board
from engine_interface import get_computer_move, close_engine

def validate_user_input(board):
  while True:
    user_input = input("Your move (e.g., e2e4): ")
    try:
      move_obj = chess.Move.from_uci(user_input)
      if move_obj in board.legal_moves:
        return user_input
      else:
        print("❌ Illegal move. Try again.")
    except:
      print("❌ Invalid input format. Try again.")


def play_game():
  custom_board = create_board()
  engine_board = chess.Board()
  move = "white"

  while not engine_board.is_game_over():
    os.system("clear") # clears the temrminal
    print("\n--- Custom Board ---")
    print_board(custom_board, flip=False)

    # print("\n--- python-chess Board ---")
    # print(engine_board)
    if move == "white":
      user_input = validate_user_input(engine_board)
      engine_board.push_uci(user_input)

      from_cell, to_cell = user_input[:2], user_input[2:]
      custom_board[to_cell] = custom_board[from_cell]
      custom_board[from_cell] = "---"
    else:
      move_played = get_computer_move(engine_board)
      print(f"Black (computer) played: {move_played}")


      from_cell, to_cell = move_played[:2], move_played[2:]
      custom_board[to_cell] = custom_board[from_cell]
      custom_board[from_cell] = "---"

    
    move = "black" if move == "white" else "white"

  
  print("Game Over: ", engine_board.result())
  close_engine()

if __name__ == "__main__":
  play_game()