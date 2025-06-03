"""
Tic Tac Toe Player
"""

import math

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
    # Count Xs and Os in board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    # Loop through possible actions and add them to the actions set
    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if move is out of bounds (out of grid)
    i, j = action
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        raise ValueError("Move is out of bounds")

    # If space is not empty show invalid move
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid Move")

    # Create a copy of the board
    new_board = [row[:] for row in board]
    # Apply move with actual player
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for the winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # Check columns for the winner
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # If there is no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks if there is a winner
    if winner(board) is not None:
        return True

    # Check if there are empty spaces on the board
    for row in board:
        if EMPTY in row:
            return False

    # No empty spaces and winner means it's game over
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If game over return None
    if terminal(board):
        return None
    # Get player and initialize best move
    current_player = player(board)
    bestmove = None

    # If it's X turn
    if current_player == X:
        # Start with lowest possible score
        bestscore = -math.inf
        for action in actions(board):
            # Get result of making this action
            new_board = result(board, action)
            # Get the score from O perspective
            score = min_value(new_board)
            # If this score is better than the best found update best move to this action
            if score > bestscore:
                bestscore = score
                bestmove = action
    # If it's O turn
    else:
        # Start with highest possible score
        bestscore = math.inf
        for action in actions(board):
            # Get result of making this action
            new_board = result(board, action)
            # Get the score from X perspective
            score = max_value(new_board)
            # If this score is better than the best found update best move to this action
            if score < bestscore:
                bestscore = score
                bestmove = action

    return bestmove

def max_value(board):

    # if game's over
    if terminal(board):
        return utility(board)
    # Set v to minus infinity
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):

    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board,action)))

    return v
