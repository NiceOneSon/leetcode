def rotate(routes):
    return list(map(lambda x : x[::-1], zip(*routes)))

def fitin(key, lock, cnt):
    miny, maxy, minx, maxx = -20, 21, -20, 21
    for y in range(miny, maxy):
        for x in range(minx, maxx):
            tmpcnt = cnt
            for i in range(len(key)):
                for j in range(len(key[0])):
                    if key[i][j] == 0:
                        continue
                    sy, sx = i + y, j + x
                    if not(0<=sy<len(lock) and 0<=sx<len(lock[0])):
                        continue
                    if lock[sy][sx] == 0:
                        tmpcnt -= 1
                    elif lock[sy][sx] == 1 and key[i][j] == 1:
                        tmpcnt = -1
                        
                    
            if tmpcnt == 0:
                return True
    return False
                    

def solution(key, lock):
    answer = False
    cnt = 0
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                cnt += 1
    
    answer |= fitin(key, lock, cnt)
    key = rotate(key)
    answer |= fitin(key, lock, cnt)
    key = rotate(key)
    answer |= fitin(key, lock, cnt)
    key = rotate(key)
    answer |= fitin(key, lock, cnt)
    
    return answer