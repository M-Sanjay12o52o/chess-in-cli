import chess
import chess.engine

engine_path = "/opt/homebrew/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

def get_computer_move(board: chess.Board) -> str:
    # result = engine.play(board, chess.engine.Limit(time=0.1))
    result = engine.play(board, chess.engine.Limit(time=1))
    board.push(result.move)
    return result.move.uci()

def close_engine():
    engine.quit()
