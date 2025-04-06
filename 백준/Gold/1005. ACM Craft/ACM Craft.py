from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    d = [0] + list(map(int,input().split()))
    
    w = [[] for i in range(n+1)]
    indegree = [0 for i in range(n+1)]
    for j in range(k):
        x,y = map(int,input().split())
        w[x].append(y)
        indegree[y] +=1
        
    g = int(input())
    dp=[0 for i in range(n+1)]
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            dp[i] = d[i]
            queue.append(i)
            
    while queue:
        cur = queue.popleft()
        for j in w[cur]:
            indegree[j] -=1
            dp[j] = max(dp[j],dp[cur] + d[j])
            
            if indegree[j] == 0:
                queue.append(j)
    
    print(dp[g])