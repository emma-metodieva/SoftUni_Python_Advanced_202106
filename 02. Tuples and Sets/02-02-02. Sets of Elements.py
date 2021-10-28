# 02-02. Tuples and Sets - Exercise
# 02. Sets of Elements

n, m = map(int, input().split())
a = set()
b = set()

for _ in range(n):
    a.add(int(input()))

for _ in range(m):
    b.add(int(input()))

[print(integer) for integer in a & b]
