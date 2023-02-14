N, K = map(int, input().split(' '))

routes = [[0] * (K+1) for i in range(N+1)]
stuffs = [(0, 0)]
DP = [0] * (K+1)
for i in range(N):
    w, v = map(int, input().split(' '))
    stuffs.append((w, v))

for i in range(1,N+1): # 물품 넘버
    weight, value = stuffs[i]
    for j in range(K+1): # 현재 무게
        if j < weight:
            routes[i][j] = routes[i-1][j]
        else:
            routes[i][j] = max(routes[i-1][j], routes[i-1][j - weight] + value)

print(routes[-1][-1])