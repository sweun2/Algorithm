from itertools import permutations

def solution(k, dungeons):
    p = list(permutations(dungeons,len(dungeons)))
    maxv = 0
    for i in p:
        cur = k
        cnt = 0
        for j in i:
            if j[0]> cur:
                break
            cnt +=1
            cur -=j[1]
        maxv = max(maxv,cnt)
    return maxv
            
        
        
        
        