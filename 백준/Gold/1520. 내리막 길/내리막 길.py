n,m = map(int,input().split())
import sys
sys.setrecursionlimit(10**7)

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for i in range(n) ]
dp =[ [-1 for _ in range(m)] for i in range(n) ]
from collections import deque
queue = deque()

def dfs():
    x,y = queue.pop()
    if x == n-1 and y == m-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    dp[x][y] = 0
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0<=nx<n and 0<= ny < m :
            if graph[nx][ny] < graph[x][y]:
                queue.append((nx,ny))
                
                dp[x][y] += dfs()
    return dp[x][y]            
    
queue.append((0,0))
dfs()
print(dp[0][0])