from collections import deque


def solution(maps):
    maps = list(
                map(lambda x : 
                    list(map(lambda y : int(y) if y != 'X' else y, list(x)))
                , maps)
               )
    
    answer = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * len(maps[0]) for i in range(len(maps))]
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != 'X' and visited[y][x] == False:
                q = deque([(y, x)])
                cnt = maps[y][x]
                visited[y][x] = True
                while q:
                    iy, ix= q.popleft()
                    for i in range(4):
                        sy, sx, = iy + dy[i], ix + dx[i]
                        if not (0 <= sy < len(maps)):
                            continue
                        if not (0 <= sx < len(maps[0])):
                            continue
                        if visited[sy][sx] or maps[sy][sx] == 'X':
                            continue
                        
                        visited[sy][sx] = True
                        q.append((sy, sx))
                        cnt += maps[sy][sx]
                answer.append(cnt)
    return sorted(answer) if answer else [-1]