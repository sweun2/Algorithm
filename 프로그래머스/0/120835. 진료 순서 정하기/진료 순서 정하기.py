from collections import deque
def solution(emergency):
    sorted_emg = sorted(emergency, reverse=True) 
    return [sorted_emg.index(x) + 1 for x in emergency]
    