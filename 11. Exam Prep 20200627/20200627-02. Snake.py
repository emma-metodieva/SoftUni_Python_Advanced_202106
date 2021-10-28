# Exam Preparation
# 20200627-02. Snake
# 12:33 - 12:57 = 24 min

def is_valid(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


n = int(input())

field = []
burrows = []
snake = tuple()
for i in range(n):
    field.append(list(input()))
    for j in range(n):
        if field[i][j] == 'S':
            snake = (i, j)
        if field[i][j] == 'B':
            burrows.append((i, j))

game_over = False
i, j = snake
food = 0
while food < 10:
    command = input()

    if command == 'up':
        field[i][j] = '.'
        if is_valid(i-1, j):
            i = i-1
            if field[i][j] == '*':
                food += 1
            elif field[i][j] == 'B':
                burrows.remove((i, j))
                field[i][j] = '.'
                i, j = burrows[0]
            field[i][j] = 'S'
        else:
            game_over = True
            break

    if command == 'down':
        field[i][j] = '.'
        if is_valid(i+1, j):
            i = i+1
            if field[i][j] == '*':
                food += 1
            elif field[i][j] == 'B':
                burrows.remove((i, j))
                field[i][j] = '.'
                i, j = burrows[0]
            field[i][j] = 'S'
        else:
            game_over = True
            break

    if command == 'left':
        field[i][j] = '.'
        if is_valid(i, j-1):
            j = j-1
            if field[i][j] == '*':
                food += 1
            elif field[i][j] == 'B':
                burrows.remove((i, j))
                field[i][j] = '.'
                i, j = burrows[0]
            field[i][j] = 'S'
        else:
            game_over = True
            break

    if command == 'right':
        field[i][j] = '.'
        if is_valid(i, j+1):
            j = j+1
            if field[i][j] == '*':
                food += 1
            elif field[i][j] == 'B':
                burrows.remove((i, j))
                field[i][j] = '.'
                i, j = burrows[0]
            field[i][j] = 'S'
        else:
            game_over = True
            break

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")

for i in range(n):
    for j in range(n):
        print(field[i][j], end='')
    print()
