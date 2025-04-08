"""
You're helping with a digital toll booth system. Every vehicle has a 4-digit number plate, and the toll system has a special rule:

📌 Only vehicles with palindromic 4-digit numbers that are even and divisible by 11 can use the FastLane (a fast pass gate).

Your task:
🔹 From the list of vehicle numbers, print all the ones eligible for FastLane.
"""
"""
approach that i will follow
1 -- taking 4 digit input num 
2 -- if num not a 4 digit or > 4 digit then terminate the program as it can't pass the toll gate 
3 -- if yes then applying conditions 4 digit%2==0,4digitnum%11==0
4 -- printing fastverified no in a single line usind end =" ".
5 -- if no numbers are 4 digit then print No fastlane Vehicles.
"""

n=int(input())
arr = list(map(int,input().split()))
found = False 
for i in range(n):
    if (1000<=arr[i]<=9999):
        if(str(arr[i]) == str(arr[i])[::-1] and arr[i]%2==0 and arr[i]%11==0):
            print(arr[i],end=" ")
            found = True
if not found:
    print("No Fastlane Vehicles")