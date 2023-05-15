N, M = map(int, input().split(' '))

routes = [tuple(input()) for _ in range(N)]

INF = float('inf')

DP = [[[INF, INF] for i in range(M)] for _ in range(N)]

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

from collections import deque

q = deque()

q.append((0, 0, 1, True)) # y, x, cnt, hammer

DP[0][0] = [0, 0]

while q:
    y, x, cnt, hammer = q.popleft()
    for i in range(4):
        sy, sx = y + dy[i], x + dx[i]
        if not(0<=sy<N and 0<=sx<M):
            continue
        if hammer:
            if routes[sy][sx] == '1':
                if DP[sy][sx][1] > cnt:
                    DP[sy][sx][1] = cnt
                    q.append((sy, sx, cnt + 1, False))
            else:
                if DP[sy][sx][0] > cnt:
                    DP[sy][sx][0] = cnt
                    q.append((sy, sx, cnt + 1, True))        
        else:
            if routes[sy][sx] == '0':
                if DP[sy][sx][1] > cnt:
                   DP[sy][sx][1] = cnt
                   q.append((sy, sx, cnt + 1, False))        

if min(DP[-1][-1]) == INF:
    print(-1)
else:
    print(min(DP[-1][-1]) + 1)