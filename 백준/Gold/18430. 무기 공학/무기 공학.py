import sys
n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))


if n*m < 3:
    print(0)
    sys.exit(0)

visited = [[False for i in range(m)] for i in range(n)]
global sumv
sumv = 0
global maxv
maxv = 0
def dfs(row):
    global sumv
    global maxv
    maxv = max(maxv,sumv)

    for i in range(row,n):
        for j in range(m):
            
            if not visited[i][j]:
                for a,b in [((0,-1),(1,0)),((1,0),(0,1)),((0,1),(-1,0)),((-1,0),(0,-1))]:
                    nx1 = i+a[0]
                    ny1 = j+a[1]
                    nx2 = i+b[0]
                    ny2 = j+b[1]
                    
                    if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m and not visited[nx1][ny1] and not visited[nx2][ny2]:               
                        sumv += arr[i][j] *2 + arr[nx1][ny1] + arr[nx2][ny2]
                        visited[i][j] = True
                        visited[nx1][ny1] = True
                        visited[nx2][ny2] = True
                        
                        dfs(i)
                        
                        sumv -= arr[i][j] *2 + arr[nx1][ny1] + arr[nx2][ny2]
                        visited[i][j] = False
                        visited[nx1][ny1] = False
                        visited[nx2][ny2] = False
                        
                
dfs(0)
print(maxv)