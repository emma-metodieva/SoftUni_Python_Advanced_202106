# 05-01. Functions Advanced - Lab
# 06. Character Combinations

def permutations(s, perm=''):
    if len(s) == 0:
        print(perm)
        return

    for i in range(len(s)):
        char = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permutations(rest, perm + char)


permutations(input())
