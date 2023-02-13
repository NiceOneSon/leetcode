from collections import deque

row, col = map(int, input().split(' '))
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
routes = []
dupli = set()
for i in range(row):
    routes.append(list(input()))
    if 'R' in routes[-1]:
        redball = (i, routes[-1].index('R'))
        routes[i][redball[1]] = '.'
    if 'B' in routes[-1]:
        blueball = (i, routes[-1].index('B'))
        routes[i][blueball[1]] = '.'
    if 'O' in routes[-1]:
        target = (i, routes[-1].index('O'))
def move(y, x, i, othery, otherx):
    while 0<=y+dy[i]<row and 0<=x+dx[i]<col and routes[y + dy[i]][x + dx[i]] in ['.', 'O'] and not (y+dy[i] == othery and x+dx[i] == otherx):
        y = y + dy[i]
        x = x + dx[i]
        if routes[y][x] == 'O':
            return -1, -1, True
    return y, x, False

answer = 11
import time
q = deque([(redball, blueball, 0)])
while q:
    (iry, irx), (iby, ibx), cnt = q.popleft()
    dupli.add(((iry, irx), (iby, ibx)))
    if cnt >= answer:
        continue
    elif cnt > 10:
        continue

    for i in range(4):
        ry, rx = iry, irx
        by, bx = iby, ibx
        if i == 0:
            if ry > by:
                by, bx, b_achive = move(by, bx, i, ry, rx)
                ry, rx, r_achive = move(ry, rx, i, by, bx)
            else:
                ry, rx, r_achive = move(ry, rx, i, by, bx)
                by, bx, b_achive = move(by, bx, i, ry, rx)
        elif i == 1:
            if ry < by:
                by, bx, b_achive = move(by, bx, i, ry, rx)
                ry, rx, r_achive = move(ry, rx, i, by, bx)
            else:
                ry, rx, r_achive = move(ry, rx, i, by, bx)
                by, bx, b_achive = move(by, bx, i, ry, rx)
        elif i == 2:
            if rx > bx:
                by, bx, b_achive = move(by, bx, i, ry, rx)
                ry, rx, r_achive = move(ry, rx, i, by, bx)
            else:
                ry, rx, r_achive = move(ry, rx, i, by, bx)
                by, bx, b_achive = move(by, bx, i, ry, rx)
        else:
            if rx < bx:
                by, bx, b_achive = move(by, bx, i, ry, rx)
                ry, rx, r_achive = move(ry, rx, i, by, bx)
            else:
                ry, rx, r_achive = move(ry, rx, i, by, bx)
                by, bx, b_achive = move(by, bx, i, ry, rx)
        if b_achive:
            continue
        elif r_achive:
            answer = cnt+1
            continue
        elif ((ry, rx), (by, bx)) in dupli:
            continue
        q.append(((ry, rx), (by, bx), cnt+1))
print(answer if answer <= 10 else -1)