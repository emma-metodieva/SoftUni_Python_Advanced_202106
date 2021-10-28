# 03-01. Multidimensional Lists - Lab
# 01. Sum Matrix Elements

matrix = []
rows, cols = [int(el) for el in input(). split(', ')]
result = 0

for row in range(rows):
    matrix.append([int(el) for el in input(). split(', ')])
    result += sum(matrix[row])

print(result)
print(matrix)
