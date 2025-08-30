n,m = map(int,input().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a,b,v = map(int,input().split())
    graph[a].append((v,b))
    graph[b].append((v,a))

import heapq
hq = graph[1][:]
heapq.heapify(hq)

visited = [False] * (n+1)
result = 0
visited[1] = True
while True:
    while hq:
        minv, next = heapq.heappop(hq)
        if not visited[next]:
            break
    visited[next] = True
    result += minv
    
    if visited.count(1) == n:
        break
    
    for i in graph[next]:
        heapq.heappush(hq,i)
    
    
print(result)

    