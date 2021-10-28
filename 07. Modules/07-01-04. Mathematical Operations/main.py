from mapper import mapper

num1, sign, num2 = input().split()
num1 = float(num1)
num2 = float(num2)

print(f"{mapper[sign](num1, num2):.2f}")
