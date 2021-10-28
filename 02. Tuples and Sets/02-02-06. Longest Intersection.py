# 02-02. Tuples and Sets - Exercise
# 06. Longest Intersection

import sys

n = int(input())
intersection = set()
max_intersection_len = -sys.maxsize

for _ in range(n):
    range_1, range_2 = input().split('-')
    set_1_start, set_1_end = map(int, range_1.split(','))
    set_2_start, set_2_end = map(int, range_2.split(','))

    set_1 = set()
    for num in range(set_1_start, set_1_end + 1):
        set_1.add(num)

    set_2 = set()
    for num in range(set_2_start, set_2_end + 1):
        set_2.add(num)

    if len(set_1 & set_2) > max_intersection_len:
        intersection = set_1 & set_2
        max_intersection_len = len(set_1 & set_2)

print(f"Longest intersection is {list(intersection)} with length {max_intersection_len}")
