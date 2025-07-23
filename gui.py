import tkinter as tk
from tkinter import messagebox
import chess
from board import create_board
from engine_interface import get_computer_move, close_engine
from utils import get_piece_symbol

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess in GUI")
        self.engine_board = chess.Board()
        self.custom_board = create_board()
        self.selected_square = None
        self.buttons = {}
        self.move_history = []
        self.status_var = tk.StringVar()
        self.user_turn = True  # Only allow input on user's turn
        self.last_move_squares = set()  # Store last move as set of square names
        self.create_widgets()
        self.update_board()
        self.update_status()

    def create_widgets(self):
        board_frame = tk.Frame(self.root)
        board_frame.grid(row=0, column=0, padx=10, pady=10)
        files = "abcdefgh"
        ranks = "87654321"
        for r, rank in enumerate(ranks):
            for f, file in enumerate(files):
                square = file + rank
                btn = tk.Button(
                    board_frame, text="", width=4, height=2,
                    font=("Arial", 24),
                    command=lambda sq=square: self.on_square_click(sq)
                )
                btn.grid(row=r, column=f)
                self.buttons[square] = btn
        # Move history
        self.history_text = tk.Text(self.root, width=30, height=20, state='disabled')
        self.history_text.grid(row=0, column=1, padx=10, pady=10, sticky='n')
        # Status
        status_label = tk.Label(self.root, textvariable=self.status_var, font=("Arial", 14))
        status_label.grid(row=1, column=0, columnspan=2, pady=5)

    def update_board(self):
        files = "abcdefgh"
        ranks = "87654321"
        for r, rank in enumerate(ranks):
            for f, file in enumerate(files):
                square = file + rank
                piece = self.custom_board.get(square, "---")
                symbol = get_piece_symbol(piece)
                btn = self.buttons[square]
                btn.config(text=symbol)
                # Determine background color
                if self.selected_square == square:
                    bg = "yellow"
                elif square in self.last_move_squares:
                    bg = "#87cefa"  # light blue
                elif (r + f) % 2 == 0:
                    bg = "#f0d9b5"  # light square
                else:
                    bg = "#b58863"  # dark square
                btn.config(bg=bg, activebackground=bg)
                # Disable all buttons if not self.user_turn:
                if not self.user_turn:
                    btn.config(state=tk.DISABLED)
                else:
                    btn.config(state=tk.NORMAL)

    def update_status(self, msg=None):
        if msg:
            self.status_var.set(msg)
            return
        if self.engine_board.is_check():
            self.status_var.set("Check!")
        elif self.engine_board.is_game_over():
            self.status_var.set(f"Game Over: {self.engine_board.result()}")
        else:
            turn = "White" if self.engine_board.turn else "Black"
            self.status_var.set(f"{turn}'s move")

    def on_square_click(self, square):
        if not self.user_turn or self.engine_board.is_game_over():
            self.update_status()
            return
        if self.selected_square is None:
            # Select a piece
            piece = self.custom_board.get(square, "---")
            if piece.startswith("w") and self.engine_board.turn:
                self.selected_square = square
                self.update_board()
                self.update_status("Select a destination square.")
            else:
                self.update_status("Select a white piece to move.")
        elif self.selected_square == square:
            # Deselect if clicking the same square
            self.selected_square = None
            self.update_board()
            self.update_status("Selection cleared.")
        else:
            # Try to make a move
            from_sq = self.selected_square
            to_sq = square
            self.try_user_move(from_sq, to_sq)

    def try_user_move(self, from_sq, to_sq):
        move_uci = from_sq + to_sq
        try:
            move_obj = chess.Move.from_uci(move_uci)
            if move_obj in self.engine_board.legal_moves:
                self.engine_board.push(move_obj)
                self.custom_board[to_sq] = self.custom_board[from_sq]
                self.custom_board[from_sq] = "---"
                self.move_history.append(f"White: {move_uci}")
                self.last_move_squares = {from_sq, to_sq}
                self.update_history()
                self.selected_square = None
                self.user_turn = False
                self.update_board()
                self.update_status("Computer is thinking...")
                self.root.after(500, self.computer_move)
            else:
                self.update_status("Illegal move.")
                self.selected_square = None
                self.update_board()
        except Exception as e:
            self.update_status("Invalid move.")
            self.selected_square = None
            self.update_board()

    def computer_move(self):
        if self.engine_board.is_game_over():
            self.update_status()
            return
        move_played = get_computer_move(self.engine_board)
        try:
            move_obj = chess.Move.from_uci(move_played)
            from_sq = chess.square_name(move_obj.from_square)
            to_sq = chess.square_name(move_obj.to_square)
            self.last_move_squares = {from_sq, to_sq}
        except Exception:
            self.last_move_squares = set()
        self.custom_board[to_sq] = self.custom_board[from_sq]
        self.custom_board[from_sq] = "---"
        self.move_history.append(f"Black: {move_played}")
        self.update_history()
        self.user_turn = True
        self.update_board()
        self.update_status()
        if self.engine_board.is_game_over():
            self.update_status()
            close_engine()

    def update_history(self):
        self.history_text.config(state='normal')
        self.history_text.delete(1.0, tk.END)
        for move in self.move_history:
            self.history_text.insert(tk.END, move + "\n")
        self.history_text.config(state='disabled')

def main():
    root = tk.Tk()
    app = ChessGUI(root)
    root.mainloop()
