# 06-01. File Handling
# 01. File Opener

try:
    open("Lab Files/text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")
