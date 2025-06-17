import math
n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
    

dist = [[math.inf for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                

for i in range(n):
    for j in range(n):
        if dist[i][j] != math.inf:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
        