def solution(n, s):
    if n>s:
        return [-1]
    
    avg = s // n
    m = s % n
    
    l = [avg] * n
    for i in range(n-1,n-1-m,-1):
        l[i] +=1
    
    
    return l
    