def getSelfNum(num):
    answer = num
    while num:
        one = num % 10
        answer += one
        num //= 10
    return answer

maxnum = 10000
routes = [False] * maxnum


for num in range(1, maxnum):
    nextnum = getSelfNum(num)
    if nextnum < maxnum:
        routes[nextnum] = True

    if routes[num]:
        continue
    print(num)
    
    
    
