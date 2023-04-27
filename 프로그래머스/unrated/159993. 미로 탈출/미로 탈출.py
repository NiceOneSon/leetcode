from collections import deque
# 문제 유형 : DP, BFS
# 최악의 경우 O(4**N)


def solution(maps):
    # init
    INF = float('inf')
    answer = 0
    row, col = len(maps), len(maps[0])
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    # get lever
    DP = [[INF] * col for _ in range(row)]
    q = deque()
        # find start point
    for y in range(row):
        for x in range(col):
            if maps[y][x] == 'S':
                break
        else:
            continue
        break
    q.append((y, x, 0))
    DP[y][x] = 0
    tmp1 = INF
    while q:
        y, x, cnt = q.popleft()
        # print(y, x)
        for i in range(4):
            sy, sx = y+dy[i], x+dx[i]
            if not(0<=sy<row and 0<=sx<col):
                continue
            elif DP[sy][sx] <= cnt + 1:
                continue
            elif maps[sy][sx] == 'X':
                continue
            elif maps[sy][sx] == 'L':
                tmp1 = min(tmp1, cnt + 1)
            DP[sy][sx] = cnt + 1
            q.append((sy, sx, cnt+1))
    
    
    # go to goal
    DP = [[INF] * col for _ in range(row)]
    q = deque()
        # find start point
    for y in range(row):
        for x in range(col):
            if maps[y][x] == 'L':
                break
        else:
            continue
        break
    q.append((y, x, 0))
    DP[y][x] = 0
    tmp2 = INF
    
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            sy, sx = y+dy[i], x+dx[i]
            if not(0<=sy<row and 0<=sx<col):
                continue
            elif DP[sy][sx] <= cnt + 1:
                continue
            elif maps[sy][sx] == 'X':
                continue
            elif maps[sy][sx] == 'E':
                tmp2 = min(tmp2, cnt + 1)
            DP[sy][sx] = cnt + 1
            q.append((sy, sx, cnt+1))
            
    answer = tmp1 + tmp2
    if answer == INF:
        return -1
    return answer