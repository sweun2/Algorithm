import sys
input = sys.stdin.readline
m = int(input())

s= [0] * 21
for i in range(m):
    li = input()
    a = li.split()
    
    if len(a) ==2:
        oper,x = a[0],int(a[1])
    else:
        oper = a[0]
        x = 0
        
    if oper == "add":
        s[x] = 1
    elif oper =="remove":
        if s[x] == 1:
            s[x] = 0
    elif oper =="check":
        print(s[x])
    elif oper =="toggle":
        if s[x]:
            s[x] = 0
        else:
            s[x] = 1
    elif oper =="all":
        s = [1] * 21
    else:
        s = [0] * 21
    