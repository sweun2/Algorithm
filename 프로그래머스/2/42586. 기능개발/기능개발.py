def solution(progresses, speeds):
    date = []
    length = len(speeds)
    for i in range(length):
        if((100-progresses[i])%speeds[i]) !=0:
            date.append((100-progresses[i])//speeds[i]+1)
        else:
            date.append((100-progresses[i])//speeds[i])
    
    cur = date[0]
    cnt = 0
    result = list()
    for i in range(len(date)):
        if date[i] <=cur:
            cnt +=1
        else:
            result.append(cnt)
            cur = date[i]
            cnt = 1
        if i == len(date) - 1:
            result.append(cnt)
    return result
            
            
        
        
        
        
    
