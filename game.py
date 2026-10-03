class TicTacToe:
    """Simple 3x3 Tic-Tac-Toe game board and rules."""

    def __init__(self):
        self.board = [" " for _ in range(9)]

    def display(self):
        print("\n")
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("--+---+--")

    def get_valid_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == " "]

    def make_move(self, position, player):
        if position in self.get_valid_moves():
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in lines:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def is_draw(self):
        return self.check_winner() is None and len(self.get_valid_moves()) == 0

    def is_terminal(self):
        return self.check_winner() is not None or self.is_draw()
