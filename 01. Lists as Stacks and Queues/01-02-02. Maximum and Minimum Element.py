# 01-02. Lists as Stacks and Queues - Exercise
# 02. Maximum and Minimum Element

n = int(input())
stack = []

for n in range(n):
    query = input().split()
    if query[0] == '1':
        stack.append(int(query[1]))
    elif len(stack) > 0:
        if query[0] == '2':
            stack.pop()
        elif query[0] == '3':
            print(max(stack))
        elif query[0] == '4':
            print(min(stack))

stack.reverse()
print(f"{', '.join(list(map(str, stack)))}")
