# 05-02. Functions Advanced - Exercise
# 04. Negative vs Positive

numbers = [int(value) for value in input().split()]

sum_positive = sum(filter(lambda x: x > 0, numbers))
sum_negative = sum(filter(lambda x: x < 0, numbers))

print(sum_negative)
print(sum_positive)

if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
