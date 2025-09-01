n = int(input())

arr = list(map(int,input().split()))

a,b = map(int,input().split())

sumv = 0
for i in arr:
    sumv += 1
    if (i-a) > 0 :
        sumv += ((i-a) // b)
        if (i-a)% b !=0:
            sumv +=1

print(sumv)