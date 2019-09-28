def newState(x, y, b):
    s = sum(b[(x + i + len(b)) % len(b)][(y + j + len(b[0])) % len(b[0])] for i in range(-1,2) for j in range(-1,2))
    return 1 if (b[x][y] and s == 4) or s == 3 else 0

def game_of_life(board, steps):
    return board if steps == 0 else game_of_life([[newState(x, y, board) for y in range(len(board[0]))] for x in range(len(board))], steps-1)
