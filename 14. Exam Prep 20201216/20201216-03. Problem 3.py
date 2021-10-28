# Exam Preparation
# 20201216-03. Problem 3
# 16:30 - 16:45 = 15 min

def get_magic_triangle(n):

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        row = []
        for j in range(i + 1):
            if j == 0:
                row.append(triangle[i - 1][0])
            elif j == i:
                row.append(triangle[i - 1][-1])
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle


print(get_magic_triangle(2))
print(get_magic_triangle(5))
