import re

letters_pattern = r"[A-Za-z]"
punctuations_pattern = r"[.?\-,!']"

with open("input.txt") as file:
    file = file.read()

with open("output.txt", "w") as result:
    for index, line in enumerate(file.split("\n")):
        letters = re.findall(letters_pattern, line)
        punctuations = re.findall(punctuations_pattern, line)
        result.write(f"Line {index + 1}: {line} ({len(letters)})({len(punctuations)})\n")
