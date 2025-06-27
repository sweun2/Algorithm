n,m = map(int,input().split())

trees = list(map(int,input().split()))

start = 0
end = max(trees) - 1
mid = (start+end)//2

sumv = 0
maxv = 0
while start<=end:
    sumv = 0
    for j in trees:
        if j>mid:
            sumv += j-mid
        if sumv > m:
            break
    if sumv >= m:
        if maxv<mid:
            maxv = mid
        start = mid + 1
    else:
        end = mid - 1
    mid = (start+end)//2
    
print(maxv)