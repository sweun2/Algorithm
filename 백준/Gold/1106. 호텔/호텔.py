import sys
input = sys.stdin.readline

c,n = map(int,input().split())
result = list()
for i in range(n):
    cost, people = map(int,input().split())
    result.append((cost,people))

import math
dp = [math.inf for i in range(c+100)]

dp[0] = 0

for i,j in result:
    for k in range(1, c+100):
        if j<=k:
            dp[k] = min(dp[k],dp[k-j]+i)


print(min(dp[c:]))    