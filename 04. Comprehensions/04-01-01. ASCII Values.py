# 04-01. Comprehensions - Lab
# 01. ASCII Values

chars = input().split(', ')

print({char: ord(char) for char in chars})
