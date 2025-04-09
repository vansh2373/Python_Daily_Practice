"""
Given a string containing alphanumeric characters (both letters and digits), sort it using these rules:

All vowels (a, e, i, o, u — both lowercase and uppercase) come first (sorted case-insensitively, but preserve the original case).

Then come consonants (also sorted case-insensitively, preserving case).

Then come all digits, but:

Odd digits before even digits

Both groups should be sorted numerically

"""


s = input()

vowels = []
consonants = []
odds = []
evens = []

for ch in s:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowels.append(ch)
        else:
            consonants.append(ch)
    elif ch.isdigit():
        if int(ch) % 2 == 0:
            evens.append(ch)
        else:
            odds.append(ch)

vowels.sort(key=lambda x: x.lower())
consonants.sort(key=lambda x: x.lower())
odds.sort()
evens.sort()


result = ''.join(vowels + consonants + odds + evens)
print(result)
