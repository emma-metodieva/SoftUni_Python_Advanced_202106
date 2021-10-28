# 01-02. Lists as Stacks and Queues - Exercise
# 09. Key Revolver

from collections import deque

price = int(input())
barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence = int(input())
count = 0

while bullets and locks:
    for shot in range(1,  barrel + 1):
        if not locks or not bullets:
            break

        bullet = bullets.pop()
        lock = locks.popleft()
        count += 1

        if bullet <= lock:
            print('Bang!')
        else:
            locks.appendleft(lock)
            print('Ping!')

        if shot == barrel and bullets:
            print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - count * price}")
