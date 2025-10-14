from itertools import combinations

N = int(input())
board = [input().split() for _ in range(N)]

teachers = []
spaces = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    # 0: 위, 1: 아래, 2: 왼쪽, 3: 오른쪽
    while True:
        if direction == 0:
            x -= 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            y += 1

        if x < 0 or x >= N or y < 0 or y >= N:
            return False
        if board[x][y] == 'O':  
            return False
        if board[x][y] == 'S': 
            return True

def process():
    for x, y in teachers:
        for d in range(4):
            if watch(x, y, d):
                return True
    return False

found = False
for o in combinations(spaces, 3):
    for x, y in o:
        board[x][y] = 'O'
    if not process():
        found = True
        break
    for x, y in o:
        board[x][y] = 'X'

print("YES" if found else "NO")
