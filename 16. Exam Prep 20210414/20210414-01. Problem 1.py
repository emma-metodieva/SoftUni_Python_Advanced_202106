# Exam Preparation
# 20210414-01. Problem 1
# 19:46 - 19:59 = 13 min

from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees_capacity = deque(map(int, input().split(', ')))

pizzas = 0
while pizza_orders and employees_capacity:
    order = pizza_orders[0]
    capacity = employees_capacity[-1]

    if order <= 0 or order > 10:
        pizza_orders.popleft()
        continue

    if order <= capacity:
        pizza_orders.popleft()
        employees_capacity.pop()
        pizzas += order
    else:
        pizza_orders.popleft()
        employees_capacity.pop()
        pizzas += capacity
        order -= capacity
        pizza_orders.appendleft(order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas}")
    print(f"Employees: {', '.join([str(value) for value in employees_capacity])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(value) for value in pizza_orders])}")
