from collections import deque
n,m = map(int,input().split())
visited =deque()
for i in range(m):
    visited.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = deque()

for i in range(m):
    for j in range(n):
        if visited[i][j]==1: 
            queue.append((i,j))

while queue:
    x,y = queue.popleft()      
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if visited[nx][ny] == 0 and visited[nx][ny] != -1:
                visited[nx][ny]=visited[x][y]+1
                queue.append((nx,ny))
                
print(max(map(max,visited))-1)
    