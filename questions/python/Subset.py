# Subset Sum 

# Problem statement: 
# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

# sample input array
val = [3, 34, 4, 12, 5, 2] 
n = len(val)

# sample target value
target = 9

# dp array
ans = [[False]*(target+1) for _ in range(n+1)]

# initialization of dp array 
for i in range(n+1):
    ans[i][0] = True

for i in range(1, n+1):
    for j in range(1, target+1):
        if val[i-1] <= j:
            ans[i][j] = ans[i-1][j-val[i-1]] or ans[i-1][j]

        else:
            ans[i][j] = ans[i-1][j]

# printing the answer
print(ans[-1][-1])