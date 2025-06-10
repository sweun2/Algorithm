from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input().strip()) for i in range(n)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == "H":
            arr[i][j] = 0
        else:
            arr[i][j] = int(arr[i][j])

def dfs(x,y):
    global inf
    
    if not (0<=x<n and 0<=y<m) or arr[x][y] == 0:
        return 0
    
    if visited[x][y]:
        inf = True
        return 0
    
    if dp[x][y]:
        return dp[x][y]
    
    visited[x][y] = True
    maxv = 0
    for dx,dy in [(arr[x][y],0), (-arr[x][y],0), (0,arr[x][y]), (0,-arr[x][y])]:
        nx = x + dx
        ny = y + dy
        
        cnt = dfs(nx,ny)+1
        maxv = max(cnt, maxv)
        if inf:
            break

    visited[x][y] = False
    dp[x][y] = maxv   
    return maxv
        
global inf
inf = False
visited = [[False for i in range(m)]for i in range(n)]
dp = [[0 for i in range(m)]for i in range(n)]

result = dfs(0,0)

print(-1 if inf else result)

