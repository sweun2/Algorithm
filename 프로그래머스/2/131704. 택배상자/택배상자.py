def solution(order):
    stack = []
    cur = 1
    idx = 0
    
    while cur <= len(order):
        if order[idx] == cur:
            idx += 1
            cur += 1
        elif stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
        else:
            stack.append(cur)
            cur += 1

    while stack and stack[-1] == order[idx]:
        stack.pop()
        idx += 1

    return idx
