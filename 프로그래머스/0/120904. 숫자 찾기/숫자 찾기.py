def solution(num, k):
    return str(num).find(str(k)) if str(num).find(str(k)) == -1 else str(num).find(str(k)) + 1