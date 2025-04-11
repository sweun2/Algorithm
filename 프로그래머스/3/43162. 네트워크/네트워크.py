from collections import deque
def solution(n, computers):
    visited = [0 for i in range(n)]
    
    queue = deque()
    
    def bfs():
        cur = queue.popleft()
        for j in range(len(computers[cur])):
            if cur == j:
                continue
            if computers[cur][j] == 1:
                if visited[j] == 0:
                    visited[j] = 1
                    queue.append(j)
    
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            cnt +=1
            queue.append(i)
            while queue:
                bfs()

    return cnt