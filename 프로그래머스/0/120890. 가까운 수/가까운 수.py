def solution(array, n):
    answer = 0
    minv = 101
    
    for i in array:
        if abs(n-i) < minv:
            minv = abs(n-i)
            answer = i
        elif abs(n-i) == minv:
            answer = min(answer,i)
                
    return answer