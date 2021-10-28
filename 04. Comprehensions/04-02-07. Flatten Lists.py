# 04.02. Comprehensions - Exercise
# 07. Flatten Lists

items = [item.split() for item in input().split('|')]

items_flat = [val for item in items[::-1]for val in item]

print(' '.join(items_flat))
