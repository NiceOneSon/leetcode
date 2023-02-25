from collections import deque
T = int(input())
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def bomb(routes, x):
    tmp = [row[:] for row in routes]
    q = deque()
    for y in range(H):
        if tmp[y][x]:
            q.append((y, x, tmp[y][x]))
            tmp[y][x] = 0
            break

    while q:
        iy, ix, num = q.popleft()
        y, x = iy, ix
        for n in range(1, num):
            for i in range(4):
                sy, sx = y + (dy[i] *  n), x + (dx[i] *  n)
                if not 0<=sy<H or not 0<=sx<W:
                    continue
                
                elif tmp[sy][sx]:
                    q.append((sy, sx, tmp[sy][sx]))
                    tmp[sy][sx] = 0
    return tmp
                
def arrange(tmp):
    for x in range(W):
        left, right = H-2, H-1
        while left >= 0:
            if left >= right:
                left -= 1
            elif tmp[left][x] == 0:
                left -= 1
            elif tmp[right][x] != 0:
                right -= 1
            else:
                tmp[right][x] = tmp[left][x]
                tmp[left][x] = 0
                left -= 1
    return tmp

        


def dfs(routes, cnt):
    if cnt == N:
        result = 0
        for y in range(H):
            for x in range(W):
                if routes[y][x]:
                    result += 1
        return result
        
    
    answer = W*H
    for i in range(W):
        tmp = bomb(routes, i)
        newroutes= arrange(tmp)
        answer = min(answer, dfs(newroutes, cnt + 1))
    return answer

for t in range(1,T+1):
    N, W, H = map(int, input().split(' '))
    routes = []
    for i in range(H):
        string = input().split(' ')
        if string[-1] == '':
            string = string[:-1]
        routes.append(list(map(int, string)))
    result = dfs(routes, 0)
    print(f'#{t} {result}')
