# Exam Preparation
# 20201024-01. Scheduling
# 17:30 - 17:55 = 25 min

from collections import deque

jobs = map(int, input().split(', '))
jobs_indices = deque(sorted((v, i) for i, v in enumerate(jobs)))

idx = int(input())

clock_cycles = 0

for job in range(len(jobs_indices)):
    value, index = jobs_indices.popleft()
    clock_cycles += value
    if index == idx:
        print(clock_cycles)
        break
