"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None
currentPlayer = True
test = True


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
    xCount = sum(x.count('X') for x in board)
    oCount = sum(x.count('O') for x in board)
    if(xCount == 0): 
        return X
    elif(xCount > oCount):
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleAction = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if(EMPTY == board[i][j]):
                possibleAction.add((i, j))
    return possibleAction


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copiedState = copy.deepcopy(board)
    player = ''
    xCount = sum(x.count('X') for x in board)
    oCount = sum(x.count('O') for x in board)
    if(xCount == 0): 
        player = X
    elif(xCount > oCount):
        player = O
    else:
        player = X
    try:
        i, j = action
        copiedState[i][j] = player
        return copiedState
    except ValueError:
        pass


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(utility(board) == 1): return X
    elif(utility(board) == -1): 
        return O
    else: None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(EMPTY == board[i][j]):
                if(utility(board) == 1 or utility(board) == -1):
                    return True
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(checkWin(board, X)):
        return 1
    elif(checkWin(board, O)):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # state = copy.deepcopy(board)

    xCount = sum(x.count('X') for x in board)
    oCount = sum(x.count('O') for x in board)
    if(xCount == 0): 
        valueMax = -math.inf
        for action in actions(board):
            tmp = minValue(result(board, action))
            if(tmp > valueMax):
                valueMax = tmp
                act = action
        return act
    elif(xCount > oCount):
        valueMin = math.inf
        for action in actions(board):
            tmp = maxValue(result(board, action))
            if(tmp < valueMin):
                valueMin = tmp
                act = action
        return act
    else:
        valueMax = -math.inf
        for action in actions(board):
            tmp = minValue(result(board, action))
            if(tmp > valueMax):
                valueMax = tmp
                act = action
        return act

def checkWin(b, m):
    return ((b[0][0] == m and b[0][1] == m and b[0][2] == m) or  # H top
            (b[1][0] == m and b[1][1] == m and b[1][2] == m) or  # H mid
            (b[2][0] == m and b[2][1] == m and b[2][2] == m) or  # H bot
            (b[0][0] == m and b[1][0] == m and b[2][0] == m) or  # V left
            (b[0][1] == m and b[1][1] == m and b[2][1] == m) or  # V centre
            (b[0][2] == m and b[1][2] == m and b[2][2] == m) or  # V right
            (b[0][0] == m and b[1][1] == m and b[2][2] == m) or  # LR diag
            (b[0][2] == m and b[1][1] == m and b[2][0] == m))  # RL diag

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v