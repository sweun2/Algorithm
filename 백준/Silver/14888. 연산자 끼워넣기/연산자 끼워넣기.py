n = int(input())

arr = list(map(int,input().split()))

plus,minus,multi,div = list(map(int,input().split()))

from collections import deque
queue = deque()
queue.append((plus,minus,multi,div,arr[0],0))
maxv = -10**10
minv = 10**10
while queue:    
    pl,mi,mul,di,sumv,i = queue.popleft()

    if i == len(arr) -1 :
        minv = min(minv,sumv)
        maxv = max(maxv,sumv)
        continue
    
    if pl:
        queue.append((pl-1,mi,mul,di,sumv + arr[i+1],i+1))
    if mi:
        queue.append((pl,mi-1,mul,di,sumv - arr[i+1],i+1))
    if mul:
        queue.append((pl,mi,mul-1,di,sumv * arr[i+1],i+1))
    if di:
        if sumv < 0:
            queue.append((pl,mi,mul,di-1,-(-sumv // arr[i+1]),i+1))
        else:
            queue.append((pl,mi,mul,di-1,sumv // arr[i+1],i+1))


print(maxv)
print(minv)