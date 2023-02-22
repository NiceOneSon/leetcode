from collections import deque

R, C = map(int, input().split(' '))

routes = [list(map(int, input().split(' '))) for i in range(R)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def check_zero(routes):
    q = deque()
    visited = [[False] * C for i in range(R)]

    for x in range(C):
        if routes[0][x] == 0:
            q.append((0, x))
            visited[0][x] = True
        if routes[R-1][x] == 0:
            q.append((R-1, x))
            visited[R-1][x] = True

    for y in range(R):
        if routes[y][0] == 0:
            q.append((y, 0))
            visited[y][0] = True
        if routes[y][C-1] == 0:
            q.append((y, C-1))
            visited[y][C-1] = True

    while q:
        iy, ix = q.popleft()
        for i in range(4):
            sy, sx = iy+dy[i], ix+dx[i]
            if not 0<=sy<R or not 0<=sx<C:
                continue
            if routes[sy][sx] == 1:
                continue
            if visited[sy][sx]:
                continue
            visited[sy][sx] = True
            q.append((sy, sx))

    return visited

def overtime(routes, outside):
    tmp = [[False] * C for i in range(R)]
    cnt = 0
    for iy in range(R):
        for ix in range(C):
            y, x = iy, ix
            chk = False
            if routes[y][x] == 0:
                continue
            for i in range(4):
                sy, sx = y+dy[i], x+dx[i]
                if not 0<=sy<R or not 0<=sx<C:
                    continue
                if outside[sy][sx] == False:
                    continue
                if routes[sy][sx] == 0:
                    chk = True
                    break
            if chk:
                tmp[y][x] = True
    
    for y in range(R):
        for x in range(C):
            if tmp[y][x]:
                routes[y][x] = 0
            if routes[y][x]:
                cnt += 1
    return cnt

def print_routes(routes):
    for y in range(R):
        print(*routes[y])
    print(' ')

CONTROL = True
answer = sum([routes[y][x] for y in range(R) for x in range(C)])
cnt = 0
while CONTROL:
    cnt += 1
    visited = check_zero(routes)
    result = overtime(routes, visited)
    if result == 0:
        CONTROL = False
    else:
        answer = result
print(cnt)
print(answer)