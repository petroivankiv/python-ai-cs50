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


def result(board, action, curr_player):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current = initial_state()

    for i in range(3):
        for j in range(3):
            current[i][j] = board[i][j]

            if (i, j) == action:
                current[i][j] = curr_player

    return current


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_set = []
    o_set = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_set.append((i, j))

            if board[i][j] == O:
                o_set.append((i, j))

    if is_winner(x_set):
        return X

    if is_winner(o_set):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_full = True
    x_set = []
    o_set = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_set.append((i, j))

            if board[i][j] == O:
                o_set.append((i, j))

            if board[i][j] == EMPTY:
                is_full = False

    return is_full or is_winner(x_set) or is_winner(o_set)


def get_score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == None:
        return 0

    return 1 if win == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_moves = actions(board)
    sum = []

    for move in possible_moves:
        counter = 0
        curr_score = 0
        curr_player = player(board)
        current_board = board
        curr_actions = actions(current_board)

        while len(curr_actions) > 0 and counter < 20:
            new_board = result(current_board, move, curr_player)
            score = get_score(new_board)
            curr_actions = actions(new_board)

            curr_player = O if player == X else X
            current_board = new_board
            curr_score += score
            counter += 1

        sum.append((curr_score, move))

    best_sum = sum[0]

    for a in sum:
        if a[1] > best_sum[1]:
            best_sum = a

    return best_sum[1]
