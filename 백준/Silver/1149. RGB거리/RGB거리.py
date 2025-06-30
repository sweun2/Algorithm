import sys
import math
input = sys.stdin.readline
n = int(input())
color = [-1]*n
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dp = [[0]*3 for i in range(n)]
for i in range(3):
    dp[0][i] = arr[0][i]

for i in range(n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1]+arr[i][1],dp[i-1][2]+arr[i][2])
        elif j == 1:
            dp[i][j] = min(dp[i-1][0]+arr[i][0],dp[i-1][2]+arr[i][2])
        else:
            dp[i][j] = min(dp[i-1][1]+arr[i][1],dp[i-1][0]+arr[i][0])

print(min(dp[n-1]))