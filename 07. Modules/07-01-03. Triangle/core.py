def print_1st_half(n):
    for r in range(1, n+1):
        for c in range(1, r+1):
            print(c, end=' ')
        print()


def print_2nd_half(n):
    for r in range(n-1, 0, -1):
        for c in range(1, r+1):
            print(c, end=' ')
        print()


def print_triangle(n):
    print_1st_half(n)
    print_2nd_half(n)


