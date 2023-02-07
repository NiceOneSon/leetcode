def extract(num):
    cnt = 0
    result = ''
    for i in range(len(num)):
        result += num[i]
        if result[-3:] == '110':
            result = result[:-3]
            cnt += 1
    return cnt, result

def find(num):
    ind = 0 
    for ind in range(len(num)):
        if num[ind:ind+2] == '11':
            return ind
        elif num[ind] == '1' and ind == (len(num) - 1):
            return ind
    return len(num)
            

def solution(s):
    answer = []
    for num in s:
        cnt, num = extract(num)
        ind = find(num)
        answer.append(num[:ind] + '110' * cnt + num[ind:])
    return answer