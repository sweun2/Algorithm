n = int(input())

arr = list(map(int,input().split()))
from collections import deque

queue = deque()

for i in range(n):
    if not queue:
        queue.append(arr[i])
        continue
    
    index = len(queue) - 1
    
    if queue[index] >= arr[i]:
        
        while queue[index] >= arr[i] and index>=0:
            index -=1
            
       
        queue[index+1] = arr[i]
    else:
        queue.append(arr[i])
            

print(len(queue))