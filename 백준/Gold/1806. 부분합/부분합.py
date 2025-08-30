n,s = map(int,input().split())
arr = list(map(int,input().split()))

from collections import deque
minv = 10**8
queue = deque()
sumv = 0
for i in arr:
    sumv += i
    queue.append(i)
    if sumv + i >= s: 
        while queue and sumv >= s:
            p = queue.popleft()
            sumv -= p
        minv = min(minv,len(queue) + 1)
if len(queue) == n:
    print(0)
else:
    print(minv)