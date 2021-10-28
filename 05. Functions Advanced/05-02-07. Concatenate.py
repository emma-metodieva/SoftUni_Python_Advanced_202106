# 05-02. Functions Advanced - Exercise
# 07. Concatenate

def concatenate(*args):
    result = ''
    for arg in args:
        result += arg
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
