n = int(input())


DP = [False] * (max(n+1, 5))

ind = 4
# 1개 : 짐
# 2개 : 이김
# 3개 : 짐
# 4개 : 이김
# 5개 : 이김
# 6개 : 3 -> 
# 7개 : 이김
DP[2] = True
DP[4] = True
while ind < n+1:
    if DP[ind-1] == False or DP[ind-3] == False or DP[ind-4] == False:
        DP[ind] = True
    ind += 1
# print(DP)
print('SK' if DP[n] else 'CY')