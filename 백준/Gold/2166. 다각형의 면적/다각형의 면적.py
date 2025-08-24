import sys

input = sys.stdin.readline

n = int(input().strip())
pts = [tuple(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(n):
    x1, y1 = pts[i]
    x2, y2 = pts[(i + 1) % n]
    s += x1 * y2 - y1 * x2

area = abs(s) / 2.0
print(f"{area:.1f}")