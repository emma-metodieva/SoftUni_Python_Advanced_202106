# 01-02. Lists as Stacks and Queues - Exercise
# 05. Truck Tour

from collections import deque

n = int(input())
start_index = 0
petrol = []
distance = []

for pumps in range(n):
    data = input().split()
    petrol.append(int(data[0]))
    distance.append(int(data[1]))

while True:
    successful = True

    petrol_try = deque(petrol)
    distance_try = deque(distance)
    tank = 0

    petrol_try.rotate(-start_index)
    distance_try.rotate(-start_index)

    for i in range(n):
        tank += petrol_try.popleft()
        distance_to_next = distance_try.popleft()

        if tank >= distance_to_next:
            tank -= distance_to_next
            continue
        else:
            successful = False
            start_index += 1
            break

    if successful:
        print(start_index)
        break
