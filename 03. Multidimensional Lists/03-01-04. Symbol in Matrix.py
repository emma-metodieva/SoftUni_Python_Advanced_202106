# 03-01. Multidimensional Lists - Lab
# 04. Symbol in Matrix

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

symbol = input()
coordinates = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            coordinates = (row, col)
            break
    if coordinates:
        break

if coordinates:
    print(coordinates)
else:
    print(f"{symbol} does not occur in the matrix")
