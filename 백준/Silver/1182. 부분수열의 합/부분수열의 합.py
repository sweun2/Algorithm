n,s = map(int,input().split())
arr = list(map(int,input().split()))
from itertools import combinations
cnt = 0
for i in range(1,n+1):
    t = combinations(arr,i)
    for j in t:
        if sum(j) == s:
            cnt +=1

print(cnt)