# 01-01. Lists as Stacks and Queues - Lab
# 04. Water Dispenser

from collections import deque

quantity = int(input())
queue = deque()

while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)

while True:
    command = input()
    if command == 'End':
        break
    elif 'refill' in command:
        quantity += int(command.split()[-1])
    else:
        liters = int(command)
        if liters > quantity:
            print(f"{queue.popleft()} must wait")
        else:
            quantity -= liters
            print(f"{queue.popleft()} got water")

print(f"{quantity} liters left")