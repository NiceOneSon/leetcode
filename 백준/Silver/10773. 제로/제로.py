N = int(input())
stack = []
for _  in range(N):
    num = int(input())
    if num == 0 and stack:
        stack.pop()
        continue
    stack.append(num)
print(sum(stack))