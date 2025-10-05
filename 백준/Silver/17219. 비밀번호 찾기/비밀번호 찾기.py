n,m = map(int,input().split())
pw = dict()

for i in range(n):
    a,b = input().split()
    pw[a] = b
    
for j in range(m):
    h = input()
    print(pw[h])