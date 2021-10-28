# 04.02. Comprehensions - Exercise
# 08. Heroes Inventory

heroes = {name: {} for name in input().split(', ')}

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    hero = command[0]
    item = command[1]
    cost = int(command[2])

    if item not in heroes[hero]:
        heroes[hero].update({item: cost})

[print(f"{hero} -> Items: {len(items)}, Cost: {sum(items.values())}") for hero, items in heroes.items()]
