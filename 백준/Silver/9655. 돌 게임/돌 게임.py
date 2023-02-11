n = int(input())


DP = [False] * (max(n+1, 5))

ind = 4

DP[1] = True
DP[3] = True
while ind < n+1:
    if DP[ind-1] == False or DP[ind-3] == False:
        DP[ind] = True
    
    ind += 1
print('SK' if DP[n] else 'CY')