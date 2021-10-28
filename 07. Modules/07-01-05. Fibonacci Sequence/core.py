def create_fibonacci_seq(n):
    fibonacci_seq = []
    for i in range(n):
        if i == 0:
            fibonacci_seq.append(0)
        elif i == 1:
            fibonacci_seq.append(1)
        else:
            fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq


def locate_number(sequence, n):
    return sequence.index(n)
