# 01-02. Lists as Stacks and Queues - Exercise
# 10. Cups and Bottles

from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        wasted += max(bottle - cup, 0)
        cup = max(cup - bottle, 0)

if cups:
    print(f"Cups: {' '.join(list(map(str, cups)))}")
else:
    bottles.reverse()
    print(f"Bottles: {' '.join(list(map(str, bottles)))}")

print(f'Wasted litters of water: {wasted}')
