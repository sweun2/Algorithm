import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n - 1
minv = float("inf")
a, b = 0, 0

while left < right:
    s = arr[left] + arr[right]

    if abs(s) < minv:
        minv = abs(s)
        a, b = arr[left], arr[right]

    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break

print(a, b)
