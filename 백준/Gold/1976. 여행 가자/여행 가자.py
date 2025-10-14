from collections import defaultdict,deque
import sys
sys.setrecursionlimit(10**9)
n = int(input())
m = int(input())

dd = defaultdict(set)

for i in range(1, n+1):
    dd[i].add(i)
    do = list(map(int,input().split()))
    
    for j in range(len(do)):
        if not do[j]:
            continue
        
        dd[i].add(j+1)
        dd[j+1].add(i)

queue = deque()
for i in list(map(int,input().split())):
    queue.append(i)

def dfs(x:int, visited:list):

 
    for nx in dd[x]:
        if not queue:
            return
        
        if not visited[nx]:
            visited[nx] = True
            
            if nx == queue[0]:
                queue.popleft()
                visited = [False]* (n+1)
            
            dfs(nx,visited)

visited = [False] * (n+1)
start = queue.popleft()
dfs(start,visited)
print("YES" if not queue else "NO")