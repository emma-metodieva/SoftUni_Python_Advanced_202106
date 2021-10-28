# 04.02. Comprehensions - Exercise
# 04. Number Classification

numbers = list(map(int, input().split(', ')))

positive = []
negative = []
[positive.append(str(num)) if num >= 0 else negative.append(str(num)) for num in numbers]

even = []
odd = []
[even.append(str(num)) if num % 2 == 0 else odd.append(str(num)) for num in numbers]

print(f"Positive:", end=' ')
print(', '.join(positive))

print(f"Negative:", end=' ')
print(', '.join(negative))

print(f"Even:", end=' ')
print(', '.join(even))

print(f"Odd:", end=' ')
print(', '.join(odd))
