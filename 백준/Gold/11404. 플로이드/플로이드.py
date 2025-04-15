import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[math.inf for i in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u][v] = min(graph[u][v], w)
    
dist = [row[:] for row in graph]    
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == math.inf:
            print(0,end=' ')
        else : print(dist[i][j], end=' ')
    print()