# Exam Preparation
# 20201216-02. Problem 2
# 15:57 - 16:18 = 21 min

def is_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


string = input()
n = int(input())

field = []
position = tuple()
for i in range(n):
    field.append(list(input()))
    for j in range(n):
        if field[i][j] == 'P':
            position = (i, j)

m = int(input())
for _ in range(m):
    move = input()

    i, j = position
    if move == 'up':
        i -= 1
    elif move == 'down':
        i += 1
    elif move == 'left':
        j -= 1
    elif move == 'right':
        j += 1

    if is_valid(field, i, j):
        symbol = str(field[i][j])
        if symbol.isalpha():
            string += symbol
        field[position[0]][position[1]] = '-'
        field[i][j] = 'P'
        position = (i, j)
    else:
        try:
            string = string[:-1]
        except IndexError:
            pass

print(string)
for i in range(n):
    for j in range(n):
        print(field[i][j], end='')
    print()
