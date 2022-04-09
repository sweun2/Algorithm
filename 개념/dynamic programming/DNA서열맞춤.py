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



# 두번에 나눠서 테이블 채움
col=m
row=n-1

"""대각으로 좌하향 하는 인덱스 표현을 위한 col, row"""
while col-1 !=-1 : # col 이 최소가 될때까지 col -=1
    col-=1
    i=col
    j=row
    while  i!=m and j!=-1:
        if x[i] == y[j]:
            penalty = 0
        else:
            penalty = 1
        #table[i][j] = min(table[i + 1][j + 1] + penalty, table[i + 1][j] + 2, table[i][j + 1] + 2)

        """테이블 채울 때 minindex도 같이 채움"""
        temp=min(table[i + 1][j + 1] + penalty, table[i + 1][j] + 2, table[i][j + 1] + 2)
        if temp==table[i + 1][j + 1] + penalty:
            minindex[i][j]=i+1,j+1
            table[i][j]=temp
        elif temp==table[i + 1][j] + 2:
            minindex[i][j]=i+1,j
            table[i][j]=temp
        elif temp==table[i][j + 1] + 2:
            minindex[i][j]=i,j+1
            table[i][j] = temp
        """ 좌하향"""
        i+=1
        j-=1

"""col의 인덱스가 0이면 끝나므로 나머지 부분을 채움"""
while row-1 !=-1:
    row -=1
    i = col
    j = row
    while  j!= -1:
        if x[i] == y[j]:
            penalty = 0
        else:
            penalty = 1
        temp = min(table[i + 1][j + 1] + penalty, table[i + 1][j] + 2, table[i][j + 1] + 2)
        if temp == table[i + 1][j + 1] + penalty:
            minindex[i][j] = i + 1, j + 1
            table[i][j] = temp
        elif temp == table[i + 1][j] + 2:
            minindex[i][j] = i + 1, j
            table[i][j] = temp
        elif temp == table[i][j + 1] + 2:
            minindex[i][j] = i, j + 1
            table[i][j] = temp
        i += 1
        j -= 1

for i in table:
    print(*i)
for j in minindex:
    print(*j)



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

"""배열의 인덱스를 대각으로 접근해야 하는 줄 알고 개삽질함
걍 밑에서부터 하나씩 올라가면서 접근하면 끝나는 문제인데 """