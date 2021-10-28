# 02-02. Tuples and Sets - Exercise
# 03. Periodic Table

n = int(input())
chemical_elements = set()

for _ in range(n):
    chemical_elements.update(input().split())

[print(chemical_element) for chemical_element in chemical_elements]
