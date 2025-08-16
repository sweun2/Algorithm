n = int(input())

def conquer(n):
    if n == 1:
        return ["*"]
    
    pattern = conquer(n//3)
    s = list()
    for p in pattern:
        s.append(p * 3)
    
    for p in pattern:
        s.append(p + " " * (n // 3) + p)
        
    for p in pattern:
        s.append(p * 3)
         
    return s

result = conquer(n)
for i in result:
    print(i)