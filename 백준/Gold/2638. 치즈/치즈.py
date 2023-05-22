from collections import deque

N, M = map(int, input().split(' '))
routes = [list(map(int, input().split(' '))) for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def getVisited():
    visited = [[False] * M for _ in range(N)]
    return visited

def init():
    visited = getVisited()
    result = 0
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            sy, sx = y+dy[i], x+dx[i]
            if not(0<=sy<N and 0<=sx<M):
                continue
            if visited[sy][sx]:
                continue
            if routes[sy][sx] == 1:
                continue
            visited[sy][sx] = True
            q.append((sy, sx))
    
    for y in range(N):
        for x in range(M):
            if routes[y][x] == 1:
                result += 1
            if routes[y][x] == 0:
                if visited[y][x] == False:
                    routes[y][x] = - 1
    return result

def air():
    q = []
    for y in range(N):
        for x in range(M):
            if routes[y][x] == 1:
                cnt = 0
                for i in range(4):
                    sy, sx = y+dy[i], x+dx[i]
                    if routes[sy][sx] == 0:
                        cnt += 1
                else:
                    if cnt >= 2:
                        q.append((y, x))
                        
    answer = len(q)
    for y, x in q:
        routes[y][x] = 0
    return answer

def refresh():
    q = deque()
    q.append((0, 0))
    visited = getVisited()
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            sy, sx = y+dy[i], x+dx[i]
            if not(0<=sy<N and 0<=sx<M):
                continue
            if visited[sy][sx]:
                continue
            if routes[sy][sx] == 1:
                continue
            visited[sy][sx] = True
            routes[sy][sx] = 0
            q.append((sy, sx))
    


cnt_1 = init()
answer = 0
while 0 < cnt_1:
    answer += 1
    cnt = air()
    cnt_1 -= cnt
    refresh()
print(answer)