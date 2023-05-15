string = tuple(input())

bomb = tuple(input())

stack = []

def check(stack, bomb):
    for i in range(-1, -len(bomb)-1, -1):
        if stack[i] != bomb[i]:
            return False
    return True
        

for i in range(len(string)):
    stack.append(string[i])

    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        result = check(stack, bomb)
        if result:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
