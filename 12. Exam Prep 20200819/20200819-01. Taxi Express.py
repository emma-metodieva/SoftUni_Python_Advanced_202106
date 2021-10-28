# Exam Preparation
# 20200819-01. Taxi Preparation
# 17:27 - 17:35 = 8 min

from collections import deque

clients = deque(map(int, input().split(', ')))
taxis = deque(map(int, input().split(', ')))

time = 0
while clients and taxis:
    client = clients.popleft()
    taxi = taxis.pop()

    if client <= taxi:
        time += client
    else:
        clients.appendleft(client)

if clients:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, list(clients)))}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {time} minutes")
