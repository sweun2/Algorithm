import sys
import math
from itertools import combinations

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    total_x = sum(x for x, _ in points)
    total_y = sum(y for _, y in points)
    
    min_val = math.inf
    
    for comb in combinations(range(n), n // 2):

        sx = 0
        sy = 0
        for idx in comb:
            sx += points[idx][0]   # 선택한 점들의 x좌표 합
            sy += points[idx][1]   # 선택한 점들의 y좌표 합
        
        vx = 2 * sx - total_x
        vy = 2 * sy - total_y
        
        length = math.sqrt(vx * vx + vy * vy)
        
        if length < min_val:
            min_val = length
    
    print(min_val)
