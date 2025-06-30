import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numbers= list(map(int,input().split()))
visited = [False]*n
global result
result = set()

def dfs(arr:list):
    global result
    if len(arr) == m:
        result.add(tuple(arr))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(numbers[i])
            dfs(arr)
            visited[i] = False
            arr.pop()
            
dfs(list())
for i in sorted(result):
    print(*i)