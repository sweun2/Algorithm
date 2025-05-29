import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

def fib(n):
    if n ==0 :
        return 0 
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fib(n-1) + fib(n-2)

print(fib(n))