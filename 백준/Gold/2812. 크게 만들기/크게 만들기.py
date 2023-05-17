N, K = map(int, input().split(' '))
# N : total length
# K : the number of what should be removed
string = input()
stack = []

for i in range(len(string)):
    if K == 0:
        stack.append(string[i])
    else:
        if not stack:
            stack.append(string[i])
        else:
            while stack and int(stack[-1]) < int(string[i]) and K:
                stack.pop()
                K -= 1
            else:
                stack.append(string[i])
while stack and K:
    stack.pop()
    K -= 1
print(int(''.join(stack)))