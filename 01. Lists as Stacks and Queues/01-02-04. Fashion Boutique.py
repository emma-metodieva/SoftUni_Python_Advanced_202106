# 01-02. Lists as Stacks and Queues - Exercise
# 04. Fashion Boutique

from collections import deque

box = deque(map(int, input().split()))
rack_capacity = int(input())
rack_current = 0
rack_count = 1

while box:
    cloth = box.pop()
    if rack_current + cloth > rack_capacity:
        rack_count += 1
        rack_current = 0
    rack_current += cloth

print(rack_count)
