def solution(n, k):
    if k - (n//10) > 0:
        return n * 12000 + (k - (n//10) ) * 2000
    else: return n * 12000