from core import *

fibonacci_seq = []
while True:
    command, *rest = input().split()
    if command == 'Stop':
        break

    if command == 'Create' and rest[0] == 'Sequence':
        fibonacci_seq = create_fibonacci_seq(int(rest[1]))
        print(*fibonacci_seq, end=' ')
        print()
    elif command == 'Locate':
        try:
            index = locate_number(fibonacci_seq, int(rest[0]))
            print(f"The number - {rest[0]} is at index {index}")
        except ValueError:
            print(f"The number {rest[0]} is not in the sequence")
