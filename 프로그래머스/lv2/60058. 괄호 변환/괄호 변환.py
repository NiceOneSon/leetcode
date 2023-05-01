

def balanced(p):
    cnt = 0 #1 if p[0] == '(' else -1
    correct = True if p[0] == '(' else False
    
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            
        if cnt == 0:
            return p[:i+1], p[i+1:], correct
        
            
    return p, '', correct

def solution(p):
    if p == '':
        return ''
    
    answer = ''
    u, v, correct = balanced(p)
    
    if correct:
        answer += u
        answer += solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        for string in u[1:-1]:
            if string == '(':
                tmp += ')'
            else:
                tmp += '('
        answer = answer + tmp
        
    return answer