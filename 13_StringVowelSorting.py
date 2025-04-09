"""
Given a string of lowercase letters only, your task is to:

Place all vowels first, in alphabetical order

Then all consonants, also in alphabetical order


"""

s = input()

vowels = []
consonants = []

for ch in s:
    if ch in 'aeiou':
        vowels.append(ch)
    else:
        consonants.append(ch)

vowels.sort()
consonants.sort()

print(''.join(vowels + consonants))
