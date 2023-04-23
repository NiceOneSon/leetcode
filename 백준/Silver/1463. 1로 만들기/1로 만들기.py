N = int(input())
DP = [0] * (N+1)
DP[N] = 1

for i in range(N, -1, -1):
    if DP[i] == 0:
        continue
    
    if i % 3 == 0:
        if DP[i//3] == 0:
            DP[i//3] = DP[i] + 1
        else:
            DP[i//3] = min(DP[i//3], DP[i] + 1)

    if i % 2 == 0:
        if DP[i//2] == 0:
            DP[i//2] = DP[i] + 1
        else:
            DP[i//2] = min(DP[i//2], DP[i] + 1)
    
    if i-1 >= 0:
        if DP[i-1]:
            DP[i-1] = min(DP[i-1], DP[i] + 1)
        else:
            DP[i-1] = DP[i] + 1
print(DP[1]-1)