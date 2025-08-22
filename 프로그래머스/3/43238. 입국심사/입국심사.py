import math
def solution(n, times):
    start = 0
    end = max(times) * n
    answer = 0 
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for time in times:
            result += mid // time 
            
            if result >= n :
                break
        
        if result >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
        
    return answer
    

