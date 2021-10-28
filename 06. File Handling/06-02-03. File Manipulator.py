# 06-02. File Handling - Exercise
# 03. File Manipulator

import os


def create_file(file_name):
    try:
        os.mkdir(os.path.join(current_dir, "Exercise Files", "06-02-03"))
    except FileExistsError:
        pass
    path = os.path.join(current_dir, "Exercise Files", "06-02-03", file_name)
    with open(path, 'w'):
        pass


def add_to_file(file_name, content):
    try:
        os.mkdir(os.path.join(current_dir, "Exercise Files", "06-02-03"))
    except FileExistsError:
        pass
    path = os.path.join(current_dir, "Exercise Files", "06-02-03", file_name)
    with open(path, 'a') as file:
        file.write(f"{content}\n")


def replace_string(file_name, old_string, new_string):
    path = os.path.join(current_dir, "Exercise Files", "06-02-03", file_name)
    try:
        with open(path, 'r') as file:
            text = file.read()
        with open(path, 'w') as file:
            file.write(text.replace(old_string, new_string))
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    path = os.path.join(current_dir, "Exercise Files", "06-02-03", file_name)
    try:
        os.remove(path)
    except FileNotFoundError:
        print("An error occurred")


current_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    command, *rest = input().split('-')
    if command == 'End':
        break

    elif command == 'Create':
        # rest[0] = {file_name}
        create_file(rest[0])
    elif command == 'Add':
        # rest[0] = {file_name}; rest[1] = {content}
        add_to_file(rest[0], rest[1])
    elif command == 'Replace':
        # rest[0] = {file_name}; rest[1] = {old_string}; rest[2] = {new_string}
        replace_string(rest[0], rest[1], rest[2])
    elif command == 'Delete':
        # rest[0] = {file_name}
        delete_file(rest[0])
