# 02-01. Tuples and Sets - Lab
# 02. Average Student Grades

n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    student = data[0]
    grade = float(data[1])
    if student not in students:
        students[student] = []
    students[student].append(grade)

for key, value in students.items():
    grades_as_str = ' '.join(map(lambda f: f'{f:.2f}', value))
    print(f"{key} -> {grades_as_str} (avg: {sum(value) / len(value):.2f})")
