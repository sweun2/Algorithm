import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    temp = []
    for i in input().rstrip():
        temp.append(int(i))
    
    graph.append(temp)
    

from collections import deque
import math
queue = deque()
visited = [[math.inf for i in range(n)] for i in range(n)]
visited[0][0] = 0
queue.append((0,0))
def z1bfs():
    x,y = queue.popleft()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx < n and 0<=ny<n:
            cost = visited[x][y] + (graph[nx][ny] == 0)
            if cost < visited[nx][ny]:
                visited[nx][ny] = cost
                if graph[nx][ny] == 1:
                    queue.appendleft((nx,ny))
                else:
                    queue.append((nx,ny))

while queue:
    z1bfs()    
    
print(visited[n-1][n-1])