"""

Generate all combinations of (i, j, k) such that:

0 ≤ i ≤ x

0 ≤ j ≤ y

0 ≤ k ≤ z

Exclude combinations where the sum i + j + k is even (i.e., only allow odd sums)


"""


x = int(input())
y = int(input())
z = int(input())

list1 = [(i,j,k) for i in range(x+1)
                for j in range(y+1)
                for k in range(z+1) if (i+j+k) % 2!=0]
print(list1)