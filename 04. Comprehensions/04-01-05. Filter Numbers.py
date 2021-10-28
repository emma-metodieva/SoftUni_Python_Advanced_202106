# 04-01. Comprehensions - Lab
# 05. Filter Numbers

def is_divisible(number):
    division = [d for d in range(2, 10 + 1) if number % d == 0]
    return True if division else False


start = int(input())
end = int(input())

print([num for num in range(start, end +1) if is_divisible(num)])
