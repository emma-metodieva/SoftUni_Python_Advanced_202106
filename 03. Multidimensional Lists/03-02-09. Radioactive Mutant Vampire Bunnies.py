# 03-02. Multidimensional Lists - Exercise
# 09. Radioactive Mutant Vampire Bunnies

def is_valid_index(matrix, i_index, j_index):
    if 0 <= i_index < len(matrix) and 0 <= j_index < len(matrix[0]):
        return True
    else:
        return False


n, m = map(int, input().split())

lair = []
bunnies = set()
player = tuple()
for i in range(n):
    lair.append(list(input()))
    for j in range(m):
        if lair[i][j] == 'B':
            bunnies.add((i, j))
        elif lair[i][j] == 'P':
            player = (i, j)

moves = list(input())

status = None
for move in moves:
    if status == 'won' or status == 'dead':
        break

    # PLAYER
    player_i, player_j = player
    if move == 'U':
        if is_valid_index(lair, player_i - 1, player_j):
            lair[player_i][player_j] = '.'
            if lair[player_i - 1][player_j] == 'B':
                status = 'dead'
            else:
                lair[player_i - 1][player_j] = 'P'
            player = (player_i - 1, player_j)
        else:
            lair[player_i][player_j] = '.'
            status = 'won'
    elif move == 'D':
        if is_valid_index(lair, player_i + 1, player_j):
            lair[player_i][player_j] = '.'
            if lair[player_i + 1][player_j] == 'B':
                status = 'dead'
            else:
                lair[player_i + 1][player_j] = 'P'
            player = (player_i + 1, player_j)
        else:
            lair[player_i][player_j] = '.'
            status = 'won'
    elif move == 'L':
        if is_valid_index(lair, player_i, player_j - 1):
            lair[player_i][player_j] = '.'
            if lair[player_i][player_j - 1] == 'B':
                status = 'dead'
            else:
                lair[player_i][player_j - 1] = 'P'
            player = (player_i, player_j - 1)
        else:
            lair[player_i][player_j] = '.'
            status = 'won'
    elif move == 'R':
        if is_valid_index(lair, player_i, player_j + 1):
            lair[player_i][player_j] = '.'
            if lair[player_i][player_j + 1] == 'B':
                status = 'dead'
            else:
                lair[player_i][player_j + 1] = 'P'
            player = (player_i, player_j + 1)
        else:
            lair[player_i][player_j] = '.'
            status = 'won'

    # BUNNIES
    new_bunnies = set()
    for bunny in bunnies:
        bunny_i, bunny_j = bunny
        if is_valid_index(lair, bunny_i - 1, bunny_j):
            if lair[bunny_i - 1][bunny_j] == 'P':
                status = 'dead'
            lair[bunny_i - 1][bunny_j] = 'B'
            new_bunnies.add((bunny_i - 1, bunny_j))
        if is_valid_index(lair, bunny_i, bunny_j + 1):
            if lair[bunny_i][bunny_j + 1] == 'P':
                status = 'dead'
            lair[bunny_i][bunny_j + 1] = 'B'
            new_bunnies.add((bunny_i, bunny_j + 1))
        if is_valid_index(lair, bunny_i + 1, bunny_j):
            if lair[bunny_i + 1][bunny_j] == 'P':
                status = 'dead'
            lair[bunny_i + 1][bunny_j] = 'B'
            new_bunnies.add((bunny_i + 1, bunny_j))
        if is_valid_index(lair, bunny_i, bunny_j - 1):
            if lair[bunny_i][bunny_j - 1] == 'P':
                status = 'dead'
            lair[bunny_i][bunny_j - 1] = 'B'
            new_bunnies.add((bunny_i, bunny_j - 1))
    bunnies = bunnies.union(new_bunnies)

for i in range(n):
    for j in range(m):
        print(lair[i][j], end='')
    print()

player_i, player_j = player
print(f'{status}: {player_i} {player_j}')
