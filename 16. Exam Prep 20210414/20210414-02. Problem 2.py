# Exam Preparation
# 20210414-02. Problem 2
# 19:59 -20:38 = 39 min

def is_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


player_1, player_2 = input().split(', ')
score_1, score_2 = 501, 501
throws_1, throws_2 = 0, 0

size = 7
dartboard = []
for i in range(size):
    dartboard.append(input().split())

turn = 0
winner = None
while True:
    turn += 1
    coordinate = input()[1:-1]
    i, j = [int(value) for value in coordinate.split(', ')]

    points = 0
    if is_valid(dartboard, i, j):
        section = str(dartboard[i][j])
        if section.isnumeric():
            points = int(section)
        elif section == 'D':
            points = (int(dartboard[i][0]) + int(dartboard[i][-1]) + int(dartboard[0][j]) + int(dartboard[-1][j])) * 2
        elif section == 'T':
            points = (int(dartboard[i][0]) + int(dartboard[i][-1]) + int(dartboard[0][j]) + int(dartboard[-1][j])) * 3
        elif section == 'B':
            points = 501

    if turn % 2 != 0:
        throws_1 += 1
        score_1 -= points
        if score_1 <= 0:
            winner = player_1
            break
    else:
        throws_2 += 1
        score_2 -= points
        if score_2 <= 0:
            winner = player_2
            break

if winner == player_1:
    print(f"{player_1} won the game with {throws_1} throws!")
elif winner == player_2:
    print(f"{player_2} won the game with {throws_2} throws!")
