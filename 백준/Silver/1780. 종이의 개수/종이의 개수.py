n = int(input())
arr = []*n
for i in range(n):
    arr.append(list(map(int,input().split())))


result = [0,0,0]

def add(start):
    if start == -1:
        result[0] +=1
    elif start == 0:
        result[1] +=1
    else:
        result[2] +=1
        
def divandcon(a,b,size):
    if size==1:
        add(arr[a][b])
        return 
    
    start = arr[a][b]
    flag = True
    for i in range(size):
        if flag:
            for j in range(size):
                if arr[a+i][b+j] != start:
                    flag = False
                    break
        else:
            break
    if flag:
        add(start)
    else:
        size = size//3
        
        for i in range(3):
            for j in range(3):
                divandcon(a+size*i,b+size*j,size)
        
                
divandcon(0,0,n)

for i in result:
    print(i)