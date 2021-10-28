# 05-01. Functions Advanced - Lab
# 07. Chairs

def chairs(names, count, curr_names=[]):
    if len(curr_names) == count:
        print(', '.join(curr_names))
        return

    for i in range(len(names)):
        curr_names.append(names[i])
        chairs(names[i+1:], count, curr_names)
        curr_names.pop()


people = input().split(', ')
n = int(input())

chairs(people, n)

# from itertools import combinations
#
# result = list(combinations(input().split(', '), int(input())))
#
# for x, y in result:
#     print(x, y, sep=', ')
