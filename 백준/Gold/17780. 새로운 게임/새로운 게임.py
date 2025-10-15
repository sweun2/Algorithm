from collections import defaultdict
n,k = map(int,input().split())
board = []
point = defaultdict(list)
g = []
for i in range(n):
    board.append(list(map(int,input().split())))
    #012 wrb
for i in range(k):
    x,y,d = map(int,input().split())
    g.append((x-1,y-1,d))
    point[(x-1,y-1)].append(i)
    #1234 우좌상하
    
cur = 0
direction = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
cnt = 0
while True:
    if cur == 0:
        cnt +=1
        if cnt > 1000:
            print(-1)
            break    
    
    x,y,d = g[cur]
    if point[(x,y)][0] != cur: # 맨 밑에 있지 아니한 경우
        cur +=1
        if cur == k:
            cur = 0
        continue
    
    dx,dy = direction[d]
    
    nx = x + dx
    ny = y + dy
    
    if 0<= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        temp = point[(x,y)][:]
        point[(x,y)].clear()
        
        point[(nx,ny)].extend(temp)
        
        for j in temp:
            g[j] = (nx,ny, g[j][2])
        g[cur] = (nx,ny,d)

    elif 0<= nx < n and 0 <= ny < n and board[nx][ny] == 1:
        temp = point[(x,y)][::-1]
        point[(x,y)].clear()
        
        point[(nx,ny)].extend(temp)
        for j in temp:
            g[j] = (nx,ny, g[j][2])
        g[cur] = (nx,ny,d)
    else:
        if (dx,dy) ==(1,0):
            dx,dy = -1,0
            d = 3
        elif (dx,dy) ==(-1,0):
            dx,dy = 1,0
            d = 4
        elif (dx,dy) ==(0,1):
            dx,dy = 0,-1
            d = 2
        elif (dx,dy) ==(0,-1):
            dx,dy = 0,1
            d = 1
            
        nx = x + dx
        ny = y + dy
        
        # 방향 바꿨는데 밖으로 향하는 경우 or 바꿔서 가는 칸이 b인경우
        if not (0<= nx < n and 0<= ny < n) or board[nx][ny] == 2: 
            
            g[cur] = (x,y,d)
        else:
            if board[nx][ny] == 0:
                temp = point[(x,y)][:]
                point[(x,y)].clear()
            
                point[(nx,ny)].extend(temp)
                for j in temp:
                    g[j] = (nx,ny, g[j][2])
                g[cur] = (nx,ny,d)
                
            elif board[nx][ny] == 1:
                temp = point[(x,y)][::-1]
                point[(x,y)].clear()
            
                point[(nx,ny)].extend(temp)
                for j in temp:
                    g[j] = (nx,ny, g[j][2])
                g[cur] = (nx,ny,d)
            
    cur+=1
    if cur == k:
        cur = 0
    if len(point[(nx,ny)]) >=4:
            print(cnt)
            break
    
    if cnt > 1000:
        print(-1)
        break
    