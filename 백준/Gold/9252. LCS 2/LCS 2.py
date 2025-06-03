import sys
input = sys.stdin.readline

n = input().strip()
n_length = len(n)
m = input().strip()
m_length = len(m)

dp = [[0]*(len(n) + 1) for i in range(len(m) + 1)]

for i in range(1,len(m) + 1):
    for j in range(1,len(n) + 1):
        m_str = m[i-1]
        n_str = n[j-1]
        
        if m_str == n_str:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

row = n_length
col = m_length

result = ""
while True:
    if col == 0 or row == 0:
        break
    if n[row-1] == m[col - 1]:
        result = n[row-1] + result
        row -=1
        col -=1
    else:
        if dp[col][row-1]> dp[col-1][row]:
            row = row -1
        else:
            col = col-1
    

print(dp[m_length][n_length])
print(result)