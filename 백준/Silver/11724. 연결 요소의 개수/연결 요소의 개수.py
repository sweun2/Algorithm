from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list() for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)



def bfs(x):
    visited[x] = True
    
    for e in graph[x]:
        if not visited[e]:
            visited[e] = True
            queue.append(e)
            
from collections import deque
queue = deque()        
cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        queue.append(i)
        
        while queue:
            x = queue.pop()
            bfs(x)
        cnt +=1
        
print(cnt)