N = int(input())
n = 1
line = 1
while n + (line + 1)< N:
    line += 1
    n += line

if n == N:
    print(f'{1}/{1}')
elif line % 2:
    den = line + 1
    num = 1
    cnt = N - n - 1
    den -= cnt
    num += cnt
    print(f'{num}/{den}')
else:
    den = 1
    num = line + 1
    cnt = N - n - 1
    den += cnt
    num -= cnt
    print(f'{num}/{den}')


