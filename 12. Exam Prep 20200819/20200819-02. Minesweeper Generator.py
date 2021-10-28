# Exam Preparation
# 20200819-02. Minesweeper Generator
# 17:36 - 18:01 = 25 min

def calc_bombs_around(matrix, row, col):
    cells_around = [(row-1, col), (row-1, col+1), (row, col+1), (row+1, col+1),
                    (row+1, col), (row+1, col-1), (row, col-1), (row-1, col-1)]
    bombs_around = 0

    for cell in cells_around:
        neighbour_i, neighbour_j = cell
        if 0 <= neighbour_i < len(matrix) and 0 <= neighbour_j < len(matrix):
            if matrix[neighbour_i][neighbour_j] == '*':
                bombs_around += 1

    return bombs_around


n = int(input())

bombs = int(input())
bombs_positions = []
for b in range(bombs):
    bombs_positions.append(input())

field = []
for i in range(n):
    field.append([])
    for j in range(n):
        position = f'({i}, {j})'
        if position in bombs_positions:
            field[i].append('*')
        else:
            field[i].append(0)

for i in range(n):
    for j in range(n):
        if field[i][j] != '*':
            field[i][j] = calc_bombs_around(field, i, j)
        print(field[i][j], end=' ')
    print()
