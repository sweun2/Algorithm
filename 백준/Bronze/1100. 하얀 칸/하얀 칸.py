arr=list()
for i in range(0,8):
    arr.append(input())

cnt=0
for i in range(0,8):
    for j in range(0,8):
        if (i+j)%2==0:
            if arr[i][j]=='F':
                cnt+=1

print(cnt)