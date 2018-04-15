# import adam's module up here
from random import randint
from numpy import array as ndarray

def evaluate_boards(boards):
    '''Determine value for each board state in array of board states
    
    Inputs:
        boards: Array of board states

    Outputs:
        best_state: The highest valued board state in the array

    '''

    # Piece values
    pawn_val = 1
    knight_val = 3
    bishop_val = 3
    rook_val = 5
    queen_val = 10
    king_val = 200

    # Piece squares - from http://www.chessbin.com/post/Piece-Square-Table
    own_pawn_squares = [
         [0,  0,  0,  0,  0,  0,  0,  0,]
        [50, 50, 50, 50, 50, 50, 50, 50,]
        [10, 10, 20, 30, 30, 20, 10, 10,]
         [5,  5, 10, 27, 27, 10,  5,  5,]
         [0,  0,  0, 25, 25,  0,  0,  0,]
         [5, -5,-10,  0,  0,-10, -5,  5,]
         [5, 10, 10,-25,-25, 10, 10,  5,]
         [0,  0,  0,  0,  0,  0,  0,  0,]
    ]

    opp_pawn_squares = [
         [0,  0,  0,  0,  0,  0,  0,  0,]
         [0,  0,  0,  0,  0,  0,  0,  0,]
         [-5,-5,-10,-15,-15,-10, -5, -5,]
         [0,  0,  0, -25, -25,  0,  0,  0,]
         [-5,  -5, -10, -27, -27, -10,  -5,  -5,]
        [-10, -10, -20, -30, -30, -20, -10, -10,]
        [-50, -50, -50, -50, -50, -50, -50, -50,]
         [0,  0,  0,  0,  0,  0,  0,  0,]
    ]

    own_knight_squares = [
        [-50,-40,-30,-30,-30,-30,-40,-50],
        [-40,-20,  0,  0,  0,  0,-20,-40],
        [-30,  0, 10, 15, 15, 10,  0,-30],
        [-30,  5, 15, 20, 20, 15,  5,-30],
        [-30,  0, 15, 20, 20, 15,  0,-30],
        [-30,  5, 10, 15, 15, 10,  5,-30],
        [-40,-20,  0,  5,  5,  0,-20,-40],
        [-50,-40,-20,-30,-30,-20,-40,-50],
    ]

    opp_knight_squares = [
        [-50,-40,-30,-30,-30,-30,-40,-50],
        [-40,-20,  0,  0,  0,  0,-20,-40],
        [-30,  0, 10, 15, 15, 10,  0,-30],
        [-30,  5, 15, 20, 20, 15,  5,-30],
        [-30,  0, 15, 20, 20, 15,  0,-30],
        [-30,  5, 10, 15, 15, 10,  5,-30],
        [-40,-20,  0,  5,  5,  0,-20,-40],
        [-50,-40,-20,-30,-30,-20,-40,-50],
    ]

    own_bishop_squares = [
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-20,-10,-40,-10,-10,-40,-10,-20],
    ]

    opp_bishop_squares = [
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-20,-10,-40,-10,-10,-40,-10,-20],
    ]
    
    own_king_squares = [
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-20,-10,-40,-10,-10,-40,-10,-20],
    ]

    opp_king_squares = [
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-20,-10,-40,-10,-10,-40,-10,-20],
    ]    

    zero_squares = [
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
         [0,  0,  0,  0,  0,  0,  0,  0],
    ]

    # Pair encoded pieces to values
    value_map = {
        9 : (pawn_val, own_pawn_squares),
        7 : (knight_val, own_knight_squares),
        3 : (bishop_val, own_bishop_squares),
        13: (rook_val, own_rook_squares),
        11: (queen_val, zero_squares),
        5 : (king_val, opp_king_squares),
        
        8 : (-pawn_val, opp_pawn_squares),
        6 : (-knight_val, opp_knight_squares),
        2 : (-bishop_val, opp_bishop_squares),
        12: (-rook_val, opp_rook_squares),
        10: (-queen_val, zero_squares),
        4 : (-king_val, opp_king_squares),
        
        0 : (0, zero_squares),
    }

    boards = (([[12, 6, 2, 10, 4, 2, 6, 12], [8, 8, 8, 8, 8, 8, 8, 8], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [9, 9, 9, 9, 9, 9, 9, 9], [13, 7, 3, 11, 5, 3, 7, 13]]))

    best_board = boards[0]
    best_board_score = -999999
    for board in boards:
        board_score = 0
        for row in board:
            for col in row:
                board_score += value_map[col][0]
                board_score += value_map[col][1][row][col]
        if board_score > best_board_score:
            best_board_score = board_score
            best_board = board

    return best_board
