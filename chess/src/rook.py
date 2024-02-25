from .utils import *

class Rook():
    def __init__(self):
        self.name = "Rook"

    def get_moves(self,row,col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        valid_moves = get_valid_moves(directions,row,col)
        return valid_moves