n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]

chicken = list()
house = list()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            house.append((i,j))

answer = float('inf')
selected = []

def get_distance():
    total = 0
    for hx,hy in house:
        dist = float('inf')
        for cx,cy in selected:
            dist = min(abs(cx-hx) + abs(cy-hy),dist)
        total += dist
    return total

def back(depth,start):
    global answer
    if depth == m:
        answer = min(answer,get_distance())
        return
    
    for i in range(start,len(chicken)):
        selected.append(chicken[i])
        back(depth+1, i+1)
        selected.pop()
        
        
        
        
back(0,0)
print(answer)
