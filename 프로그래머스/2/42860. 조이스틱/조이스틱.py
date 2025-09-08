def solution(name):
    s = len(name) * "A"
    answer = 0
    
    for index in range(len(s)):
        if s[index] != name[index]:
            answer += min(abs(ord(s[index]) - ord(name[index])),abs(26 + ord(s[index]) - ord(name[index]))) 
            
        move = len(s) - 1
        for i in range(len(s)):
            j = i + 1
            while j < len(s) and name[j] == 'A':
                j += 1
            move = min(move, 2*i + len(s) - j, 2*(len(s) - j) + i)
    return answer + move    
            
                
            
        
        
        