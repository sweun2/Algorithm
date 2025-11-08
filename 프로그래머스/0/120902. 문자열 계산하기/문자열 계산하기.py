def solution(my_string):
    f = my_string.split()
    
    sumv = int(f[0])
    for i in range(1,len(f),2):
        if f[i] == "+":
            sumv += int(f[i+1])
        else:
            sumv -= int(f[i+1])
        
    return sumv