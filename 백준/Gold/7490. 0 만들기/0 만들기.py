T = int(input())

def getnum(string):
    string = string.replace(' ', '')
    tmp = []
    for s in string:
        if '0' <= s <= '9':
            if tmp and '0' <= tmp[-1] <= '9':
                tmp[-1] = tmp[-1] + s
                continue
        tmp.append(s)
    string = tmp
    
    answer = 0
    right = None
    oper = None
    for i in range(len(string)):
        s = string[i]
        if i % 2:
            oper = s
        else:
            if not oper:
                answer = int(s)
            else:
                right = int(s)
                if oper == '+':
                    answer += right
                else:
                    answer -= right
    return answer

def recur(num, string):
    global answer
    if num == N+1:
        result = getnum(string)
        if result == 0:
            return string
        return None
    
    res1 = recur(num + 1, string + f'+{num}')
    res2 = recur(num + 1, string + f' {num}')
    res3 = recur(num + 1, string + f'-{num}')
    if res1:
        answer.append(res1)
    if res2:
        answer.append(res2)
    if res3:
        answer.append(res3)


for i in range(T):
    N = int(input())
    answer = []
    recur(2, '1')
    answer.sort()
    for string in answer:
        print(string)
    else:
        print(' ')
        
