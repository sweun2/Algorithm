def solution(balls, share):
    sumv = 1
    
    for i in range(balls,balls - share,-1):
        sumv *= i
    div = 1
    for j in range(1,share+1):
        div *=j
    return int(sumv//div)
            
        
    
