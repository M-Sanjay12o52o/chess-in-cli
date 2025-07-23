import os
import time
import chess
from board import create_board, print_board, center_line
from engine_interface import get_computer_move, close_engine

def validate_user_input(board):
  while True:
    # - [ ] Display the last move that was made and who made it as text always
    user_input = input("Your move (e.g., e2e4): ")
    try:
      move_obj = chess.Move.from_uci(user_input)
      is_castling = board.is_castling(move_obj)# this returns true for both right&left castle
      if is_castling:
        to_square = move_obj.to_square
        to_square_name = chess.square_name(to_square)

        if to_square_name in ("g1", "g8"):
            print("🏰 Kingside castling")
        elif to_square_name in ("c1", "c8"):
            print("🏰 Queenside castling")
        else:
            print("⚠️ Unexpected castling move")
      print("is_castling: ", is_castling)
      # based on this variable `is_castling` 
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
    board_msg = center_line("--- Chess Board ---")
    # print("\n--- Custom Board ---")
    if engine_board.move_stack:
      last_move = engine_board.peek()
      if engine_board.is_castling(last_move):
        print("Last move was a castle")
      if (engine_board.is_check()):
        print("Last move:", engine_board.peek().uci(), "CHECK")
      else:
        print("Last move:", engine_board.peek().uci())
    else:
      print("No moves made yet.")
    print(board_msg)
    print_board(custom_board, flip=False)

    # print("\n--- python-chess Board ---")
    # print(engine_board)
    if move == "white":
      user_input = validate_user_input(engine_board)
      # this is where we need to add logic to have the castle move be reflected on our
      # custom board as well
      engine_board.push_uci(user_input)

      from_cell, to_cell = user_input[:2], user_input[2:]
      custom_board[to_cell] = custom_board[from_cell]
      custom_board[from_cell] = "---"

      time.sleep(1)

      if engine_board.is_check():
        print(f"⚠️ {move.capitalize()} is in check!")
    else:
      move_played = get_computer_move(engine_board)
      print(f"Black (computer) played: {move_played}")


      from_cell, to_cell = move_played[:2], move_played[2:]
      custom_board[to_cell] = custom_board[from_cell]
      custom_board[from_cell] = "---"

      time.sleep(1)

      if engine_board.is_check():
        print(f"⚠️ {move.capitalize()} is in check!")

    move = "black" if move == "white" else "white"

  
  print("Game Over: ", engine_board.result())
  close_engine()
