def solution(brown, yellow):
    for i in range(1, (int(brown/2) -2)+1):
        x = i
        y = (int(brown/2) - 2) -x
        
        if x * y ==yellow:
            return sorted([x+2,y+2],reverse = True)
    
