import sys
input = sys.stdin.readline

while True:
    arr_str = input().strip()
    if arr_str == '0':
        break
    arr = list(map(int,arr_str.split()))
    h = arr.pop(0)
    
    stack = list()
    maxv = 0
    start = 0
    for i in range(h):
        if not stack:
            stack.append((i,arr[i]))
            continue
        
        start = i
        while stack and stack[-1][1] > arr[i]:
            prev,height = stack.pop()
            maxv = max(maxv, (i-prev)*height)
            start = prev
        stack.append((start,arr[i]))
        
    while stack:
            prev,height = stack.pop()
            maxv = max(maxv, (i-prev +1)*height)
    print(maxv)