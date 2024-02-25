from .utils import *

class Bishop():
    def __init__(self):
        self.name = "Bishop"

    def get_moves(self,row,col):        
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        valid_moves = get_valid_moves(directions,row,col)
        return valid_moves