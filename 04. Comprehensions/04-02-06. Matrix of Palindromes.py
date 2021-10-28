# 04.02. Comprehensions - Exercise
# 06. Matrix of Palindromes

def palindrome(char, row, col):
    return chr(ord(char) + row) + chr(ord(char) + row + col) + chr(ord(char) + row)


rows, cols = map(int, input().split())

matrix = [[palindrome('a', i, j) for j in range(cols)] for i in range(rows)]

[print(' '.join(matrix[i])) for i in range(rows)]
