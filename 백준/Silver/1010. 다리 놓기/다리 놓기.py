t=int(input())

for i in range(0,t):
    temp = input()
    temp = temp.split(' ')
    west = int(temp[0])
    east = int(temp[1])

    if west==0 or east==0:
        print(0)
        continue

    n=1
    nk=1
    k=1
    for i in range(1,east+1):
        n=n*i
    for j in range(1,west+1):
        k=k*j
    for i in range(1,east-west+1):
        nk=nk*i

    result=n//(nk*k)
    print(result)