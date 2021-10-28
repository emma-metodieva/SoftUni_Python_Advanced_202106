from os import remove

data = input()
while not data == "End":

    command, *rest = data.split('-')

    if command == "Create":
        name = rest[0]
        with open(name, 'w') as file:
            pass

    elif command == "Add":
        name, line = rest
        # appending
        with open(name, 'a') as file:
           file.write(line + '\n')

    elif command == "Replace":
        name, old, new = rest
        try:
            # reading
            with open(name, 'r') as file:
                content = file.read()
            # writing
            with open(name, 'w') as file:
                content = content.replace(old, new)
                file.write(content)

        except Exception as e:
            print("An error occurred")
            data = input()  # cuz while loop
            continue

    elif command == "Delete":
        try:
            name = rest[0]
            remove(name)  # from os
        except FileNotFoundError:
            print("An error occurred!")

    data = input()
