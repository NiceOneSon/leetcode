N, L = map(int, input().split(' '))

routes = [list(map(int, input().split(' '))) for _ in range(N)]

def check(path, L):
    cnt = 1
    prev = path[0]
    ind = 1
    front = False
    while ind < N:
        num = path[ind]
        if not front:
            if prev == num:
                cnt += 1
            elif prev + 1 == num:
                if cnt < L:
                    return False
                else: # cnt >= L
                    cnt = 1
                    prev = num
            elif prev == num + 1:
                cnt = 1
                prev = num
                if cnt != L:
                    front = True
                else:
                    cnt = 0
                
            else:
                return False
            
        else:
            if prev == num:
                cnt += 1
                if cnt >= L:
                    cnt = 0
                    front = False
            else:
                return False
        ind += 1
    if front and cnt < L:
        return False
    return True

            
    # 이전 숫자가 없다면
        # 이전 숫자 = 현재 숫자
    # 이전 숫자보다 현재 숫자가 크다면
        # 이전 숫자의 개수가 L 이상이여야 통과
        # 이하라면 return False
    # 이전 숫자보다 현재 숫자가 작다면
        # 앞으로 나올 숫자를 세야함.
        # 앞으로 나올 숫자가 L 이상이다 통과
        # 이하라면 return False
answer = 0
for i in range(N):
    if check(routes[i], L):
        # print('row', i)
        answer += 1

routes = list(zip(*routes))
for i in range(N):
    if check(routes[i], L):
        # print('col', i)
        answer += 1
print(answer)

# 10 2
# 2 2 3 5 3 1 1 1 1 1
# 2 2 3 5 3 1 1 1 1 1
# 3 3 4 5 4 3 2 1 1 2
# 3 3 4 5 4 3 2 1 1 2
# 5 5 5 5 5 5 3 1 1 3
# 4 4 4 5 5 5 4 3 3 3
# 4 4 4 5 5 5 5 5 5 3
# 4 4 4 4 4 5 5 5 5 3
# 4 4 4 4 4 5 5 5 5 3
# 5 5 4 4 4 5 5 5 5 4