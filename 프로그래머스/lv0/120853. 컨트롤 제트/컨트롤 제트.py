def solution(s):
    stack = []
    s = s.split(' ')
    for string in s:
        if string == 'Z':
            if stack:
                stack.pop()
            else:
                continue
        else:
            stack.append(int(string))
    return sum(stack)