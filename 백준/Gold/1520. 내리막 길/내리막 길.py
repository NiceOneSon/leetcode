N, M = map(int, input().split(' '))
routes = [list(map(int, input().split(' '))) for _ in range(N)]
DP = [[-1] * M for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def dfs(y, x):
    if y == N-1 and x == M-1:
        return 1
    
    if DP[y][x] != -1:
        return DP[y][x]
    
    DP[y][x] = 0

    for i in range(4):
        sy, sx = y+dy[i], x+dx[i]
        if not(0<=sy<N and 0<=sx<M):
            continue
        if routes[sy][sx] >= routes[y][x]:
            continue
        DP[y][x] += dfs(sy, sx)

    return DP[y][x]
print(dfs(0, 0))
