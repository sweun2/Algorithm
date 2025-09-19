n,m = map(int,input().split())

arr = []
shark = []
for i in range(n):
    temp = list(map(int,input().split()))
    
    for j in range(m):
        if temp[j] == 1:
            shark.append((i,j))
visited = set(shark[:])
depth = 0
for i in range(n*m):
    temp = []
    depth = i 
    if len(visited) == n*m:
        break
    
    while shark:
        x,y  = shark.pop()
        
        for dx,dy in [(1,0),(1,1),(1,-1),(0,0),(0,-1),(0,1),(-1,0),(-1,-1),(-1,1)]:
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0 <= ny < m and (nx,ny) not in visited:
                visited.add((nx,ny))
                temp.append((nx,ny))
    
    shark = temp[:]

print(depth)
                
    