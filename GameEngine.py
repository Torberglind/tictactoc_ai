# Created by: Tor Berglind @https://github.com/Torberglind/unbeatable-tictactoe.git
class GameEngine:
    def __init__(self):
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]


def player_move(row_num: int, col_num: int):
    if board[row_num][col_num] == "_":
        board[row_num][col_num] = "player"
        return True
    else:
        return False
