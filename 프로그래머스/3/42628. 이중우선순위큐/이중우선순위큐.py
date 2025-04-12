from collections import deque
import math
def solution(operations):
    queue = deque()
    
    for i in operations:
        if i[0] =="I":
            queue.append(int(i[1:].strip()))
        elif i == "D 1":
            max = -math.inf
            if queue:
                for j in queue:
                    if j> max:
                        max = j
                queue.remove(max)
        elif i == "D -1":
            min = math.inf
            if queue:
                for j in queue:
                    if j < min:
                        min = j
                queue.remove(min)
        
    max = -math.inf
    min = math.inf            
    if len(queue) == 0:
        return[0,0]
    else:
        for i in queue:
            if i > max:
                max = i
            if i < min:
                min = i
        return [max,min]   