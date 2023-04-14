dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
direction = {
    'N' : 0,
    'S' : 1,
    'W' : 2,
    'E' : 3
}

def solution(park, routes):
    answer = []
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == 'S':
                break
        else:
            continue
        break
                
    for route in routes:
        direct, num = route.split(' ')
        num = int(num)
        # CONTROL = True
        iy, ix = y, x
        i = direction[direct]
        while num:
            num -= 1
            sy, sx = y+dy[i], x+dx[i]
            if not(0<=sy<len(park) and 0<=sx<len(park[0])):
                break
            if park[sy][sx] == 'X':
                break
            y, x = sy, sx
        else:
            continue
        y, x = iy, ix
    return y, x