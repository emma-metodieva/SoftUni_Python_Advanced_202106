# 02-01. Tuples and Sets - Lab
# 04. Parking Lot

n = int(input())
parking = set()

for _ in range(n):
    command, car = input().split(', ')
    if command == 'IN':
        parking.add(car)
    elif command == 'OUT':
        parking.discard(car)

if parking:
    [print(car) for car in parking]
else:
    print('Parking Lot is Empty')
