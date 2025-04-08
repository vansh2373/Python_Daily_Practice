n = int(input())
count1 = 0
list1 = []
arr = list(map(str,input().split()))
for i in range(len(arr)):
    if (arr[i] == arr[i][::-1]) and (int(arr[i])%2==0):
        list1.append(int(arr[i]))
if not list1: 
    print(-1)
else:
    print(max(list1))
