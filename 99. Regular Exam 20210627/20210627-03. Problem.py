# Regular Exam
# 20210627-03. Problem

def math_operations(*args, **kwargs):
    seq = 0
    for a in args:
        seq += 1
        if seq == 5:
            seq = 1

        if seq == 1:
            kwargs['a'] += a
        elif seq == 2:
            kwargs['s'] -= a
        elif seq == 3:
            try:
                kwargs['d'] /= a
            except ZeroDivisionError:
                continue
        elif seq == 4:
            kwargs['m'] *= a

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))

