# 05-02. Functions Advanced - Exercise
# 08. Even or Odd

def even_odd(*args):
    mapper = {'even': (lambda x: x % 2 == 0), 'odd': (lambda x: x % 2 != 0)}
    return list(filter(mapper[args[-1]], args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
