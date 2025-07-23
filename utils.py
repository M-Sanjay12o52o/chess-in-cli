def get_piece_symbol(piece_code):
    symbol_map = {
        "bK": "♔", "bQ": "♕", "bR": "♖", "bB": "♗", "bN": "♘", "bp": "♙",
        "wK": "♚", "wQ": "♛", "wR": "♜", "wB": "♝", "wN": "♞", "wp": "♟"
    }
    # Extract piece type (e.g., "wK ", "bp1" → "wK", "bp")
    key = piece_code[:2]
    # return symbol_map.get(key, "*")
    return symbol_map.get(key, ".")
