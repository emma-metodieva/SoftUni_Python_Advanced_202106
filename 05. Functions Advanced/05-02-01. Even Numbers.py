# 05-02. Functions Advanced - Exercise
# 01. Even Numbers

def even_numbers(x):
    if x % 2 == 0:
        return True
    else:
        return False


numbers = map(int, input().split())
print(list(filter(even_numbers, numbers)))
