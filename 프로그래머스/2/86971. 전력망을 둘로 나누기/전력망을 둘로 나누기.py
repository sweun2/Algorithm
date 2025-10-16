def solution(n, wires):
    graph = [[]for i in range(n+1)]
    
    for i,j in wires:
        graph[i].append(j)
        graph[j].append(i)
    
    
    def dfs(l,r,x):
        global cnt
        visited[x] = True
        cnt += 1
        
        for nx in graph[x]:
            if nx != l and nx != r and not visited[nx]:
                dfs(l,r,nx)
            
        
        
    
    global cnt
    minv = n
    for l,r in wires:
        cnt = 0 
        visited = [False] * (n+1)
        
        dfs(l,r,l)
        left = cnt
        
        cnt = 0 
        visited = [False] * (n+1)
        dfs(l,r,r)
        right = cnt
        
        minv = min(abs(left-right),minv)
        
    return minv
        