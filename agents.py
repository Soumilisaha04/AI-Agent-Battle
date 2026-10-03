from minimax import choose_best_move


class Agent:
    def __init__(self, name, depth, heuristic):
        self.name = name
        self.depth = depth
        self.heuristic = heuristic

    def choose_move(self, board, player):
        return choose_best_move(board, player, self.depth, self.heuristic)
