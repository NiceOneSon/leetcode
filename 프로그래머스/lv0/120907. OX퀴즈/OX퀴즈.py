def solution(quiz):
    result = []
    for q in quiz:
        eq = q.split(' ')
        left, oper = None, None 
        for ind in range(len(eq)-2):
            if ind % 2 == 0: # 숫자
                if left == None:
                    left = int(eq[ind])
                elif oper == '+':
                    left += int(eq[ind])
                elif oper == '-':
                    left -= int(eq[ind])
            else:
                oper = eq[ind]
        if left == int(eq[-1]):
            result.append('O')
        else:
            result.append('X')
                
                
    return result