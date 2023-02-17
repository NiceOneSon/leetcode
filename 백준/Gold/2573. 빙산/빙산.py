from collections import deque
N, M = map(int, input().split(' '))

routes = [list(map(int, input().split(' '))) for _ in range(N)]

dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs(routes):
    visited = [[False] * M for i in range(N)]
    cnt = 0 
    for iy in range(N):
        for ix in range(M):
            if visited[iy][ix] or routes[iy][ix] == 0:
                continue
            q = deque()
            q.append((iy, ix))
            visited[iy][ix] = True
            while q:
                y, x = q.popleft()
                for i in range(4):
                    sy, sx = y+dy[i], x+dx[i]
                    if not 0<=sy<N or not 0<=sx<M:
                        continue
                    if routes[sy][sx] == 0:
                        continue
                    if visited[sy][sx]:
                        continue
                    visited[sy][sx] = True
                    q.append((sy, sx))
            cnt += 1
    return cnt

def getnum(routes):
    answer = 100
    for y in range(N):
        for x in range(M):
            if routes[y][x] == 0:
                continue
            cnt = 0
            for i in range(4):
                sy, sx = y+dy[i], x+dx[i]
                if not 0<=sy<N or not 0<=sx<M:
                    continue
                if routes[sy][sx]:
                    continue
                cnt += 1
            if not cnt:
                continue
            answer = min(answer, routes[y][x] // cnt)
    return answer + 1

def flowtime(routes, num):
    tmproutes = [row[:] for row in routes]
    for y in range(N):
        for x in range(M):
            if routes[y][x] == 0:
                continue
            cnt = 0
            for i in range(4):
                sy, sx = y+dy[i], x+dx[i]
                if not 0<=sy<N or not 0<=sx<M:
                    continue
                if tmproutes[sy][sx] > 0:
                    continue
                cnt += 1
            routes[y][x] -= cnt # * num
            routes[y][x] = max(routes[y][x], 0)
result = bfs(routes)
answer = 0

while result == 1:
    num = 1
    flowtime(routes, num)
    result = bfs(routes)
    answer += 1
print(answer if result >= 2 else 0)