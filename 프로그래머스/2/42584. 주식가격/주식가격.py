from collections import deque
def solution(prices):
    pq = deque()
    n = len(prices)
    result = [0] * n
    
    for i in range(n):
        if not pq:
            pq.append((prices[i],i))
        
        else:
            while pq and pq[-1][0] > prices[i] :
                p,index = pq.pop()
                result[index] = i - index 
            
            pq.append((prices[i],i))
    
    for p,index in pq:
        result[index] = n - 1 - index
    
    return result