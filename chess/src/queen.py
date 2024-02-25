from .utils import *

class Queen():
    def __init__(self):
        self.name = "Queen"
        
    def get_moves(self,row,col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        valid_moves = get_valid_moves(directions,row,col)        
        return valid_moves