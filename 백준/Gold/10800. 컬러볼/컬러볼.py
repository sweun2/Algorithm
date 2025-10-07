import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
color_sum = {}
for i in range(n):
    color, size = map(int, input().split())
    heapq.heappush(hq, (size, color, i))
    color_sum[color] = 0

total_sum = 0
result = [0] * n

prev_size = 0
same_size = []  

while hq:
    size, color, idx = heapq.heappop(hq)

    if prev_size != size:
        for s, c, _ in same_size:
            total_sum += s
            color_sum[c] += s
        same_size = []
        prev_size = size

    result[idx] = total_sum - color_sum[color]

    same_size.append((size, color, idx))

for s, c, _ in same_size:
    total_sum += s
    color_sum[c] += s

for r in result:
    print(r)
