def solution(n, results):
    win = [[] for i in range(n+1)]
    lose = [[] for i in range(n+1)]
    
    for a,b in results:
        win[a].append(b)
        lose[b].append(a)


    re = [set() for _ in range(n+1)]
    for i in range(1,n+1):
        
        def dfs(start,x,graph,visited):
            for j in graph[x]:
                if j not in visited:
                    visited.add(j)
                    re[start].add(j)
                    dfs(start,j,graph,visited)

        dfs(i,i,win,set())
        dfs(i,i,lose,set())
    
    cnt = 0
    for i in re:
        if len(i) >= n-1:
            cnt +=1
    return cnt
        
        