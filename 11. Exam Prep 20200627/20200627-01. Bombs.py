# Exam Preparation
# 20200627-01. Bombs
# 11:37 - 12:29 = 52 min

from collections import deque

bombs = {
    'Cherry Bombs': {'materials': 60, 'count': 0},
    'Datura Bombs': {'materials': 40, 'count': 0},
    'Smoke Decoy Bombs': {'materials': 120, 'count': 0}
}
materials = [data['materials'] for data in bombs.values()]
count = [data['count'] for data in bombs.values()]

bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = deque(map(int,  input().split(', ')))

full = False
while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()
    bomb = bomb_effect + bomb_casing
    if bomb in materials:
        idx = materials.index(bomb)
        bomb_type = list(bombs.keys())[idx]
        bombs[bomb_type]['count'] += 1
    else:
        bomb_effects.appendleft(bomb_effect)
        bomb_casings.append(bomb_casing - 5)

    if min([data['count'] for data in bombs.values()]) == 3:
        full = True
        break

if full:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print("Bomb Effects:", end=' ')
if bomb_effects:
    print(*list(bomb_effects), sep=', ')
else:
    print('empty')

print("Bomb Casings:", end=' ')
if bomb_casings:
    print(*list(bomb_casings), sep=', ')
else:
    print('empty')

for key, value in bombs.items():
    print(f"{key}: {value['count']}")
