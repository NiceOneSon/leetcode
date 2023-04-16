import sys
input = sys.stdin.readline
T = int(input())
INF = float('inf')

def getDist(y2, x2, y1, x1):
    return ((y2-y1)**2 + (x2-x1)**2) ** 0.5

def vectorSum(vector1, vector2):
    y1, x1 = vector1
    y2, x2 = vector2
    return (y1+y2, x1+x2)

def dfs(hash, cnt, vector, p):
    if p > N:
        return INF
    elif cnt == N//2:
        y, x = vector
        sy, sx = totalSum
        sy = sy - y
        sx = sx - x
        return getDist(*vector, sy, sx)  
    
    answer = INF
    answer = min(answer, dfs(hash, cnt, vector, p+1))
    y, x = hash[p]
    sy, sx = vector
    sy += y
    sx += x
    answer = min(answer, dfs(hash, cnt+1, (sy, sx), p+1))
    return answer


for _ in range(T):
    N = int(input())
    hash = {}
    sy, sx = 0, 0
    for n in range(1, N+1):
        y, x = map(int, input().split(' '))
        hash[n] = (y, x)
        sy += y
        sx += x
    totalSum = (sy, sx)
    result = dfs(hash, 0, (0, 0), 1)
    print(result)