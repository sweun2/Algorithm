n,r,c = map(int,input().split())

def di(length,r,c):
    #4di
    if 0<= r< length/2 and 0<= c< length/2:
        return 1
    elif length/2 <= r <length and 0<= c< length/2:
        return 3
    elif 0<= r< length/2 and length/2 <=c <length:
        return 2
    elif length/2 <=c <length and length/2 <=r <length:
        return 4

cnt = 0
while n>1:
    length = 2**n 
    
    d = di(length,r,c)
    cnt += length*length / 4 * (d-1)
    
    if r>= (length/2):
        r -= (length/2)
    if c>= (length/2):
        c -= (length/2)
    
    n-=1

if r:
    cnt +=1

print(int(cnt + r + c))
    