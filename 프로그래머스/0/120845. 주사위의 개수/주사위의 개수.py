def solution(box, n):
    v = 1
    for i in box:
        if i < n:
            return 0
        v *= max((i//n),1)
    
    return v
    