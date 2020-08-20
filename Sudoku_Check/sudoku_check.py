sudoku = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""

board = [[" " for k in range(9)] for i in range(9)]
sudoku_rows = sudoku.splitlines()
temp = []

for k in range(len(sudoku_rows)):
    for i in range(len(sudoku_rows[k])):
        board[k][i] = sudoku_rows[k][i]

low, high, rngLow, rngHigh = 0, 3, 0, 3

def test_squares(low, high, rngLow, rngHigh):
    temp = []
    for row in range(low, high):
        for colum in range(rngLow, rngHigh):
            temp.append(board[row][colum])
    temp = ''.join(temp)
    for i in range(1, 10):
        if temp.count(str(i)) != 1: return False

    low += 3
    high += 3
    if high < 10:
        test_squares(low, high, rngLow, rngHigh)
    else:
        rngLow += 3
        rngHigh += 3
        if rngHigh < 10:
            test_squares(low=0, high=3, rngLow=rngLow, rngHigh=rngHigh)

    for i in range(1, 10):
        if sudoku.count(str(i)) != 9: return False    

    for row in sudoku_rows:
        for i in range(1, 10):
            if row.count(str(i)) != 1: return False
    
    return True

print(test_squares(low, high, rngLow, rngHigh))

