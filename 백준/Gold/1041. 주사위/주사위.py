import sys

n=int(input())
arr=list(map(int,input().split()))

if(n!=1):
    result= ((n**2-3*n+2)*4 + (n-2)**2)*min(arr)

    min_two=sys.maxsize
    for i in range(5):
        for j in reversed(range(i+1,6)):
            if(i+j)!=5:
                if min_two>(arr[i]+arr[j]):
                    min_two=arr[i]+arr[j]

    result+= ((n-2)*min_two)*4+((n-1)*min_two)*4

    min_third=sys.maxsize
    for i in range(4):
        for j in range(i+1,5):
            for k in range(j+1,6):
                if(i+j)!=5 and (i+k)!=5 and(k+j)!=5:
                    if (arr[i]+arr[j]+arr[k])<min_third:
                        min_third=arr[i]+arr[j]+arr[k]

    result += min_third*4

    print(result)
else:
    print(sum(arr)-max(arr))