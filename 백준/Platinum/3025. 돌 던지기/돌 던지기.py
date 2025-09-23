row,col = map(int,input().split())

board = []
for i in range(row):
    board.append(list(input()))

from collections import deque
dp = [deque() for i in range(col)]
n = int(input())


for i in range(n):
    m = int(input()) - 1
    
    while dp[m] and board[dp[m][-1][0]][dp[m][-1][1]]=='O':
        dp[m].pop()
    if dp[m]:
        r, c = dp[m][-1]
    else:
        r, c = 0, m
        dp[m].append((r, c))
        
    while True:
        if r + 1 < row and board[r + 1][c] == '.':
            r += 1
            dp[m].append((r, c))
            continue
        if r + 1 == row or board[r + 1][c] == 'X':
            board[r][c] = 'O'
            dp[m].append((r,c))
            break
        
        if c - 1 >= 0 and board[r][c - 1] == '.' and board[r + 1][c - 1] == '.':
            c -= 1
            r += 1
            dp[m].append((r, c))
        elif c + 1 < col and board[r][c + 1] == '.' and board[r + 1][c + 1] == '.':
            c += 1
            r += 1
            dp[m].append((r, c))
        else:
            board[r][c] = 'O'
            dp[m].append((r,c))
            break
        
        

for i in range(row):
    for j in range(col):
        print(board[i][j],end="")
    print()