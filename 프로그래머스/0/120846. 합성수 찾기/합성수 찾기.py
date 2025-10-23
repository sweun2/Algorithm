import math
def solution(n):
    
    def prime(n):
        arr = [False] * (n+1)
        for i in range(2,int(math.sqrt(n))+1):
            
            start= i 
            cur = i 
            cur += start
            while cur <= n:
                arr[cur] = True
                cur += start
                
        return [i for i in range(1,n+1) if arr[i]]
    return len(prime(n))
                
                
               
            
    
    