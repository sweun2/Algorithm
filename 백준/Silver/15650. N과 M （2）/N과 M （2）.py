n,m = map(int,input().split())
result = list()
arr = list()

def back(depth,arr:list,start):
    if depth == m:
        result.append(arr[:])
        return arr
    
    for i in range(start,n+1):
        arr.append(i)
        back(depth+1, arr, i+1)
        arr.pop()
back(0,arr,1)

for i in result:
    print(' '.join(map(str,i)))