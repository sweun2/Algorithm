n = int(input())

arr = list(map(int,input().split()))

lis = []
lis.append(arr[0])

for i in arr:
    if lis[-1] < i:
        lis.append(i)
    else:
        start = 0
        end = len(lis) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if i > lis[mid]:
                start = mid + 1
            elif i < lis[mid]:
                end = mid - 1
            else:
                start = mid
                break
        
        lis[start] = i

print(len(lis))
    
        
    
    