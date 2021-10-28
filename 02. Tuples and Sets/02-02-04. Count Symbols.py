# 02-02. Tuples and Sets - Exercise
# 04. Count Symbols

text = input()
result = {}

for symbol in text:
    if symbol not in result:
        result[symbol] = 0
    result[symbol] += 1

for key, value in sorted(result.items()):
    print(f"{key}: {value} time/s")
