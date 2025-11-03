import math

n = int(input())
i = 2 ** math.ceil(math.log2(n))
m = i
cnt = 0
remain = n

while remain > 0:
    if m <= remain:
        remain -= m
    else:
        m //= 2
        cnt += 1

print(i, cnt)
