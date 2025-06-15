def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    num = n - len(lost)
    b = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            b.append(i)
            num +=1
    
    for i in b:
        lost.remove(i)
            
    for i in lost:
        if (i-1) in reserve:
            reserve.remove(i-1)
            num +=1
        elif (i+1) in reserve:
            reserve.remove(i+1)
            num +=1
        else:
            continue
    return num