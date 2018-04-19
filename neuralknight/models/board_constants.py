__all__ = [
    'INITIAL_BOARD',
    'BISHOP', 'KING', 'KNIGHT', 'PAWN', 'QUEEN', 'ROOK',
    'BISHOP_MOVES', 'KING_MOVES', 'KNIGHT_MOVES', 'QUEEN_MOVES', 'ROOK_MOVES',
    'unit']

BISHOP = 0B10
KING = 0B100
KNIGHT = 0B110
PAWN = 0B1000
QUEEN = 0B1010
ROOK = 0B1100

_FIRST_ROW = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
_PAWN_ROW = [PAWN for _ in range(8)]

# INITIAL_BOARD = [
#     _FIRST_ROW,
#     _PAWN_ROW,
#     *[[0 for _ in range(8)] for _ in range(4)],
#     [piece | 1 for piece in _PAWN_ROW],
#     [piece | 1 for piece in _FIRST_ROW]]
INITIAL_BOARD = [
    [ROOK, KNIGHT, BISHOP, QUEEN, KING, 0, 0, ROOK],
    [0, PAWN, 0, PAWN, PAWN, PAWN, BISHOP, PAWN],
    [0, 0, 0, 0, 0, 0, PAWN, KNIGHT],
    [PAWN, 0, PAWN, 0, 0, 0, 0, 0],
    [0, 0, 0, PAWN | 1, PAWN | 1, PAWN | 1, 0, 0],
    [0, 0, 0, 0, BISHOP | 1, KNIGHT | 1, 0, 0],
    [PAWN | 1, PAWN | 1, PAWN | 1, 0, 0, 0, PAWN | 1, PAWN | 1],
    [ROOK | 1, KNIGHT | 1, 0, QUEEN | 1, KING | 1, BISHOP | 1, 0, ROOK | 1]]
# low bit indicates active player piece

BISHOP_MOVES = (
    (-8, -8), (-7, -7), (-6, -6), (-5, -5),
    (-4, -4), (-3, -3), (-2, -2), (-1, -1),
    (1, 1), (2, 2), (3, 3), (4, 4),
    (5, 5), (6, 6), (7, 7), (8, 8),
    (-8, 8), (-7, 7), (-6, 6), (-5, 5),
    (-4, 4), (-3, 3), (-2, 2), (-1, 1),
    (1, -1), (2, -2), (3, -3), (4, -4),
    (5, -5), (6, -6), (7, -7), (8, -8))
KING_MOVES = (
  (-1, -1), (-1, 0), (-1, 1), (0, -1),
  (0, 1), (1, -1), (1, 0), (1, 1))
KNIGHT_MOVES = (
  (-2, -1), (-2, 1), (-1, -2), (-1, 2),
  (1, -2), (1, 2), (2, -1), (2, 1))
QUEEN_MOVES = (
  (-8, -8), (-7, -7), (-6, -6), (-5, -5),
  (-4, -4), (-3, -3), (-2, -2), (-1, -1),
  (1, 1), (2, 2), (3, 3), (4, 4),
  (5, 5), (6, 6), (7, 7), (8, 8),
  (-8, 8), (-7, 7), (-6, 6), (-5, 5),
  (-4, 4), (-3, 3), (-2, 2), (-1, 1),
  (1, -1), (2, -2), (3, -3), (4, -4),
  (5, -5), (6, -6), (7, -7), (8, -8),
  (0, -8), (0, -7), (0, -6), (0, -5),
  (0, -4), (0, -3), (0, -2), (0, -1),
  (0, 1), (0, 2), (0, 3), (0, 4),
  (0, 5), (0, 6), (0, 7), (0, 8),
  (-8, 0), (-7, 0), (-6, 0), (-5, 0),
  (-4, 0), (-3, 0), (-2, 0), (-1, 0),
  (1, 0), (2, 0), (3, 0), (4, 0),
  (5, 0), (6, 0), (7, 0), (8, 0)
)
ROOK_MOVES = (
  (0, -8), (0, -7), (0, -6), (0, -5),
  (0, -4), (0, -3), (0, -2), (0, -1),
  (0, 1), (0, 2), (0, 3), (0, 4),
  (0, 5), (0, 6), (0, 7), (0, 8),
  (-8, 0), (-7, 0), (-6, 0), (-5, 0),
  (-4, 0), (-3, 0), (-2, 0), (-1, 0),
  (1, 0), (2, 0), (3, 0), (4, 0),
  (5, 0), (6, 0), (7, 0), (8, 0)
)


def unit(i):
    return -1 if i < 0 else (0 if i == 0 else 1)
