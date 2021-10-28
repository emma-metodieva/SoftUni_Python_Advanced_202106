# 03-01. Multidimensional Lists - Lab
# 05. Square with Maximum Sum

import sys

rows, cols = [int(el) for el in input(). split(', ')]
matrix = []
max_sum = -sys.maxsize
position = None, None

for row in range(rows):
    matrix.append([int(el) for el in input(). split(', ')])

for row in range(rows-1):
    for col in range(cols-1):
        current_sum = \
            matrix[row][col] + matrix[row][col+1] + \
            matrix[row+1][col] + matrix[row+1][col+1]
        if current_sum > max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position
print(matrix[row][col], matrix[row][col+1])
print(matrix[row+1][col], matrix[row+1][col+1])
print(max_sum)
