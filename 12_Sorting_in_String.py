"""
You are given a string S.
        contains alphanumeric characters only.
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""



if __name__ == '__main__':
    S=input()
    lowers = []
    uppers = []
    evens = []
    odds = []
    
    
    for char in S:
        if char.islower():
            lowers.append(char)
        elif char.isupper():
            uppers.append(char)
        elif char.isdigit():
            if int(char)%2==0:
                evens.append(char)
            else:
                odds.append(char)
    
    lowers.sort()
    uppers.sort()
    evens.sort()
    odds.sort()
    
    print("".join(lowers+uppers+odds+evens))