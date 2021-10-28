# 05-02. Functions Advanced - Exercise
# 13. Recursive Power

def recursive_power(number, power, result=1):
    if power == 0:
        return result

    result *= number
    return recursive_power(number, power-1, result)


print(recursive_power(2, 10))
print(recursive_power(10, 100))
