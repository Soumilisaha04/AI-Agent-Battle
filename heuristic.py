def heuristic_h1(board, ai_player):
    """H1: rewards winning lines, center and corners."""
    opponent = "O" if ai_player == "X" else "X"
    score = 0

    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for line in lines:
        values = [board[i] for i in line]
        ai_count = values.count(ai_player)
        opp_count = values.count(opponent)

        if ai_count > 0 and opp_count == 0:
            if ai_count == 2:
                score += 10
            elif ai_count == 1:
                score += 3
        elif opp_count > 0 and ai_count == 0:
            if opp_count == 2:
                score -= 10
            elif opp_count == 1:
                score -= 3

    if board[4] == ai_player:
        score += 3
    elif board[4] == opponent:
        score -= 3

    for i in [0, 2, 6, 8]:
        if board[i] == ai_player:
            score += 2
        elif board[i] == opponent:
            score -= 2

    return score


def heuristic_h2(board, ai_player):
    """H2: strongly values immediate threats and positional control."""
    opponent = "O" if ai_player == "X" else "X"
    score = 0

    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for line in lines:
        values = [board[i] for i in line]
        ai_count = values.count(ai_player)
        opp_count = values.count(opponent)

        if ai_count > 0 and opp_count == 0:
            if ai_count == 2:
                score += 15
            elif ai_count == 1:
                score += 2
        elif opp_count > 0 and ai_count == 0:
            if opp_count == 2:
                score -= 15
            elif opp_count == 1:
                score -= 2

    if board[4] == ai_player:
        score += 5
    elif board[4] == opponent:
        score -= 5

    for i in [0, 2, 6, 8]:
        if board[i] == ai_player:
            score += 1
        elif board[i] == opponent:
            score -= 1

    return score
