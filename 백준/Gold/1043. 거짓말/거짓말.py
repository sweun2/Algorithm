n, m = map(int, input().split())
know = input().split()

if know[0] == '0':
    know = []
else:
    know = list(map(int, know[1:]))
parties = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(set(party))

true_set = set(know)

changed = True
while changed:
    changed = False
    for p in parties:
        if p & true_set:
            if not p <= true_set:
                true_set |= p
                changed = True

result = 0
for p in parties:
    if not (p & true_set):
        result += 1

print(result)
