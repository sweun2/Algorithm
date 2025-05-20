n = int(input())
import heapq

cup = []
for i in range(n):
    cup.append(tuple(map(int,input().split())))
cup.sort(reverse = True)

idx = 0
heap = []
result = 0
for day in range(n,0,-1):
    while idx < n and cup[idx][0] >= day:
        heapq.heappush(heap, -cup[idx][1])
        idx += 1
    if heap:
        result += -heapq.heappop(heap)

print(result)