import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = 1
    nxt = select[x]

    if visited[nxt] == 0:  
        dfs(nxt)
    elif visited[nxt] == 1: 
        cur = nxt
        cycle = 0
        while True:
            cycle += 1
            cur = select[cur]
            if cur == nxt:
                break
        cnt += cycle 

    visited[x] = 2

t = int(input())
for _ in range(t):
    n = int(input())
    select = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)

    print(n - cnt)
