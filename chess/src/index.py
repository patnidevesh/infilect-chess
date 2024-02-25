from .bishop import *
from .queen import *
from .rook import *
from .knight import *
from .king import *
from .utils import *

Piece = {
    "QUEEN":"Queen",
    "KNIGHT":"Knight",
    "BISHOP":"Bishop",
    "ROOK":"Rook",
    "KING":"King"
}

def get_piece_moves(piece, position):
        row, col = position_to_row_col(position)
        piece_available_moves = None
        if piece == Piece["QUEEN"]:
            piece_available_moves = Queen().get_moves(row,col)
        if piece == Piece["KNIGHT"]:
            piece_available_moves = Knight().get_moves(row,col)
        if piece == Piece["BISHOP"]:
            piece_available_moves = Bishop().get_moves(row,col)
        if piece == Piece["ROOK"]:
            piece_available_moves = Rook().get_moves(row,col)
        if piece == Piece["KING"]:
            piece_available_moves = King().get_moves(row,col)
        return piece_available_moves

def get_available_moves(slug,positions):
    all_available_moves = []
    for piece in positions:
        if piece != slug:
            piece_moves = get_piece_moves(piece,positions[piece])
            all_available_moves.extend(piece_moves)
    
    all_available_moves = [row_col_to_position(row, col) for row, col in all_available_moves]
    all_available_moves = list(set(all_available_moves))
    
    slug_position = positions.get(slug)
    slug_available_moves = get_piece_moves(slug, slug_position)
    slug_available_moves = [row_col_to_position(row, col) for row, col in slug_available_moves]
    slug_available_moves = list(set(slug_available_moves))

    result_moves = [moves for moves in slug_available_moves if moves not in all_available_moves]

    return result_moves