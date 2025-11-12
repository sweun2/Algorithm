def solution(my_str, n):
    answer = []
    index = 0
    while index + n < len(my_str):
        answer.append(my_str[index:index+n])
        index += n
    
    answer.append(my_str[index:])
    return answer        