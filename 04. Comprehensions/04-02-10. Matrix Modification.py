# 04.02. Comprehensions - Exercise
# 10. Matrix Modification

def add(source, i, j, value):
    i = int(i)
    j = int(j)
    if 0 <= i < len(source) and 0 <= j < len(source):
        source[i][j] += int(value)
    else:
        print("Invalid coordinates")


def subtract(source, i, j, value):
    i = int(i)
    j = int(j)
    if 0 <= i < len(source) and 0 <= j < len(source):
        source[i][j] -= int(value)
    else:
        print("Invalid coordinates")


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

while True:
    command = input().split()
    if command[0] == 'END':
        break

    if command[0] == 'Add':
        add(matrix, command[1], command[2], command[3])
    elif command[0] == 'Subtract':
        subtract(matrix, command[1], command[2], command[3])

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

