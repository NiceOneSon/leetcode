from collections import deque

def move(board, i, y, x, dy, dx):
    while True:
        sy, sx = y+dy[i], x+dx[i]
        if not(0<=sy<len(board) and 0<=sx<len(board[0])):
            return y, x
        elif board[sy][sx] == 'D':
            return y, x 
        else:
            y, x = sy, sx
            
def solution(board):
    answer = 0
    row, col = len(board), len(board[0])
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    INF = float('inf')
    DP = [[INF] * col for _ in range(row)]
    
    board = [list(string) for string in board]
    
    for y in range(row):
        for x in range(col):
            if board[y][x] == 'R':
                break
        else:
            continue
        break
    q = deque()
    q.append((y, x, 0))
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            sy, sx = move(board, i, y, x, dy, dx)
            if DP[sy][sx] <= cnt + 1:
                continue
            q.append((sy, sx, cnt + 1))
            DP[sy][sx] = cnt + 1
            
    for y in range(row):
        for x in range(col):
            if board[y][x] == 'G':
                if DP[y][x] == INF:
                    return -1
                return DP[y][x]