Target = int(input())
N = max(3, Target)
DP = [0] * (N+1)
DP[1] = 1
DP[2] = 2
for i in range(3, N+1):
    DP[i] = DP[i-1] + DP[i-2]
print(DP[Target]%10007)