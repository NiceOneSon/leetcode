
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    calls = []
    for __ in range(N):
        numbers = input().strip()
        calls.append(numbers)
    calls.sort()
    for ind in range(1, len(calls)):
        prev, now = calls[ind-1], calls[ind]
        if prev == now[:len(prev)]:
            print('NO')
            break
    else:
        print('YES')