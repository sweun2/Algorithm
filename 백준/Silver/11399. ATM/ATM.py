n=int(input())
p=list(map(int,input().split()))
arr=list()
result=0
for i in range(n):
    minute=p.pop( p.index( min(p)))
    result+=minute
    arr.append(result)



print(sum(arr))