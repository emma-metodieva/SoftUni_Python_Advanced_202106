# 01-02. Lists as Stacks and Queues - Exercise
# 08. Crossroads

from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
parts = deque()
count = 0
crash = False

while True:
    command = input()
    if command == 'END':
        break

    elif command == 'green':
        for sec in range(green_light):
            if len(cars) > 0 and len(parts) == 0:
                car_on_crossroad = cars.popleft()
                parts = deque(car_on_crossroad)
            if len(parts) > 0:
                part_on_crossroad = parts.popleft()
                if len(parts) == 0:
                    count += 1
        for sec in range(free_window):
            if len(parts) > 0:
                part_on_crossroad = parts.popleft()
                if len(parts) == 0:
                    count += 1
        if len(parts) > 0:
            part_on_crossroad = parts.popleft()
            crash = True
            break

    else:
        cars.append(command)

if crash:
    print('A crash happened!')
    print(f'{car_on_crossroad} was hit at {part_on_crossroad}.')
else:
    print('Everyone is safe.')
    print(f'{count} total cars passed the crossroads.')
