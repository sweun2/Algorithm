k=int(input())
queue=list(map(int, input().split()))
cnt=0
result=list()
for i in range(0,k):
    result.append(list())

def layer(_queue,_cnt,_result):
    if len(_queue)!=1:
        u=_queue[0:len(_queue)//2]
        v=_queue[len(_queue)//2+1:]
        _result[_cnt].extend([_queue[len(_queue)//2]])
        temp=_cnt+1
        layer(u,temp,_result)
        layer(v, temp, _result)
    else:
        _result[_cnt] .extend(_queue)

layer(queue,cnt,result)

for i in range(k):
    print(*result[i])