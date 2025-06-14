n, a,b = map(int, input().split())
arr = [i for i in range(1,n+1)]

cnt = 0
flag = False
while True:
    temp = []
    while len(arr)>1:
        u = arr.pop(0)
        v = arr.pop(0)
        if (a,b) == (u,v) or (a,b) == (v,u):
            flag = True
            break
        
        if u == a or u == b:
            temp.append(u)
        elif v == a or v == b:
            temp.append(v)
        else:
            temp.append(u)
    if arr:
        temp.append(arr.pop())
    
    arr = temp[:]
    cnt +=1
    
    if flag:
        print(cnt)
        break
    
        