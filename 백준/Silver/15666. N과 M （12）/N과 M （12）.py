n,m = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))


def dfs(depth:int ,result:list, cur:int):
    if depth == m:
        print(*result)
        return
    
    for i in range(cur, len(arr)):
        result.append(arr[i])
        dfs(depth+1, result, i)
        result.remove(arr[i])

dfs(0, [], 0)