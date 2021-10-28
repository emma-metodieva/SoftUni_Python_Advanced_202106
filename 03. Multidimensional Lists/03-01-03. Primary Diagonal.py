# 03-01. Multidimensional Lists - Lab
# 03. Primary Diagonal

n = int(input())
matrix = []
diagonal = 0

for i in range(n):
    matrix.append([int(el) for el in input().split()])
    diagonal += matrix[i][i]

print(diagonal)
