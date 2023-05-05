R, C = map(int, input().split(' '))

routes = [list(input()) for _ in range(R)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
for y in range(R):
    for x in range(C):
        if routes[y][x] != 'S':
            continue
        for i in range(4):
            sy, sx = y+dy[i], x+dx[i]
            if not(0<=sy<R and 0<=sx<C):
                continue
            if routes[sy][sx] == 'W':
                print(0)
                break
            if routes[sy][sx] == '.':
                routes[sy][sx] = 'D'
        else:
            continue
        break
    else:
        continue
    break
else:
    print(1)
    for row in routes:
        print(''.join(row))
