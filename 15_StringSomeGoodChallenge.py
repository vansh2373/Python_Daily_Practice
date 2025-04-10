"""
Group characters into 6 separate lists:

Lower vowels

Lower consonants

Upper vowels

Upper consonants

Odd digits

Even digits

Sort each list

Join them in the order listed

"""

s = input()

lvowels = []
lconsonants = []
uvowels = []
uconsonants = []
odds = []
evens = []

for ch in s:
    if ch.isalpha():
        if ch in 'aeiou':
            lvowels.append(ch)
        elif ch in 'AEIOU':
            uvowels.append(ch)
        elif ch.islower():
            lconsonants.append(ch)
        else:
            uconsonants.append(ch)
    elif ch.isdigit():
        if int(ch) % 2 == 0:
            evens.append(ch)
        else:
            odds.append(ch)

# Sort all groups
lvowels.sort()
lconsonants.sort()
uvowels.sort()
uconsonants.sort()
odds.sort()
evens.sort()

# Combine all groups in order
result = ''.join(lvowels + lconsonants + uvowels + uconsonants + odds + evens)
print(result)
