# Regular Exam
# 20210627-01. Problem

from collections import deque

chocolates = deque(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))

milkshakes = 0
while chocolates and cups_of_milk:
    chocolate = chocolates[-1]
    cup_of_milk = cups_of_milk[0]

    if chocolate <= 0 and cup_of_milk <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    elif chocolate <= 0:
        chocolates.pop()
        continue
    elif cup_of_milk <= 0:
        cups_of_milk.popleft()
        continue

    elif chocolate == cup_of_milk:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        cups_of_milk.popleft()
        cups_of_milk.append(cup_of_milk)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print("Chocolate:", end=' ')
if chocolates:
    print(', '.join([str(value) for value in chocolates]))
else:
    print("empty")

print("Milk:", end=' ')
if cups_of_milk:
    print(', '.join([str(value) for value in cups_of_milk]))
else:
    print("empty")
