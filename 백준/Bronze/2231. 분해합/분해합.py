n = int(input())
result =0

for i in range(1,n+1):
    sumv = 0
    for j in str(i):
        sumv += int(j)
    
    if sumv+i == n:
        result = i
        break

print(result)