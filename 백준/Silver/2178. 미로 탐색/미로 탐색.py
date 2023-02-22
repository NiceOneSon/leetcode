from collections import deque

R, C = map(int, input().split(' '))
routes = [list(map(int, list(input()))) for i in range(R)]
visited = [[False] * C for i in range(R)]
visited[0][0] = True
q = deque([(0,0,1)])
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
CONTROL = True
answer = float('inf')
while q and CONTROL:
    y, x, c = q.popleft()
    if c > answer:
        continue
    for i in range(4):
        sy, sx = y+dy[i], x+dx[i]
        if not 0<=sy<R or not 0<=sx<C:
            continue
        if visited[sy][sx]:
            continue
        if routes[sy][sx] == 0:
            continue
        visited[sy][sx] = True
        q.append((sy, sx, c+1))
        if sy == R-1 and sx == C-1:
            answer = min(answer, c+1)
print(answer)