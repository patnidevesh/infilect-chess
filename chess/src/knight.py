class Knight():
    def __init__(self):
        self.name = "Knight"

    def get_moves(self,row,col):
        valid_moves = []

        directions = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 1 <= new_row <= 8 and 1 <= new_col <= 8:
                valid_moves.append((new_row, new_col))

        return valid_moves