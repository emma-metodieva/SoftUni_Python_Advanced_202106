# 01-02. Lists as Stacks and Queues - Exercise
# 01. Reverse Numbers with a Stack

# from collections import deque
#
# integers = deque(input().split())
# result = []
#
# while len(integers) > 0:
#     result.append(integers.pop())
#
# print(f"{' '.join(result)}")

##########

from collections import deque

integers = deque(input().split())

integers.reverse()

print(f"{' '.join(integers)}")
