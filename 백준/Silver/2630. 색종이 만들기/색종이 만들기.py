import sys
sys.setrecursionlimit(10**9)
n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))

color = [0,0]
def back(x1,y1,x2,y2):
    start = maps[x1][y1]
    flag = True
    for i in range(x1,x2):
        for j in range(y1,y2):
            if maps[i][j] != start:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        return start
    else:
        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2
        temp = back(x1, y1, mid_x, mid_y)
        if temp !=None:
            color[temp] +=1
        temp = back(x1, mid_y, mid_x, y2)
        if temp !=None:
            color[temp] +=1
        temp = back(mid_x, y1, x2, mid_y)
        if temp !=None:
            color[temp] +=1
        temp = back(mid_x, mid_y, x2, y2)
        if temp !=None:
            color[temp] +=1
           
v = back(0,0,n,n) 
if v != None:
    color[v] +=1

print(color[0])
print(color[1])