# Exam Preparation
# 20210214-02. Problem 2
# 17:27 - 17:43 = 16 min

def is_valid(matrix, row, col):
    coordinates = (row, col)
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if coordinates not in walls:
            return True
    return False


n = int(input())

field = []
position = tuple()
walls = []
for i in range(n):
    field.append(input().split())
    for j in range(n):
        if field[i][j] == "P":
            position = (i, j)
        elif field[i][j] == "X":
            walls.append((i, j))

win = False
coins = 0
path = []
while True:
    command = input()

    i, j = position
    if command == 'up':
        i -= 1
    elif command == 'down':
        i += 1
    elif command == 'left':
        j -= 1
    elif command == 'right':
        j += 1

    if is_valid(field, i, j):
        coins += int(field[i][j])
        field[i][j] = 0
        position = [i, j]
        path.append(position)
        if coins > 100:
            win = True
            break
    else:
        coins = int(coins/2)
        break

if win:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")
for p in path:
    print(p)
