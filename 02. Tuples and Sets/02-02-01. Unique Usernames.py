# 02-02. Tuples and Sets - Exercise
# 01. Unique Usernames

n = int(input())
usernames = set()

for _ in range(n):
    usernames.add(input())

[print(username) for username in usernames]
