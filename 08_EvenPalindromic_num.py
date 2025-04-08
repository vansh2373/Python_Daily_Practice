n = int(input())
arr = list(map(str,input().split()))
for i in range(len(arr)):
    if (arr[i] == arr[i][::-1]) and (int(arr[i])%2==0):
        print(arr[i],end=" ")