# 04.02. Comprehensions - Exercise
# 02. Words Lenghts

text = input().split(', ')

print(', '.join([f"{string} -> {len(string)}" for string in text]))
