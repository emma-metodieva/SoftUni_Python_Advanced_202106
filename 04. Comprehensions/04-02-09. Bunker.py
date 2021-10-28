# 04.02. Comprehensions - Exercise
# 09. Bunker

categories = input().split(', ')
n = int(input())

bunker = {}
for _ in range(n):
    category, item, info = input().split(' - ')
    quantity_info, quality_info = info.split(';')
    quantity = int(quantity_info.split(':')[1])
    quality = int(quality_info.split(':')[1])

    if (category, item) not in bunker:
        bunker[(category, item)] = (quantity, quality)

print(f"Count of items: {sum([value[0] for key, value in bunker.items()])}")
print(f"Average quality: {sum([value[1] for key, value in bunker.items()]) / len(categories):.02f}")

[print(f"{category} -> {', '.join([key[1] for key, value in bunker.items() if key[0] == category])}")
 for category in categories]
