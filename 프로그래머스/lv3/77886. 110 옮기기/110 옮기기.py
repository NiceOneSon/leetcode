def extract(num):
    stack = ''
    tmp = 0
    for i in range(len(num)):
        stack += num[i]
        if len(stack) >= 3 and stack[-3:] == '110':
            stack = stack[:-3]
            tmp += 1
    return stack, tmp

def load(num, tmp):
    for i in range(len(num)):
        if num[i:i+2] == '11': # 앞
            return num[:i] + '110' * tmp + num[i:]
        elif num[i] == '1' and i == (len(num) - 1): # 앞
            return num[:i] + '110' * tmp + num[i:]
        elif num[i:i+3] == '011': # 사이
            return num[:i+1] + '110' * tmp + num[i+1:]
    # 뒤
    return num + '110' * tmp
            
    
        
def solution(numbers):
    answer = []
    for num in numbers:
        if len(num) < 3:
            answer.append(num)
            continue
        num, tmp = extract(num)
        num = load(num, tmp)
        answer.append(num)
        
    return answer