def solution(m, n, puddles):
    maps = [[1 for i in range(m+1)] for i in range(n+1)]
    
    for puddle in puddles:
        x,y = puddle[1], puddle[0]
        
        maps[x][y] = 0
        
    flag = False    
    for i in range(1,n+1):
        if maps[i][1] == 0:
            flag = True
            continue
        if flag:
            maps[i][1] = 0
        else:
            maps[i][1] = 1
    
    flag = False    
    for i in range(1,m+1):
        if maps[1][i] == 0:
            flag = True
            continue
        if flag:
            maps[1][i] = 0
        else:
            maps[1][i] = 1
                
    
    for i in range(2,n+1):
        for j in range(2,m+1):
            if maps[i][j] == 0:
                continue
            
            maps[i][j] = maps[i-1][j] + maps[i][j-1]

    return maps[n][m]%1000000007
