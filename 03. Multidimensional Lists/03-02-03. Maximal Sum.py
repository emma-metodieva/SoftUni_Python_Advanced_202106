# 03-02. Multidimensional Lists - Exercise
# 03. Maximal Sum

import sys

rows, cols = map(int, input(). split())
matrix = []
max_sum = -sys.maxsize
position = None, None

for row in range(rows):
    matrix.append([int(el) for el in input(). split()])

for row in range(rows-2):
    for col in range(cols-2):
        current_sum = \
            matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + \
            matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + \
            matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if current_sum > max_sum:
            max_sum = current_sum
            position = (row, col)

print(f"Sum = {max_sum}")
row, col = position
print(matrix[row][col], matrix[row][col+1], matrix[row][col+2])
print(matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2])
print(matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2])
