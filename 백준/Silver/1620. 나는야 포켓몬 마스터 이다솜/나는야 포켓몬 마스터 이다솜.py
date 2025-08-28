from collections import defaultdict
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = defaultdict(int)
for i in range(n):
    s = input().strip()
    d[s] = i+1
    d[i+1] = s
for i in range(m):
    s = input().strip()
    if s[0].isdigit():
        print(d[int(s)])
    else:
        print(int(d[s]))