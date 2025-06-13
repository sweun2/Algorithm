def solution(sizes):
    
    s = set()
    for x,y in sizes:
        s.add(x)
        s.add(y)
    
    s = list(s)
    result = 1000 * 1000
    
    for i in s:
        for j in s:
            
            flag = True
            for x,y in sizes:
                if (i < x or j < y) and (i < y or j < x):
                    
                    flag = False
                    break
            
            if flag and i*j < result:
                result = i*j
    return result           
