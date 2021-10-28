# 04-01. Comprehensions - Lab
# 02. No Vowels

def is_vowel(character):
    if character.lower() in ['a', 'o', 'u', 'e', 'i']:
        return True
    return False


text = list(input())

print(''.join([char for char in text if not is_vowel(char)]))
