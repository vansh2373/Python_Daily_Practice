"""
You are given:

An integer n → total number of scores.

A list of n integers → these are the scores.

You need to find the second highest score (called the runner-up score).

"""

n = int(input())
arr = list(map(int,input().split()))

max_score = max(arr)
filtered_score = [score for score in arr if score != max_score]

print(max(filtered_score))