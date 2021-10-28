# 04-01. Comprehensions - Lab
# 04. Flattening Matrix

rows = int(input())

matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]

print([col for row in matrix for col in row])
