import heapq
import sys

input = sys.stdin.readline

N = int(input())

routes = list(map(int, input().split(' ')))

routes.sort()
S, E = -1, 0
for num in routes:
    newS, newE = S + num, E + num
    if S == 0 and E == 0:
        S, E = newS, newE
        if S > 1:
            print(1)
            break
    elif newS > E :
        print(E+1)
        break
    else:
        E = newE
else:
    print(E+1)