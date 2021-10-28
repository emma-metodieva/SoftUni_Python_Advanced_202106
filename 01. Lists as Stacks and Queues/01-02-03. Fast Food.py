# 01-02. Lists as Stacks and Queues - Exercise
# 03. Fast Food

from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    order = orders.popleft()
    if order <= food_quantity:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break

if orders:
    print(f"Orders left: {' '.join(list(map(str, orders)))}")
else:
    print("Orders complete")
