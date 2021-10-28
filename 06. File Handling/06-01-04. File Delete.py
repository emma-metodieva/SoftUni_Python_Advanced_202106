# 06-01. File Handling
# 04. File Delete

import os

try:
    os.remove("Lab Files/test.txt")
except FileNotFoundError:
    print("File already deleted!")
