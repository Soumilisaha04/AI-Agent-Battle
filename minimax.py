import random
class SearchStats:
    def __init__(self):
        self.nodes = 0
        self.pruned = 0


def minimax(board, depth, maximizing, ai_player, opponent, heuristic, alpha, beta, stats):
    stats.nodes += 1

    winner = check_winner_board(board)
    if winner == ai_player:
        return 100 + depth
    if winner == opponent:
        return -100 - depth
    if depth == 0 or " " not in board:
        return heuristic(board, ai_player)

    moves = [i for i, cell in enumerate(board) if cell == " "]

    if maximizing:
        best = -float("inf")
        for move in moves:
            board[move] = ai_player
            value = minimax(board, depth - 1, False, ai_player, opponent,
                            heuristic, alpha, beta, stats)
            board[move] = " "
            best = max(best, value)
            alpha = max(alpha, best)
            if beta <= alpha:
                stats.pruned += len(moves) - moves.index(move) - 1
                break
        return best
    else:
        best = float("inf")
        for move in moves:
            board[move] = opponent
            value = minimax(board, depth - 1, True, ai_player, opponent,
                            heuristic, alpha, beta, stats)
            board[move] = " "
            best = min(best, value)
            beta = min(beta, best)
            if beta <= alpha:
                stats.pruned += len(moves) - moves.index(move) - 1
                break
        return best


def check_winner_board(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def choose_best_move(board, ai_player, depth, heuristic):
    opponent = "O" if ai_player == "X" else "X"
    stats = SearchStats()
    best_score = -float("inf")
    best_moves = []

    for move in [i for i, cell in enumerate(board) if cell == " "]:
        board[move] = ai_player
        score = minimax(
            board, depth - 1, False, ai_player, opponent,
            heuristic, -float("inf"), float("inf"), stats
        )
        board[move] = " "

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    # Random choice is only between equally good moves.
    move = random.choice(best_moves)
    return move, stats
