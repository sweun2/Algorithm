n,m = map(int,input().split())
indegree = [0] * (n+1)
graph = [[]for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) # a => b
    indegree[b] +=1 
    
from collections import deque
queue = deque()
for d in range(1,n+1):
    if indegree[d] == 0:
        queue.append(d)

result = []
while queue:
    x = queue.popleft()
    result.append(x)
    
    for b in graph[x]:
        indegree[b] -=1
        
        if indegree[b] == 0:
            queue.append(b)
print(" ".join(map(str,result)))