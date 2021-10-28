# 02-02. Tuples and Sets - Exercise
# 05. Phonebook

n = 0
phonebook = {}

while True:
    command = input().split('-')
    if command[0].isdigit():
        n = int(command[0])
        break

    name = command[0]
    phone_number = command[1]

    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = phone_number

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f"Contact {name} does not exist.")
