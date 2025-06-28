import sys
input = sys.stdin.readline
n,m = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()

s = list()
def dfs(s:list):
    if len(s) == m:
        result = ""
        for i in s:
            result += str(i) + " "
        print(result.strip())
        return
    
    for number in numbers:
        if number not in s:
            s.append(number)
            dfs(s)
            s.remove(number)

dfs(s)
        