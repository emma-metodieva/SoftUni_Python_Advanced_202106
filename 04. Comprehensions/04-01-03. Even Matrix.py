# 04-01. Comprehensions - Lab
# 03. Even Matrix

rows = int(input())

print([[int(j) for j in input().split(', ') if int(j) % 2 == 0] for i in range(rows)])
