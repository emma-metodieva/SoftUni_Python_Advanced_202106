# 04.02. Comprehensions - Exercise
# 05. Diagonals

n = int(input())

matrix = [list(map(int, input().split(', '))) for i in range(n)]

diagonal_1 = []
diagonal_2 = []

[[diagonal_1.append(matrix[i][j]) for j in range(n) if i == j] for i in range(n)]
[[diagonal_2.append(matrix[i][j]) for j in range(n) if i + j == n - 1]for i in range(n)]

print(f"First diagonal: {', '.join(list(map(str, diagonal_1)))}. Sum: {sum(diagonal_1)}")
print(f"Second diagonal: {', '.join(list(map(str, diagonal_2)))}. Sum: {sum(diagonal_2)}")
