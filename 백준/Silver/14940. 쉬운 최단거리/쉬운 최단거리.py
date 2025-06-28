from collections import deque

n,m = map(int,input().split())

maps = []
stone = []
start = 0,0
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        if temp[j] == 2:
            start = i,j
        elif temp[j] == 0:
            stone.append((i,j))        
    maps.append(temp)

queue = deque()
queue.append(start)

visited = [[False]* m for i in range(n)]
visited[start[0]][start[1]] = True

result = [[-1]* m for i in range(n)]
result[start[0]][start[1]] = 0
for i,j in stone:
    result[i][j] = 0


while queue:
    x,y = queue.popleft()
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if 0<= nx and nx< n and 0<= ny and ny<m and not visited[nx][ny] and maps[nx][ny] !=0:
            queue.append((nx,ny))
            visited[nx][ny] = True
            result[nx][ny] = result[x][y] +1


for i in result:
    s = ""
    for j in i:
        s += str(j) + " "
    print(s.strip())