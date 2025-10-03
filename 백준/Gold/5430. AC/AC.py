t = int(input())

for _ in range(t):
    p = list(input())
    n = int(input())
    arr = input()[1:-1]
    if arr:
        arr = list(map(int,arr.split(",")))
    else:
        arr = list()
    err = False
    rev = False
    
    for oper in p:
        if oper =='D':
            if arr:
                err = False
                if rev:
                    arr.pop(-1)
                else:
                    arr.pop(0)
                    
            else:
                err = True
                break
        else:
            if not rev:
                rev = True
            else:
                rev = False
        
    if err:
        print("error")
    else:
        result = "["
        if rev:
            for i in arr[::-1]:
                result += str(i)
                result +=','
        else:
            for i in arr:
                result += str(i)
                result +=','
        if result != "[":
            result = result[:-1]
        result +="]"
        print(result)
                
    
    