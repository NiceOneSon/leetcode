from collections import deque

N = int(input())

routes = [input() for i in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def get_cnt(routes, hash = {
    'R' : 1,
    'G' : 2,
    'B' : 3
    }):
    visited = [[False] * N for i in range(N)]
    cnt = 0
    for iy in range(N):
        for ix in range(N):
            if visited[iy][ix]:
                continue
            cnt += 1
            y, x = iy, ix
            q = deque()
            q.append((y, x))
            while q:
                y, x = q.popleft()
                for i in range(4):
                    sy, sx = y+dy[i], x+dx[i]
                    if not 0<=sy<N or not 0<=sx<N:
                        continue
                    if visited[sy][sx]:
                        continue
                    if hash[routes[iy][ix]] == hash[routes[sy][sx]]:
                        visited[sy][sx] = True
                        q.append((sy, sx))
    return cnt
print(get_cnt(routes), get_cnt(routes, {'R' : 1, 'G' : 1, 'B' : 2}))