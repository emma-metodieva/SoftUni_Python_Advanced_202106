# 06-02. File Handling - Exercise
# 01. Even Lines

import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "Exercise Files", "06-02-01", "input.txt")

with open(input_path) as in_file:
    text = in_file.read().split('\n')

for i, line in enumerate(text):
    if i % 2 != 0:
        continue

    line = re.sub(r'[-,.!?]', '@', line)
    line = ' '.join(reversed(line.split()))

    print(line)
