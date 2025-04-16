n = int(input())
arr = list(map(int,input().split()))
d= int(input())

def dfs(d,arr):
    arr[d] = -2
    for i in range(len(arr)):
        if d == arr[i]:
            dfs(i,arr)


dfs(d,arr)
cnt = 0
for i in range(len(arr)):
    if i not in arr and arr[i] != -2:
        cnt +=1

print(cnt)