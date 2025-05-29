def solution(citations):
    length = len(citations)
    result = 0
    for i in range(length,0,-1):
        cnt = 0
        for j in citations:
            if j>=i:
                cnt +=1
        if cnt >=i:
            result = i
            break
            
    return result
            
        
        
