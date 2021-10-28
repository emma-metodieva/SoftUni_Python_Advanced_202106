# Exam Preparation
# 20200627-03. List Manipulator
# 12:58 - 13:14 = 16 min

from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    command_1, command_2, *rest = args

    if command_1 == 'add':
        if command_2 == 'beginning':
            numbers.extendleft(reversed(rest))
        elif command_2 == 'end':
            numbers.extend(rest)

    if command_1 == 'remove':
        if command_2 == 'beginning':
            n = 1
            if rest:
                n = rest[0]
            for _ in range(n):
                numbers.popleft()
        if command_2 == 'end':
            n = 1
            if rest:
                n = rest[0]
            for _ in range(n):
                numbers.pop()

    return list(numbers)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
