from collections import deque, defaultdict
import heapq

T = int(input())
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)


def spread(now, q, hash):
    tmp = {}
    while q and q[0][0] == now:
        _, y, x = heapq.heappop(q)
        number = hash[(y, x)][0]
        for i in range(4):
            sy, sx = y+dy[i], x+dx[i]
            if (sy, sx) in hash:
                continue
            
            if (sy, sx) in tmp:
                tmp[(sy, sx)] = max(number, tmp[(sy, sx)])
            else:
                tmp[(sy, sx)] = number

    for (y, x), num in tmp.items():
        heapq.heappush(q, (now + num + 1, y, x))
        hash[(y, x)] = (num, now + num * 2)
    



for i in range(T):
    N, M, K = map(int, input().split(' '))
    
    hash = {}
    q = []
    
    for y in range(N):
        inserted = input().split(' ')
        if inserted[-1] == '':
            inserted = inserted[:-1]
        arr = list(map(int, inserted))
        for x in range(M):
            if arr[x] == 0:
                continue
            hash[(y, x)] = (arr[x], arr[x] * 2)
            heapq.heappush(q, (arr[x] + 1, y, x))
    now = 0
    while now < K:
        now += 1
        spread(now, q, hash)
        
    answer = 0
    for _, t in hash.values():
        if t > K:
            answer += 1
    print(f'#{i+1} {answer}')


