def solution(board, skill):
    n = len(board)
    m = len(board[0])
    d = [[0 for i in range(len(board[0]) + 1)] for i in range(len(board)+1)]

    for t,r1, c1, r2, c2, degree in skill:
        if t == 1:
            k = -1
        else:
            k = 1
        d[r1][c1] += degree * k
        d[r2+1][c1] -= degree * k
        d[r1][c2+1] -= degree * k
        d[r2+1][c2+1] += degree * k

    for i in range(0,n+1):
        for j in range(1,m+1):
            d[i][j] = d[i][j-1] + d[i][j]
    for i in range(0,m+1):
        for j in range(1,n+1):
            d[j][i] = d[j-1][i] + d[j][i]
            
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = board[i][j] + d[i][j]
    cnt = 0
    for i in result:
        for j in i:
            if j>0:
                cnt +=1
    return cnt        