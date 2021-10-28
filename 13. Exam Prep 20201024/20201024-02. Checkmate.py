# Exam Preparation
# 20201024-02. Checkmate
# 21:55 - 22:24 = 29 min

def is_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def move_up(matrix, position):
    row, col = position
    row -= 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        row -= 1
    return False


def move_down(matrix, position):
    row, col = position
    row += 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        row += 1
    return False


def move_left(matrix, position):
    row, col = position
    col -= 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        col -= 1
    return False


def move_right(matrix, position):
    row, col = position
    col += 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        col += 1
    return False


def move_up_left(matrix, position):
    row, col = position
    row -= 1
    col -= 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        row -= 1
        col -= 1
    return False


def move_up_right(matrix, position):
    row, col = position
    row -= 1
    col += 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        row -= 1
        col += 1
    return False


def move_down_right(matrix, position):
    row, col = position
    row += 1
    col += 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        row += 1
        col += 1
    return False


def move_down_left(matrix, position):
    row, col = position
    row += 1
    col -= 1
    while is_valid(matrix, row, col):
        if matrix[row][col] == 'Q':
            return False
        elif matrix[row][col] == 'K':
            return True
        row += 1
        col -= 1
    return False


chess_board = []
queens = []
for i in range(8):
    chess_board.append(input().split())
    for j in range(8):
        if chess_board[i][j] == "Q":
            queens.append([i, j])

queen_capture = []
for queen in queens:
    if move_up(chess_board, queen):
        queen_capture.append(queen)
    elif move_down(chess_board, queen):
        queen_capture.append(queen)
    elif move_left(chess_board, queen):
        queen_capture.append(queen)
    elif move_right(chess_board, queen):
        queen_capture.append(queen)
    elif move_up_left(chess_board, queen):
        queen_capture.append(queen)
    elif move_up_right(chess_board, queen):
        queen_capture.append(queen)
    elif move_down_left(chess_board, queen):
        queen_capture.append(queen)
    elif move_down_right(chess_board, queen):
        queen_capture.append(queen)

if queen_capture:
    [print(capture) for capture in queen_capture]
else:
    print("The king is safe!")
