import math
import heapq

def solution(n, costs):
    graph = [[] for i in range(n)]
    for x,y,v in costs:
        graph[x].append((v,y))
        graph[y].append((v,x))
        
    visited = [False] * n
    pq = graph[0][:]
    visited[0] = True
    heapq.heapify(pq)
    result = 0
    cnt = 0
    while pq and cnt < n:
        v,x = heapq.heappop(pq)
        
        if not visited[x] :
            visited[x] = True
            result += v
            cnt +=1
            for nv,y in graph[x]:
                if not visited[y]:
                    heapq.heappush(pq,(nv,y))
                    
    return result
    