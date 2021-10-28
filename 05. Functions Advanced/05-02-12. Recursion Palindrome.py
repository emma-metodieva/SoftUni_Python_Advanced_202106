# 05-02. Functions Advanced - Exercise
# 12. Recursion Palindrome

# def palindrome(word, i):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"


def palindrome(word, i):
    j = len(word) - i
    curr_string = word[i:j]
    if len(curr_string) <= 1:
        return f"{word} is a palindrome"

    if curr_string[0] != curr_string[-1]:
        return f"{word} is not a palindrome"
    else:
        return palindrome(word, i+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
