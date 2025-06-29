n = int(input())
graph = [list() for i in range(n+1)]

for i in range(n-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)


parent = [0] * (n+1)

def dfs():
    visiting = set()
    visited = set()
    
    visited.add(1)
    visiting.add(1)

    while visiting:
        x = visiting.pop()
        for i in graph[x]:
            if i not in visited:
                parent[i] = x
                visited.add(i)
                visiting.add(i)

dfs()
for i in range(2,n+1):
    print(parent[i])