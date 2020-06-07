"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    count = 0
    for row in board:
        count = count + row.count(EMPTY)
    if count % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set ()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    results = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
        ]

    for i in range(3):
        for j in range(3):
            if (i, j) == (action[0], action[1]):
                results[i][j] = player(board)
            else:
                results[i][j] = board[i][j]
    return results


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) == 1 or utility(board) == -1:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
            if board[i][0] == X:
                return 1
            else:
                return -1
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != EMPTY:
            if board[0][i] == X:
                return 1
            else:
                return -1
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY:
        if board[0][0] == X:
            return 1
        else:
            return -1
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != EMPTY:
        if board[0][2] == X:
            return 1
        else:
            return -1
    else:
        return 0

def max_value(board, alpha, beta):
    """
    Returns the maximum value of a state
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        # Alpha beta pruning
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v


def min_value(board, alpha, beta):
    """
    Returns the minimum value of a state
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        # Alpha beta pruning
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    frontier = set()

    # If player maximizes
    if player(board) == X:
        for action in actions(board):
            alpha = - math.inf
            beta = math.inf
            frontier.add((min_value(result(board, action), alpha, beta), action))
        return max(frontier)[1]
    
    # If player minimizes
    if player(board) == O:
        for action in actions(board):
            alpha = - math.inf
            beta = math.inf
            frontier.add((max_value(result(board, action), alpha, beta), action))
        return min(frontier)[1]
