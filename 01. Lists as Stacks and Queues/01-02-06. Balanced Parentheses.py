# 01-02. Lists as Stacks and Queues - Exercise
# 06. Balanced Parentheses

from collections import deque

parentheses = deque(input())
opening_parentheses = deque()
opening_allowed = ['(', '{', '[']
closing_allowed = [')', '}', ']']
balanced = True

while parentheses:
    current = parentheses.popleft()
    if current in opening_allowed:
        opening_parentheses.append(current)
    elif len(opening_parentheses) > 0:
        opening_index = opening_allowed.index(opening_parentheses.pop())
        closing_index = closing_allowed.index(current)
        if opening_index != closing_index:
            balanced = False
            break
    else:
        balanced = False
        break

if balanced:
    print("YES")
else:
    print("NO")
