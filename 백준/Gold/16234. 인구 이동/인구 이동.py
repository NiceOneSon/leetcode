from collections import deque

def bfs(routes, n, l, r):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    moved = True
    cnt = -1
    while moved:
        moved = False
        visited = [[False] * n for _ in range(n)]
        unions = []
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                union = []
                s = 0
                while q:
                    x, y = q.popleft()
                    union.append((x, y))
                    s += routes[x][y]
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if visited[nx][ny]:
                            continue
                        diff = abs(routes[nx][ny] - routes[x][y])
                        if diff >= l and diff <= r:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            moved = True
                avg = s // len(union)
                for x, y in union:
                    routes[x][y] = avg
        cnt += 1
    return cnt

n, l, r = map(int, input().split())
routes= []
for i in range(n):
    routes.append(list(map(int, input().split())))
print(bfs(routes, n, l, r))