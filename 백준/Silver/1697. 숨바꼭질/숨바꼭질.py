import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n,k = map(int,input().split())

queue = deque()

dp = [abs(k-n)+1] *200001
dp[n] = 0
queue.append((n,0))

while queue:
    n,cnt = queue.popleft()
    
    for i in [n-1,n+1,2*n]:
        if i >=0 and i<200001 and dp[i] > cnt+1 and dp[n]+1 < dp[i]:
            dp[i] = cnt+1
            queue.append((i,cnt+1))
            

print(dp[k])