n,m,k=tuple(map(int,input().split()))
arr=sorted( list(map(int,input().split())))
result=0
first= arr[n-1]
second=arr[n-2]

#m <10000 인경우->greedy
"""
while m>0:
    for i in range(k):
        if m==0:
            break
        result+=first
        m -= 1
    if m==0:
        break
    result+=second
    m-=1

print(result)
"""

#m이 매우 큰 경우 시간초과

#수열로 접근
div=m//(k+1)
mod=m%(k+1)

structure = first*k + second
result=structure*div + mod*first
print(result)

"""
grredy의 경우 시간복잡도 o(m)
"""
