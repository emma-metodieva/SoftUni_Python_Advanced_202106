# 03-02. Multidimensional Lists - Exercise
# 04. Matrix Shuffling

rows, cols = map(int, input().split())
matrix = []

for row in range(rows):
    matrix.append(input().split())

while True:
    command = input().split()
    if command[0] == 'END':
        break

    is_valid = False
    if len(command) == 5 and command[0] == 'swap':
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])
        if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
            is_valid = True
            el1 = matrix[row1][col1]
            el2 = matrix[row2][col2]
            matrix[row1][col1] = el2
            matrix[row2][col2] = el1
            for row in range(rows):
                for col in range(cols):
                    print(matrix[row][col], end=' ')
                print()

    if not is_valid:
        print('Invalid input!')
