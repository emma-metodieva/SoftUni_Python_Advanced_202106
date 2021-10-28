# Regular Exam
# 20210627-02. Problem

def is_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


shotgun_range = []
size = 5
position = tuple
targets_left = 0
targets_hit = []
for i in range(size):
    shotgun_range.append(input().split())
    for j in range(size):
        if shotgun_range[i][j] == 'A':
            position = (i, j)
        elif shotgun_range[i][j] == 'x':
            targets_left += 1

n = int(input())
for _ in range(n):
    action, direction, *steps = input().split()
    i, j = position

    if action == 'move':
        i_new, j_new = None, None
        steps = int(steps[0])
        if direction == 'right':
            i_new = i
            j_new = j + steps
        elif direction == 'left':
            i_new = i
            j_new = j - steps
        elif direction == 'up':
            i_new = i - steps
            j_new = j
        elif direction == 'down':
            i_new = i + steps
            j_new = j

        if is_valid(shotgun_range, i_new, j_new):
            if shotgun_range[i_new][j_new] == '.':
                shotgun_range[i][j] = '.'
                shotgun_range[i_new][j_new] = 'A'
                position = (i_new, j_new)

    elif action == 'shoot':
        if direction == 'right':
            for step in range(j, len(shotgun_range)+1):
                if is_valid(shotgun_range, i, step):
                    if shotgun_range[i][step] == 'x':
                        shotgun_range[i][step] = '.'
                        targets_hit.append([i, step])
                        targets_left -= 1
                        break
        elif direction == 'left':
            for step in range(j, 0-1, -1):
                if is_valid(shotgun_range, i, step):
                    if shotgun_range[i][step] == 'x':
                        shotgun_range[i][step] = '.'
                        targets_hit.append([i, step])
                        targets_left -= 1
                        break
        elif direction == 'up':
            for step in range(i, 0-1, -1):
                if is_valid(shotgun_range, step, j):
                    if shotgun_range[step][j] == 'x':
                        shotgun_range[step][j] = '.'
                        targets_hit.append([step, j])
                        targets_left -= 1
                        break
        elif direction == 'down':
            for step in range(i, len(shotgun_range)):
                if is_valid(shotgun_range, step, j):
                    if shotgun_range[step][j] == 'x':
                        shotgun_range[step][j] = '.'
                        targets_hit.append([step, j])
                        targets_left -= 1
                        break

    if targets_left == 0:
        break

if targets_left == 0:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")

for target in targets_hit:
    print(target)
