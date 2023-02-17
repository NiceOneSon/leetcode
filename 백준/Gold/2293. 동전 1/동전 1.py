
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]
print(dp[k])
# 0 1 2 3 4 5 6 7 8 9 10
# 1 1 1 1 1 1 1 1 1 1 1
# 1 1 2 2 3 3 4 4 5 5 6
# 1 1 2 2 3 4 5 6 7 8 10