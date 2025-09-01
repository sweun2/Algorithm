n = int(input())
arr = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    arr[i] = [0] + list(map(int,input().split()))

from itertools import combinations

combs = combinations(range(1,n+1),n//2)
result = 10**9
for comb in combs:
    teama = list(comb)
    teamb = [p for p in range(1,n+1) if p not in teama]
    ta = tb = 0
    for a, b in combinations(teama, 2):
        ta += arr[a][b] + arr[b][a]
    for a, b in combinations(teamb, 2):
        tb += arr[a][b] + arr[b][a]

    result = min(result, abs(ta - tb))

print(result)