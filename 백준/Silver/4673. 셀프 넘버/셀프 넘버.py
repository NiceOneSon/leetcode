n = 10000
DP = [False] * (n+1)
for num in range(1, n):
    ind = num
    while num:
        rest = num % 10
        ind += rest
        num //= 10
    if ind < 10000:
        DP[ind] = True

for i in range(1, 10000):
    if DP[i] == False:
        print(i)