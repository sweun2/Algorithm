a,b,c,d,e,f = map(int,input().split())
x = (e*c-b*f)/(a*e-b*d)
y = (-1*d*c+a*f)/(a*e-b*d)
print(int(x),int(y))