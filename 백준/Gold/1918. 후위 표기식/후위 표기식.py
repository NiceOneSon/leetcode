

string = input()
answer = []
stack = []

def recur(string):
    for i in range(len(string)):
        word = string[i]
        if 'A' <= word <= 'Z':
            answer.append(word)
        
        elif word in ('+', '-'):
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.append(word)

        elif word in ('*', '/'):
            while stack and stack[-1] in ('*', '/'):
                answer.append(stack.pop())
            stack.append(word)
        
        elif word == '(':
            stack.append(word)
        
        elif word == ')':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            else:
                stack.pop()
    
    while stack:
        answer.append(stack.pop())
recur(string)
print(''.join(answer))
        
