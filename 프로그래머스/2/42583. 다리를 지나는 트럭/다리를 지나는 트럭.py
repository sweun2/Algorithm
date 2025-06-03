from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = len(truck_weights)
    truck_w = deque()
    for i in range(cnt):
        truck_w.append((truck_weights[i],i))
        
    time = 0
    td = dict()
    cur_pass = list()
    al_passed = list()
    
    while True:
        time +=1
                
        if len(al_passed) == cnt:
            return time
        
        sumv = 0
        for i,j in cur_pass:
            sumv += i
        
        if truck_w and truck_w[0][0] + sumv <= weight and len(cur_pass)< bridge_length:
            truck,index = truck_w.popleft()
            
            if td.get((truck,index)) == None:
                td[(truck,index)] = 0
                cur_pass.append((truck,index))
        to_remove = []
        for t in cur_pass:
            td[t] += 1
            if td[t] == bridge_length:
                to_remove.append(t)

        for t in to_remove:
            cur_pass.remove(t)
            al_passed.append(t)
