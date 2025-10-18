import math
from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = [math.inf] * (n+1)
    queue = deque([destination])
    dist[destination] = 0
    visited = [False] * (n+1)
    visited[destination] = True

    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                dist[nx] = dist[x] + 1
                queue.append(nx)

    result = []
    for s in sources:
        if dist[s] == math.inf:
            result.append(-1)
        else:
            result.append(dist[s])

    return result
