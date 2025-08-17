import sys
sys.setrecursionlimit(10**9)

arr = []
row_used = [[False]*10 for _ in range(9)]
col_used = [[False]*10 for _ in range(9)]
box_used = [[False]*10 for _ in range(9)]


for i in range(9):
    arr.append(list(map(int,list(input()))))

def check(x,y):
    num = arr[x][y]
    dx = x // 3
    dy = y // 3
    for i in range(dx*3,dx*3 + 3):
        for j in range(dy*3,dy*3 + 3):
            if (i,j) != (x,y) and arr[i][j] == num:
                return False
    
    for j in range(9):
        if j != y and arr[x][j] == num:
            return False
        
    for i in range(9):
        if i != x and arr[i][y] == num:
            return False
        
    return True

blanks = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
for i in range(9):
    for j in range(9):
        num = arr[i][j]
        if num != 0:
            row_used[i][num] = True
            col_used[j][num] = True
            box_used[(i//3)*3 + (j//3)][num] = True
            
def dfs(depth):
    if depth == len(blanks):
        for row in arr:
            print(''.join(map(str, row)))
        sys.exit(0)

    x, y = blanks[depth]
    b = (x//3)*3 + (y//3)
    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[b][num]:
            arr[x][y] = num
            row_used[x][num] = col_used[y][num] = box_used[b][num] = True

            dfs(depth+1)

            arr[x][y] = 0
            row_used[x][num] = col_used[y][num] = box_used[b][num] = False

dfs(0)