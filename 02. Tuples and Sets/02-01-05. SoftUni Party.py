# 02-01. Tuples and Sets - Lab
# 05. SoftUni Party

n = int(input())
regular = set()
vip = set()

for _ in range(n):
    reservation = input()
    if reservation[0].isdigit():
        vip.add(reservation)
    else:
        regular.add(reservation)

while True:
    guest = input()
    if guest == 'END':
        break

    if guest[0].isdigit():
        vip.discard(guest)
    else:
        regular.discard(guest)

print(len(vip) + len(regular))
[print(v) for v in sorted(vip)]
[print(r) for r in sorted(regular)]
