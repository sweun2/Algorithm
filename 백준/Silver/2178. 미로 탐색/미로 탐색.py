import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
visited = [[0 for i in range(m)] for i in range(n)]

miro = []
for i in range(n):
    temp = input()
    arr = list()
    for j in temp:
        if j != '\n':
            arr.append(int(j))
    miro.append(arr)


def bfs():
    x,y = queue.popleft()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx and nx< n and 0 <= ny and ny < m:
            if miro[nx][ny] == 0:
                continue
            
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1


graph = [[0 for i in range(m)] for i in range(n)]
graph[0][0] = 1
queue = deque()
queue.append((0,0))
visited[0][0] = 1
while queue:
    bfs()

print(graph[n-1][m-1])
    
    
