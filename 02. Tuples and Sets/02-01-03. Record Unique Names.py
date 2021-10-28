# 02-01. Tuples and Sets - Lab
# 03. Record Unique Names

n = int(input())
names = set()

for _ in range(n):
    names.add(input())

[print(name) for name in names]
