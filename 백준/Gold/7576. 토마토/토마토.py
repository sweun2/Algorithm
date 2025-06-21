from collections import deque
n,m = map(int,input().split())
arr = []
tomato = deque()

for i in range(m):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            tomato.append((i,j))
    arr.append(row)
            
def bfs():
    x,y = tomato.popleft()
    visited[x][y] = 1
    
    for (dx,dy) in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx = dx + x
        ny = dy + y
        
        if 0<=nx <m and 0<=ny <n and visited[nx][ny] == 0:
            if arr[nx][ny] == 0:
                nt.append((nx,ny))
                visited[nx][ny] = 1
    

day = 0 
visited = [[0]*n for i in range(m)]
nt = deque()
while True:
    while tomato:
        bfs()
    
    if not nt:
        break
    
    for x,y in nt:
        arr[x][y] = 1
    
    tomato = nt.copy()
    nt.clear()
    
    day +=1
    
flag = True
for i in arr:
    for j in i:
        if j == 0:    
            flag = False
            break
if flag:
    print(day)
else:
    print(-1)