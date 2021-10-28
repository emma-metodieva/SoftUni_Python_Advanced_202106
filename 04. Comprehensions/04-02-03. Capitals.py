# 04.02. Comprehensions - Exercise
# 03. Capitals

countries = input().split(', ')
capitals = input().split(', ')

[print(f"{country} -> {capital}") for country, capital in zip(countries, capitals)]
