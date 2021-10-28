# 04.02. Comprehensions - Exercise
# 01. Word Filter

def even_length(string):
    length = len(string)
    return True if length % 2 == 0 else False


words = input().split()

[print(word) for word in words if even_length(word)]
