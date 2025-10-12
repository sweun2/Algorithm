import sys
from collections import deque
import math
input = sys.stdin.readline

m, n = map(int, input().split())
arr = []
targets = []
for i in range(n):
    temp = input().strip() 
    for j, ch in enumerate(temp):
        if ch == 'C':
            targets.append((i, j))
    arr.append(list(temp))

(sx, sy), (tx, ty) = targets
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
INF = math.inf

dp = [[[INF] * 4 for _ in range(m)] for __ in range(n)]
queue = deque()

for d in range(4):
    dp[sx][sy][d] = 0
    queue.append((sx, sy, d))

minv = INF

while queue:
    x, y, d = queue.popleft()
    if (x, y) == (tx, ty):
        minv = min(minv, dp[x][y][d])
        continue

    for nd, (dx, dy) in enumerate(dirs):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m): continue
        if arr[nx][ny] == '*': continue

        add = 0 if d == nd else 1
        ncost = dp[x][y][d] + add

        if dp[nx][ny][nd] > ncost:
            dp[nx][ny][nd] = ncost
            if add == 0:
                queue.appendleft((nx, ny, nd))
            else:
                queue.append((nx, ny, nd))

print(min(dp[tx][ty]))
