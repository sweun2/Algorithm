n = int(input())

d = {
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    "G":16,
    "H":17,
    "I":18,
    "J":19,
    "K":20,
    "L":21,
    "M":22,
    "N":23,
    "O":24,
    "P":25,
    "Q":26,
    "R":27,
    "S":28,
    "T":29,
    "U":30,
    "V":31,
    "W":32,
    "X":33,
    "Y":34,
    "Z":35,
}
rev = {i:(str(i) if i<10 else chr(ord('A')+i-10)) for i in range(36)}
sumv = 0
mult = [0 for i in range(36)]
for i in range(n):
    s = input()
    length = len(s)
    
    for j in range(len(s)):
        mult[d[s[j]]] += (35 - d[s[j]])* (36 ** (len(s)-1-j)) 
        sumv +=d[s[j]] * (36 ** (len(s)-1-j))

k = int(input())    
import heapq
hq = []
for i in range(36):
    heapq.heappush(hq,(-mult[i],i))

for _ in range(k):
    multi,i = heapq.heappop(hq)
    multi = -multi
    sumv += multi


if sumv == 0:
    print("0")
else:
    out = []
    while sumv > 0:
        out.append(rev[sumv % 36])
        sumv //= 36
    print(''.join(reversed(out)))