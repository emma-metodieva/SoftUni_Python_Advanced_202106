import re

with open("input.txt") as file:
    file = file.read()


pattern = r"[-,.!?]"
for index, line in enumerate(file.split("\n")):
    if index % 2 == 0:
        line = re.sub(pattern, "@", line)
        line = " ".join(line.split()[::-1])
        print(line.strip())
