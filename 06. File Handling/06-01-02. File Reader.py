# 06-01. File Handling
# 02. File Reader

file = open("Lab Files/numbers.txt")

print(sum([int(line) for line in file]))
