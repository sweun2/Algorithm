n = int(input())

arr = list(map(int,input().split()))
maxdp = arr[:]
mindp = arr[:]
for i in range(1,n):
    arr = list(map(int,input().split()))
    maxdp = [arr[0] + max(maxdp[0],maxdp[1]), arr[1] + max(maxdp[0],maxdp[1],maxdp[2]), arr[2] + max(maxdp[2],maxdp[1])]
    
    mindp = [arr[0] + min(mindp[0],mindp[1]), arr[1] + min(mindp[0],mindp[1],mindp[2]), arr[2] + min(mindp[2],mindp[1])]

print(max(maxdp))    
print(min(mindp))