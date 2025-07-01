import sys
from collections import deque
import math
input = sys.stdin.readline
queue = deque()

n,m = map(int,input().split())
dp = [math.inf] *(max(n, m) * 2 + 1)

queue.append((n,0))

while queue:
    cur, cnt = queue.popleft()
    if cur == m:
        print(cnt)
        break
    if cur > m+n:
        continue
    
    if dp[cur] > cnt:
        dp[cur] = cnt
    else:
        continue
    
    
    queue.append((cur*2, cnt))
    if cur - 1 >= 0 :
        queue.append((cur-1, cnt+1))
    queue.append((cur+1,cnt+1))