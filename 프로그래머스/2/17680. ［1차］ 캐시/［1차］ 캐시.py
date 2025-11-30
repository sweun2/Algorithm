from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    def updateCache(item):
        for i in range(len(cache)):
            if cache[i] == item:
                temp = cache[i]
                cache.remove(temp)
                cache.appendleft(temp)
                return True
        return False            
        
    
    for city in cities:
        city = city.lower()
        isHits = updateCache(city)
        
        if isHits:
            answer += 1
        else:
            answer += 5
            cache.appendleft(city)
            
            if len(cache) > cacheSize:
                cache.pop()
    
    return answer
        
        
        
                
        
        
    