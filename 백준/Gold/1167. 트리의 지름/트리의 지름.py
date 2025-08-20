n = int(input())
graph = [[]for i in range(n+1)]
import sys
sys.setrecursionlimit(10**9)
for i in range(n):
    temp = list(map(int,input().split()))
    node = temp[0]
    
    for j in range(1,len(temp[1:-1]),2):
        graph[node].append((temp[j],temp[j+1]))
        

visited = [False] * (n+1)
global maxv
global maxn
maxv = 0
maxn = -1
def dfs(x,sumv):
    global maxv
    global maxn
    
    for n,v in graph[x]:
        if not visited[n]:
            visited[n] = True
            dfs(n,sumv+v)
    if maxv < sumv:
        maxn = x
        maxv = sumv

visited[1] = True
dfs(1,0)
visited = [False] * (n+1)
maxv = 0
visited[maxn] = True
dfs(maxn,0)
print(maxv)