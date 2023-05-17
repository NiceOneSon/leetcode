
N, K = map(int, input().split(' '))
answer = 0

routes = list(map(int, input().split(' ')))
d = set()

def check(d, ind):
    tmp = set()
    for i in range(ind+1, K):
        if i >= K:
            break
        tmp.add(routes[i])
    # 앞으로 한 번도 사용하지 않는 거 1순위
    # 만일 모두 사용한다면 가장 마지막에 있는 게 2순위
    tmp = d - tmp
    if tmp:
        return tmp.pop()
    
    else:
        tmp_dic = {}
        for i in range(ind+1, K):
            if routes[i] not in tmp_dic:
                tmp_dic[routes[i]] = i

        maxind, result = None, None
        for num, ind in tmp_dic.items():
            if num in d:
                if maxind == None and result == None:
                    maxind = ind
                    result = num
                elif maxind < ind:
                    maxind = ind
                    result = num
        return result


            
                

answer = 0
for ind in range(len(routes)):
    num = routes[ind]

    if len(d) < N:
        d.add(num)

    elif num in d:
        continue

    else:
        result = check(d, ind)
        d.remove(result)
        d.add(num)
        answer += 1
    
print(answer)


