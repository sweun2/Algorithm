a=['G','A','C','T','T','A','C','C']
b=['C','A','C','G','T','C','C','A','C','C']

# a,b 중 길이가 긴 것을 x , 짧은 것을 y 대입
if len(a)<len(b):
    x=b
    m=len(b)
    y=a
    n = len(a)
else:
    x = a
    m = len(a)
    y = b
    n = len(b)


#기초 테이블 생성
table=[[0 for i in range(n+1)]for j in range(m+1)] # 테이블
minindex=[[(0,0)for j in range(0,n+1)]for i in range(0,m+1)] # 최적경로 배열
"""맨 끝 인덱스는 틈행, 틈열-> 가중치 2"""
for i in range(0,m+1):
    table[i][n]=2*(m-i)
for i in range(0,n+1):
    table[m][i]=2*(n-i)

for i in reversed(range(0,m)):
    for j in reversed(range(n)):
        if x[i]==y[j]:
            penalty=0
        else:
            penalty=1
        temp=min(table[i+1][j+1]+penalty,table[i+1][j]+2,table[i][j+1]+2)
        if temp==table[i+1][j+1]+penalty:
            minindex[i][j]=(i+1,j+1)
        elif temp==table[i+1][j]+2:
            minindex[i][j] = (i + 1, j )
        else:
            minindex(i , j+1 )
        table[i][j]=temp



""" 서열 구성"""
_x,_y=0,0
while(_x<m and _y<n):
    tx,ty=_x,_y
    print(minindex[_x][_y])
    _x,_y=minindex[_x][_y]
    if _x==tx+1 and _y==ty+1:
        print(x[tx]," ",y[ty])
    elif _x==tx and _y==ty+1:
        print(" - "," ",y[ty])
    else:
        print(x[tx]," "," - ")
