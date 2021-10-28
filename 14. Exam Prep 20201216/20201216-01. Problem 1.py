# Exam Preparation
# 20201216-01. Problem 1
# 16:38

from collections import deque

males = deque(map(int, input().split()))
females = deque(map(int, input().split()))

matches = 0
while males and females:
    m = males[-1]
    f = females[0]

    if m <= 0:
        males.pop()
    elif f <= 0:
        females.popleft()
    elif m % 25 == 0:
        for _ in range(2):
            males.pop()
    elif f % 25 == 0:
        for _ in range(2):
            females.popleft()
    elif m == f:
        matches += 1
        males.pop()
        females.popleft()
    else:
        males[-1] -= 2
        females.popleft()

print(f"Matches: {matches}")

print("Males left:", end=' ')
if males:
    print(*reversed(males), sep=', ')
else:
    print("none")

print("Females left:", end=' ')
if females:
    print(*females, sep=', ')
else:
    print("none")
