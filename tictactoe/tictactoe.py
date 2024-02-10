"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

WIN_COMPBINATIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]


def is_winner(score_list):
    for comb in WIN_COMPBINATIONS:
        if all(s in score_list for s in comb):
            return True

    return False


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_counter += 1

            if cell == O:
                o_counter += 1

    return X if x_counter == o_counter else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = initial_state()
    curr_player = player(board)

    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]

            if (i, j) == action:
                new_board[i][j] = curr_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_moves = []
    o_moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_moves.append((i, j))

            if board[i][j] == O:
                o_moves.append((i, j))

    if is_winner(x_moves):
        return X

    if is_winner(o_moves):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_full = True
    x_moves = []
    o_moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_moves.append((i, j))

            if board[i][j] == O:
                o_moves.append((i, j))

            if board[i][j] == EMPTY:
                is_full = False

    return is_full or is_winner(x_moves) or is_winner(o_moves)


def get_score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == None:
        return 0

    return 1 if win == X else -1


def max_value(board):
    if terminal(board):
        return get_score(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return get_score(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curr_player = player(board)
    score = 0
    move = ()

    for action in actions(board):
        if curr_player == X:
            v = min_value(result(board, action))

            if v >= score:
                score = v
                move = action

        if curr_player == O:
            v = max_value(result(board, action))

            if v <= score:
                score = v
                move = action

    return move
