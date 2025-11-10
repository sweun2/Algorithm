def solution(quiz):
    result = []
    for q in quiz:
        arr = q.split()
        if arr[1] == "-":
            sumv = int(arr[0]) - int(arr[2])
            if sumv == int(arr[-1]):
                result.append("O")
            else:
                result.append("X")
        else:
            sumv = int(arr[0]) + int(arr[2])
            if sumv == int(arr[-1]):
                result.append("O")
            else:
                result.append("X")
    return result            
                