import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
tree = dict()

for i in range(n+1):
    tree[i] = list()

for i in range(n-1):
    p,c, v = map(int,input().split())
    tree[p].append((c,v))
    tree[c].append((p,v))
    

visited = [False] *(n+1)
global maxv
global maxn
global sumv
sumv = 0
maxv = 0
maxn = 0
def dfs(node):
    global maxv
    global maxn
    global sumv
    if not tree[node]:
        return
    
    visited[node] = True
    
    for (i,v) in tree[node]:
        if visited[i] == False:
            visited[i] = True
            sumv += v
            dfs(i)
            if maxv < sumv:
                maxv = sumv
                maxn = i
                
            sumv -=v
            visited[i] = False
             

dfs(1)
visited = [False] *(n+1)
sumv = 0
maxv = 0
dfs(maxn)

print(maxv)