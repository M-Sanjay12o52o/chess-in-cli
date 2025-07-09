from board import create_board, print_board

if __name__ == "__main__":
  board = create_board()
  print("\n--- White's View ---")
  print_board(board, flip=False)
  print("\n--- Black's View ---")
  print_board(board, flip=True)
