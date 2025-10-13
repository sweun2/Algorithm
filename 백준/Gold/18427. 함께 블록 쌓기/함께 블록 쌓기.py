import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(H + 1):
        
        dp[i][j] += dp[i - 1][j]
        
        for h in blocks[i - 1]:
            if j - h >= 0:
                dp[i][j] += dp[i - 1][j - h]

print(dp[N][H] % 10007)
