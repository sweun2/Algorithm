def solution(lines):
    arr = [0] * 201  
    
    for start, end in lines:
        for i in range(start, end):  
            arr[i + 100] += 1  
    
    return sum(1 for x in arr if x >= 2)