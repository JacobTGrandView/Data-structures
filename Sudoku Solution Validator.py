#validate row
def RowValid(row_num):
    return len(set(sudoku[row_num])) == 9

#validate column
def ColValid(col_num):
    col = [item[col_num] for item in sudoku]
    return len(set(col)) == 9

#validate cell
def CellValid(cel_row, cel_col):
    vals = sudoku[cel_row][cel_col: cel_col+3]
    vals.extend(sudoku[cel_row+1] [cel_col: cel_col+3])
    vals.extend(sudoku[cel_row+2] [cel_col: cel_col+3])
    return len(set(vals)) == 9

#validate sudoku
def validate_solution():
    for i in range(0,9):
        if not RowValid(i):
            return False
        if not ColValid(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            print(i, j)
            if not CellValid(i, j):
                return False
    return True

sudoku = [[1, 3, 4, 6, 7, 8, 9, 1, 2],
            [3, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [1, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]
 
if validate_solution():
    print("True")
else:
    print("False")



