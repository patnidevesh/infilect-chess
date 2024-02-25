
def get_valid_moves(directions,row,col):
    valid_moves = []
    for drow, dcol in directions:
        for step in range(1,9):
            new_row, new_col = row + step * drow, col + step * dcol
            if not (1 <= new_row <= 8 and 1 <= new_col <= 8):
                break

            valid_moves.append((new_row, new_col))
    return valid_moves

def position_to_row_col(position):
    col_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    row = int(position[1])
    col = col_map[position[0].upper()]
    return row, col

def row_col_to_position(row,col):
    col_map = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    new_col = col_map[col]
    new_row = str(row)
    return new_col + new_row