# 05-02. Functions Advanced - Exercise
# 09. Function Executor

def func_executor(*args):
    results = []
    for func in args:
        results.append(func[0](*func[1]))
    return results


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
