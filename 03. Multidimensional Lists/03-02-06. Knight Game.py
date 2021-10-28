# 03-02. Multidimensional Lists - Exercise
# 06. Knight Game

def is_valid_index(matrix, i_index, j_index):
    if 0 <= i_index < len(matrix) and 0 <= j_index < len(matrix[0]):
        return True
    else:
        return False


n = int(input())
chess_board = []

for _ in range(n):
    chess_board.append(list(input()))

removed = 0
while True:
    max_attack = 0
    max_attack_i = None
    max_attack_j = None
    for i in range(n):
        for j in range(n):
            attack = 0
            if chess_board[i][j] == 'K':
                if is_valid_index(chess_board, i-2, j-1) and chess_board[i-2][j-1] == 'K':  # move 1
                    attack += 1
                if is_valid_index(chess_board, i-2, j+1) and chess_board[i-2][j+1] == 'K':  # move 2
                    attack += 1
                if is_valid_index(chess_board, i-1, j-2) and chess_board[i-1][j-2] == 'K':  # move 3
                    attack += 1
                if is_valid_index(chess_board, i-1, j+2) and chess_board[i-1][j+2] == 'K':  # move 4
                    attack += 1
                if is_valid_index(chess_board, i+1, j-2) and chess_board[i+1][j-2] == 'K':  # move 5
                    attack += 1
                if is_valid_index(chess_board, i+1, j+2) and chess_board[i+1][j+2] == 'K':  # move 6
                    attack += 1
                if is_valid_index(chess_board, i+2, j-1) and chess_board[i+2][j-1] == 'K':  # move 7
                    attack += 1
                if is_valid_index(chess_board, i+2, j+1) and chess_board[i+2][j+1] == 'K':  # move 8
                    attack += 1
            if attack > 0 and attack > max_attack:
                max_attack = attack
                max_attack_i = i
                max_attack_j = j
    if max_attack > 0:
        removed += 1
        chess_board[max_attack_i][max_attack_j] = '0'
    else:
        break

print(removed)
