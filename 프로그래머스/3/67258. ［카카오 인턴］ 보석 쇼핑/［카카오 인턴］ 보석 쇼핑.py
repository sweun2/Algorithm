def solution(gems):
    kind = len(set(gems))
    dic = {}
    answer = [0, len(gems) - 1]
    
    left = 0
    
    for right in range(len(gems)):
        dic[gems[right]] = dic.get(gems[right], 0) + 1
        
        while len(dic) == kind:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                del dic[gems[left]]
            left += 1
    
    return [answer[0] + 1, answer[1] + 1]
