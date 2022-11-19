def solution(ingredient):
    answer = 0
    stack = ingredient[:3]
    for ind in range(3, len(ingredient)):
        mat = ingredient[ind]
        stack.append(mat)
        if stack[-4:] == [1,2,3,1]:
            for i in range(4):
                stack.pop()
            answer += 1
        
    
    
    return answer