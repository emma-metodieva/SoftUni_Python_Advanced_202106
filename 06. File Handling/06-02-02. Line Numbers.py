# 06-02. File Handling - Exercise
# 02. Line Numbers

import os
import string


def count_letters(characters):
    count = 0
    for char in characters:
        if char.isalpha():
            count += 1
    return count


def count_punctuation(characters):
    count = 0
    for char in characters:
        if char in string.punctuation:
            count += 1
    return count


current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "Exercise Files", "06-02-02", "input.txt")
output_path = os.path.join(current_dir, "Exercise Files", "06-02-02", "output.txt")

with open(input_path) as in_file:
    text = in_file.read().split('\n')

with open(output_path, "w") as file:
    for i, line in enumerate(text):
        file.write(f"Line {i+1}: {line} ({count_letters(line)}) ({count_punctuation(line)})\n")
