import math
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
length = y - x + 1
is_square_free = [True] * length


for i in range(2, int(math.sqrt(y)) + 1):
    sq = i * i

    start = ((x + sq - 1) // sq) * sq
    for j in range(start, y + 1, sq):
        is_square_free[j - x] = False

print(sum(is_square_free))