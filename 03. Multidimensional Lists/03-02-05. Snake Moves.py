# 03-02. Multidimensional Lists - Exercise
# 05. Snake Moves

from collections import deque

rows, cols = map(int, input().split())
matrix = []
string = input()
queue = deque()

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        if not queue:
            queue = deque(string)
        matrix[row].append(queue.popleft())
    if not row % 2 == 0:
        matrix[row] = matrix[row][::-1]

for row in range(rows):
    print(''.join(matrix[row]))
