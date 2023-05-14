import sys
input = sys.stdin.readline

N = int(input())
INF = float('inf')

maxval, minval = None, None

for _ in range(N):
    row = list(map(int, input().split(' ')))
    row1 = row[:]
    row2 = row[:]
    if maxval == None:
        maxval = row
        minval = row
        continue
    
    row1[0] += max(maxval[0], maxval[1])
    row1[1] += max(maxval[0], maxval[1], maxval[2])
    row1[2] += max(maxval[1], maxval[2])

    row2[0] += min(minval[0], minval[1])
    row2[1] += min(minval[0], minval[1], minval[2])
    row2[2] += min(minval[1], minval[2])

    maxval = row1
    minval = row2
print(max(maxval), min(minval))