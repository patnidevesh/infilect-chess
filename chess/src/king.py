from .utils import *

class King():
    def __init__(self):
        self.name = "King"

    def get_moves(self,row,col):        
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),  # Horizontal and vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
        ]
        for drow, dcol in directions:
            new_row, new_col = row + drow, col + dcol
            if 1 <= new_row <= 8 and 1 <= new_col <= 8:
                valid_moves.append((new_row, new_col))
        return valid_moves