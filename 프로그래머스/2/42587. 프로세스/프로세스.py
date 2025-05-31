def solution(priorities, location):
    value = priorities[location]
    arr = list()
    for i in range(len(priorities)):
        arr.append((priorities[i],i))
    
    cnt = 0
    while True:
        cur = arr[0][0]
        if max(priorities) > cur:
            arr.append((arr[0]))
            arr.remove(arr[0])
        else:
            if arr[0][1] == location:
                return cnt+1
                
            priorities.remove(cur)
            arr.remove(arr[0])
            cnt +=1
            
        
        
    
    