import heapq

def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)
        
    for _ in range(n):
        largest = heapq.heappop(works)
        if largest == 0:
            return 0
        heapq.heappush(works, largest + 1)
    
    return sum([w*w for w in works])    
        
        
        
        
                
    
            
            
    
            
            
            
        
        
    
    
    
    
