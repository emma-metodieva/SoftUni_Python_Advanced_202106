# 05-02. Functions Advanced - Exercise
# 05. Odd and Even

command = input()
numbers = [int(value) for value in input().split()]

mapper = {'Even': (lambda x: x % 2 == 0), 'Odd': (lambda x: x % 2 != 0)}

print(sum(filter(mapper[command], numbers)) * len(numbers))
