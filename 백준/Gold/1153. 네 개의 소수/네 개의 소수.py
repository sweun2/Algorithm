import math,sys
input = sys.stdin.readline

n = int(input())
if n < 8:
    print(-1)
    sys.exit()
    
def prime(s):
    result = [True for i in range(s+1)]
    
    for i in range(2,int(math.sqrt(s)+1)):
        cur = i * 2
        while cur <= s:
            result[cur] = False
            cur += i
            
    return [i for i in range(2,s+1) if result[i]]


r_list = prime(n- 4)

def fi():
    answer= []
    find = 0
    answer.append(2)
    if n%2 == 0:
        answer.append(2) 
        find = n-4
    else:
        answer.append(3)
        find = n-5

    for i in r_list:
        for j in r_list:
            if i+j == find:
                answer.extend([i,j])
                return answer
        
answer = fi()
if sum(answer) == n:
    print(*answer)
else:
    print(-1)
         