from pprint import pprint

def find_next_empty(puzzle):

    # encuentra el siguiente casillero vacío  
    # por cada r (row) vamos a ver las c (columns). Si el valor es -1 significa que el casillero está vacío
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    # en caso de que ya no exista casillero vacío
    return None, None


def is_valid(puzzle, guess, row, col):
    
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True
    

def solve_sudoku(puzzle):
    # solve sudouke using backtracking
    
    # paso 1: situarnos en un casillero vacío
    row, col = find_next_empty(puzzle)

    # row is None significaría que el juego está completo (True)
    if row is None:
        return True

    # paso 2: en el casillero vamos a elegir un dígito 1-9
    for guess in range(1, 10): # range(1,10) is 1, 2, 3, ..., 9
        # paso 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess # completamos el casillero con el dígito

            if solve_sudoku(puzzle):
                return True
    
        puzzle[row][col] = -1

    return False



if __name__ == '__main__':
    example_board = [
        [ 3, 9,-1,  -1, 5,-1,  -1,-1,-1],
        [-1,-1,-1,   2,-1,-1,  -1,-1, 5],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],

        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],

        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,-1],
    ]

    print(solve_sudoku(example_board))
    pprint(example_board)
