# 01-01. Lists as Stacks and Queues - Lab
# 01. Reverse Strings

text = list(input())
result = []

while len(text) > 0:
    result.append(text.pop())

print(f"{''.join(result)}")
