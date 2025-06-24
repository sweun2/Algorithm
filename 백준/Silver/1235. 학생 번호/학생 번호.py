n = int(input())
stduent = []
for i in range(n):
    stduent.append(input())

length= len(stduent[0])

for i in range(-1,-length-1,-1):
    flag = False
    visit = set()
    for st in stduent:
        if st[i:] not in visit:
            visit.add(st[i:])
        else:
            flag = True
            break
    
    if not flag:
        print(-i)
        break