# 05-01. Functions Advanced - Lab
# 08. Expressions

def expression(numbers, curr_result=0, curr_expression=''):
    if not numbers:
        print(f"{curr_expression}={curr_result}")
        return
    expression(numbers[1:], curr_result + numbers[0], f"{curr_expression}+{numbers[0]}")
    expression(numbers[1:], curr_result - numbers[0], f"{curr_expression}-{numbers[0]}")


integers = [int(value) for value in input().split(', ')]
expression(integers)
