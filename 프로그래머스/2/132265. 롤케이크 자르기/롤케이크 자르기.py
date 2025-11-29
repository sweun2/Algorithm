def solution(topping):
    left = dict()
    right = dict()
    left[topping[0]] = 1
    
    for i in range(1, len(topping)):
        right[topping[i]] = right.get(topping[i], 0) + 1
    
    index = 0
    answer = 0
    while index < len(topping) - 1:
        if len(left.keys()) == len(right.keys()):
            answer += 1
        
        index += 1
        left[topping[index]] = left.get(topping[index], 0) + 1
        right[topping[index]] -= 1
        if right[topping[index]] == 0:
            del right[topping[index]]
    
    return answer
    
    
