# 03-02. Multidimensional Lists - Exercise
# 08. Miner

def is_valid_index(matrix, i_index, j_index):
    if 0 <= i_index < len(matrix) and 0 <= j_index < len(matrix[0]):
        return True
    else:
        return False


n = int(input())
moves = input().split()

field = []
coal = 0
start = None
for i in range(n):
    field.append(input().split())
    for j in range(n):
        if field[i][j] == 's':
            start = (i, j)
        elif field[i][j] == 'c':
            coal += 1

game_over = False
current_i, current_j = start
for move in moves:
    if move == 'up' and is_valid_index(field, current_i-1, current_j):
        current_i -= 1
        if field[current_i][current_j] == 'c':
            field[current_i][current_j] = '*'
            coal -= 1
        elif field[current_i][current_j] == 'e':
            game_over = True
            break
    elif move == 'down' and is_valid_index(field, current_i+1, current_j):
        current_i += 1
        if field[current_i][current_j] == 'c':
            field[current_i][current_j] = '*'
            coal -= 1
        elif field[current_i][current_j] == 'e':
            game_over = True
            break
    elif move == 'left' and is_valid_index(field, current_i, current_j-1):
        current_j -= 1
        if field[current_i][current_j] == 'c':
            field[current_i][current_j] = '*'
            coal -= 1
        elif field[current_i][current_j] == 'e':
            game_over = True
            break
    elif move == 'right' and is_valid_index(field, current_i, current_j+1):
        current_j += 1
        if field[current_i][current_j] == 'c':
            field[current_i][current_j] = '*'
            coal -= 1
        elif field[current_i][current_j] == 'e':
            game_over = True
            break

if game_over:
    print(f"Game over! ({current_i}, {current_j})")
elif coal == 0:
    print(f" You collected all coals! ({current_i}, {current_j})")
elif coal > 0:
    print(f"{coal} coals left. ({current_i}, {current_j})")
