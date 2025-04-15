import sys
import math
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())

graph = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]
distance = [math.inf for i in range(v+1)]

for i in range(e):
    u,ve,w = map(int,input().split())
    graph[u].append((ve,w))
    
def get_smallest_node():
    index = 0
    minv = math.inf
    for i in range(1,v+1):
        if minv > distance[i] and visited[i] ==0:
            minv = distance[i]
            index = i
    return index
import heapq

def dik(start):
    q = []
    distance[start] = 0 
    heapq.heappush(q,(0,start))
    
    while q:
        weight,now = heapq.heappop(q)
        
        if distance[now]< weight:
            continue
        
        for i in graph[now]:
            if weight + i[1] < distance[i[0]]:
                distance[i[0]] = weight + i[1]
                heapq.heappush(q,(weight+i[1],i[0]))
    
dik(k)
for i in distance[1:]:
    if i ==math.inf:
        print("INF")
    else: print(i)
