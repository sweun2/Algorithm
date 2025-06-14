import math
from itertools import permutations

def prime(n):
    if n == 0 or n == 1:
        return False
    
    v = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i ==0:
            return False
    return True
            

def solution(numbers):
    num = list()
    for i in numbers:
        num.append(i)
    
    num.sort(reverse = True)
    result = prime(int("".join(num)))
    
    r = []
    cnt = 0
    for i in range(1,len(num)+1):
        r += permutations(num,i)
    
    ns = [int("".join(p)) for p in r]
    
    for i in list(set(ns)):
        if prime(i):
            cnt +=1
        
    return cnt