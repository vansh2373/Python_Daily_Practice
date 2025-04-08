"""
input 
5
121 34 44 99 123
output
print all the palindromic numbers from the list 
"""

n = int(input())
arr = list(map(str,input().split()))
for i in range(len(arr)):
    if arr[i] == arr[i][::-1]:
        print(arr[i],end=" ")
