import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x,y = map(int,input().split())
    diff = y-x

    num = 0
    cnt = 1
    half = False
    result = 0
    while True:
        num += cnt
        result +=1
        if diff <= num:
            break
        if(half ==True):
            cnt +=1
        half = not half
    
    print(result)