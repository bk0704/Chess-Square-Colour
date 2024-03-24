def getChessSquareColor(column, row):
    if not(1 <= column <= 8 and 1 <= row <= 8):
        return ''
    if (column + row) % 2 == 0:
        return 'white'
    else:
        return 'black'

assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''