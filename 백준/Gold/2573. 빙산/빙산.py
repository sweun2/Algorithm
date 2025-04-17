n,m = map(int,input().split())
import sys
sys.setrecursionlimit(10000)
graph = [list(map(int,input().split())) for i in range(n)]
def check_melt():
    melt = [[0 for i in range(m)] for i in range(n)]
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    for i,j in ice:
        for k in range(4):
            nx = i + direction[k][0]
            ny = j + direction[k][1]
            if 0<=nx < n and 0<=ny <m and graph[nx][ny] == 0:
                melt[i][j] +=1
    return melt
from collections import deque
cnt=0
while True:
    cnt +=1
    ice = [(i,j) for i in range(n) for j in range(m) if graph[i][j]>0]
    if not ice:
        print(0)
        break    
    melt = check_melt()
    
    for i,j in ice:
        graph[i][j] -= melt[i][j]
        if graph[i][j] <=0:
            graph[i][j] = 0
    
    queue = deque()
    visited = set()
    def bfs():
        x,y = queue.pop()
        visited.add((x,y))
        
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx < n and 0<=ny <m and (nx,ny) not in visited:
                if graph[nx][ny] !=0:
                    queue.append((nx,ny))
    group = 0
    for i,j in ice:
        if graph[i][j] != 0 and (i,j) not in visited :
            group +=1
            queue.append((i,j))
            while queue:
                bfs()
            if group >1:
                break 
    if group > 1:
        print(cnt)
        break