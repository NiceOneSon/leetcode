from collections import deque

M, N, H = map(int, input().split(' '))

routes = [] 
q = deque()

for i in range(H):
    tmp = [list(map(int, input().split(' '))) for j in range(N)]
    routes.append(tmp)

for z in range(H):
    for y in range(N):
        for x in range(M):
            if routes[z][y][x] == 1:
                q.append((z, y, x))

dy, dx, dz = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)

def get_day(routes):
    days = 0
    CONTROL = True
    q = deque()

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if routes[z][y][x] == 1:
                    q.append((z, y, x))

    while CONTROL:
        CONTROL = False
        tmp = deque()
        while q:
            iz, iy, ix = q.popleft()
            z, y, x = iz, iy, ix
            for i in range(6):
                sz, sy, sx = z+dz[i], y+dy[i], x+dx[i]
                if not 0<=sz<H or not 0<=sy<N or not 0<=sx<M:
                    continue
                if routes[sz][sy][sx] in (1, -1):
                    continue
                routes[sz][sy][sx] = 1
                tmp.append((sz, sy, sx))
                CONTROL = True
        if CONTROL:
            q = tmp
            days += 1
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if routes[z][y][x] == 0:
                    return -1
    return days


print(get_day(routes))