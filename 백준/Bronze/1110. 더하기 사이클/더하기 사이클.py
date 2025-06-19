k = input()
if len(k) == 1:
    k += "0"


n = k
cnt = 0
while True:
    re = int(n[0]) + int(n[1])  
    n = n[1] + str(re)[-1]
    
    cnt +=1
    
    if n == k:
        break

print(cnt)