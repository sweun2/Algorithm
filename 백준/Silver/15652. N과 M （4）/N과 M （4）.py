n,m = map(int,input().split())
result = []


def dfs(depth, start):
    if depth == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        dfs(depth + 1, i)
        result.remove(i)

dfs(0,1)