# 7 8 2
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0
R, C, T = map(int, input().split(' '))
routes = [list(map(int, input().split(' '))) for i in range(R)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
ldy, ldx = [1, 0, -1, 0], [0, 1, 0, -1]

for y in range(R):
    if routes[y][0] == -1:
        conditioner = (y, 0)
        break            

def distributed(routes):
    tmp = [[0] * C for i in range(R)]
    for y in range(R):
        for x in range(C):
            if routes[y][x] <= 0:
                continue
            amount = routes[y][x] // 5
            cnt = 0
            for i in range(4):
                sy, sx = y+dy[i], x+dx[i]
                if not 0<=sy<R or not 0<=sx<C:
                    continue
                if routes[sy][sx] == -1:
                    continue
                tmp[sy][sx] += amount
                cnt += 1
            tmp[y][x] -= cnt * amount

    for y in range(R):
        for x in range(C):
            routes[y][x] += tmp[y][x]

def ventilation(routes):
    # upper
    iy, ix = conditioner
    y, x = iy, ix
    ind = 0
    sy, sx = y+dy[ind], x+dx[ind]
    while sy != iy or sx != ix:
        routes[y][x] = routes[sy][sx]
        routes[sy][sx] = 0
        y, x = sy, sx
        if not 0<=y+dy[ind]<=iy or not 0<=x+dx[ind]<C:
            ind += 1
        sy, sx = y+dy[ind], x+dx[ind]
    # lower
    iy, ix = conditioner
    iy += 1
    y, x = iy, ix
    ind = 0
    sy, sx = y+ldy[ind], x+ldx[ind]
    while sy != iy or sx != ix:
        routes[y][x] = routes[sy][sx]
        routes[sy][sx] = 0
        y, x = sy, sx
        if not iy<=y+ldy[ind]<R or not 0<=x+ldx[ind]<C:
            ind += 1
        sy, sx = y+ldy[ind], x+ldx[ind]
    y, x = conditioner
    routes[y][x] = -1
    routes[y+1][x] = -1

def count_finedust(routes):
    cnt = 0 
    for y in range(R):
        for x in range(C):
            if routes[y][x] == -1:
                continue
            cnt += routes[y][x]
    return cnt

for i in range(T):
    distributed(routes)
    ventilation(routes)

print(count_finedust(routes))

