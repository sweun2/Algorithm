import sys
input = sys.stdin.readline
n = int(input())

numbers= [[]for i in range(4)]

for i in range(n):
    a,b,c,d = map(int,input().split())
    numbers[0].append(a)
    numbers[1].append(b)
    numbers[2].append(c)
    numbers[3].append(d)

from collections import defaultdict

dic = defaultdict(int)

for a in numbers[0]:
    for b in numbers[1]:
        dic[a+b] +=1
cnt = 0
for c in numbers[2]:
    for d in numbers[3]:
        t = -(c+d)
        
        if t in dic:
            cnt += dic[t]

print(cnt) 
