import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

stack = set([(0, 0, board[0][0])])
maxLen = 0

dir = [(0,1), (1,0), (-1,0), (0, -1)]
while stack:
    i, j, visited = stack.pop()

    if maxLen < len(visited):
        maxLen = len(visited)
        if maxLen == 26 or maxLen == R*C:
            break
    
    for di, dj in dir:
        ni, nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and not board[ni][nj] in visited:
            stack.add((ni, nj, visited+board[ni][nj]))
print(maxLen)