# 02-01. Tuples and Sets - Lab
# 01. Count Same Values

nums = tuple([float(num) for num in input().split()])
result = {}

for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1

for key, value in result.items():
    print(f"{key} - {value} times")
