from collections import deque

C, R = map(int, input().split(' '))

routes = [list(map(int, input().split(' '))) for i in range(R)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()

answer = 0 

for y in range(R):
    for x in range(C):
        if routes[y][x] == 1:
            q.append((y, x, 0))

while q:
    y, x, cnt = q.popleft()
    for i in range(4):
        sy, sx = y + dy[i], x + dx[i]
        if not 0<=sy<R or not 0<=sx<C:
            continue
        if routes[sy][sx]:
            continue
        q.append((sy, sx, cnt + 1))
        routes[sy][sx] = 1
    answer = max(answer, cnt)

chk = False
for y in range(R):
    for x in range(C):
        if routes[y][x] == 0:
            chk = True

if chk:
    print(-1)
else:
    print(answer)