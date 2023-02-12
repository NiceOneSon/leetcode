from collections import deque

def bfs(A, n, l, r):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    moved = True
    cnt = 0
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
                    s += A[x][y]
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if visited[nx][ny]:
                            continue
                        diff = abs(A[nx][ny] - A[x][y])
                        if diff >= l and diff <= r:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            moved = True
                avg = s // len(union)
                for x, y in union:
                    A[x][y] = avg
        if moved:
            cnt += 1
    return cnt

n, l, r = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
print(bfs(A, n, l, r))