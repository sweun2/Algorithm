n,m = map(int,input().split())

from collections import deque
queue = deque()

queue.append((n,0))

while queue:
    cur, cnt = queue.popleft()
    if cur == m:
        print(cnt+1)
        exit(0)
    if cur > m//2:
        continue
    
    queue.append((int(str(cur)+"1"),cnt + 1))
    queue.append((cur*2,cnt + 1))

print(-1)