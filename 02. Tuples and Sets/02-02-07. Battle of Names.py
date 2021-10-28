# 02-02. Tuples and Sets - Exercise
# 07. Battle of Names

n = int(input())
odd = set()
even = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = 0
    for symbol in name:
        ascii_sum += ord(symbol)
    result = int(ascii_sum / row)
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

odd_sum = sum(odd)
even_sum = sum(even)

if odd_sum == even_sum:
    output = [str(int(el)) for el in (odd | even)]
elif odd_sum > even_sum:
    output = [str(int(el))  for el in (odd - even)]
else:
    output = [str(int(el))  for el in (odd ^ even)]

print(', '.join(output))
