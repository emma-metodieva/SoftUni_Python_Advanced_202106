# Exam Preparation
# 20201024-03. List Pureness
# 22:24 -22:42 - 18 min

import sys

from collections import deque


def best_list_pureness(numbers, k):
    best_pureness = -sys.maxsize
    rotations = 0

    for i in range(k+1):
        numbers_d = deque(numbers)
        numbers_d.rotate(i)
        pureness = 0
        for idx, number in enumerate(numbers_d):
            pureness += number * idx
            if pureness > best_pureness:
                best_pureness = pureness
                rotations = i

    return f"Best pureness {best_pureness} after {rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
