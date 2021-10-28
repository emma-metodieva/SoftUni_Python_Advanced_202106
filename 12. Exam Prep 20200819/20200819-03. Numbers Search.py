# Exam Preparation
# 20200819-03. Numbers Search
# 18:02 - 18:12 = 10 min

def numbers_searching(*args):
    available_nums = list(args)
    min_num = min(available_nums)
    max_num = max(available_nums)

    missing_nums = []
    for n in range(min_num, max_num+1):
        if n not in available_nums:
            missing_nums.append(n)

    seen = set()
    duplicates = set()
    for n in available_nums:
        if n not in seen:
            seen.add(n)
        else:
            duplicates.add(n)

    return [missing_nums.pop(), sorted(list(duplicates))]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

