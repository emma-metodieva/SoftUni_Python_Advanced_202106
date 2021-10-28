# 03-02. Multidimensional Lists - Exercise
# 01. Diagonal Difference

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(el) for el in input().split()])

primary = 0
secondary = 0
for row in range(n):
    for col in range(n):
        if row == col:
            primary += matrix[row][col]
        if (row + col) == (n - 1):
            secondary += matrix[row][col]

print(abs(primary - secondary))
