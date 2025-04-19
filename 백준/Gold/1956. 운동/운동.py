import sys
import math
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[0 for i in range(v+1)] for i in range(v+1)]
d = [[math.inf for i in range(v+1)] for i in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    d[a][b] = c

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

result = math.inf
for i in range(1,v+1):
    if d[i][i] < result:
        result = d[i][i]

if result == math.inf:
    print(-1)
else:print(result)