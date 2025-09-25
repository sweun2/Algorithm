n = int(input())
m = int(input())

down = [[]for i in range(n+1)]
up = [[]for i in range(n+1)]
result = [[False for i in range(n+1)] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    down[a].append(b)
    up[b].append(a)


for i in range(1,n+1):
    start = i
    visited = [False] * (n+1)
    
    def dfs(x):
        for i in down[x]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
    visited[start] = True
    dfs(start)
    
    for j in range(len(visited)):
        result[i][j] = visited[j]
        

for i in range(1,n+1):
    start = i
    visited = [False] * (n+1)
    
    def dfs(x):
        for i in up[x]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
    visited[start] = True
    dfs(start)
    
    for j in range(len(visited)):
        if visited[j]:
            result[i][j] = visited[j]

for i in result[1:]:
    print(n - (i.count(True)))    