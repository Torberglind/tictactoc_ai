# Created by: Tor Berglind @https://github.com/Torberglind/unbeatable-tictactoe.git
# Credit to: http://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-2-evaluation-function/
class GameEngine:
    def __init__(self):
        self.board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]


def player_move(row_num: int, col_num: int):
    if board[row_num][col_num] == "_":
        board[row_num][col_num] = "PL"
        return True
    else:
        return False


#returns max/min/0 based on who is winning
def evaluate():

    for i in range (0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == "PL":
                return +10
            else if board[i][0] == "AI":
                return -10
    for j in range (0, 3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            if board[0][j] == "PL":
                return +10
            else if board[0][j] == "AI":
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "PL":
            return +10
        else if board[0][0] == "AI":
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == "PL":
            return +10
        else if board[0][2] == "AI":
            return -10

    else: return 0