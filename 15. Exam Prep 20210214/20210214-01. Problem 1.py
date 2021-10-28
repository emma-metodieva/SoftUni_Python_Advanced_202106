# Exam Preparation
# 20210214-01. Problem 1
# 16:54 - 17:17 = 23 min

from collections import deque

firework_effect = deque(map(int, input().split(', ')))
explosive_power = deque(map(int, input().split(', ')))

palm_firework = 0
willow_firework = 0
crossette_firework = 0

prepared = False
while firework_effect and explosive_power:
    effect = firework_effect[0]
    power = explosive_power[-1]

    if effect <= 0:
        firework_effect.popleft()
        continue
    if power <= 0:
        explosive_power.pop()
        continue

    firework_sum = effect + power

    if firework_sum % 3 == 0 and firework_sum % 5 != 0:
        palm_firework += 1
        firework_effect.popleft()
        explosive_power.pop()
    elif firework_sum % 5 == 0 and firework_sum % 3 != 0:
        willow_firework += 1
        firework_effect.popleft()
        explosive_power.pop()
    elif firework_sum % 3 == 0 and firework_sum % 5 == 0:
        crossette_firework += 1
        firework_effect.popleft()
        explosive_power.pop()
    else:
        firework_effect.popleft()
        firework_effect.append(effect - 1)

    if min(palm_firework, willow_firework, crossette_firework) == 3:
        prepared = True
        break

if prepared:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join([str(value) for value in firework_effect])}")

if explosive_power:
    print(f"Explosive Power left: {', '.join([str(value) for value in explosive_power])}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
