#import sys
#input = sys.stdin.readline

T = int(input())

for i in range(1,T+1):
    N, K = map(int, input().split(' '))
    string = input().replace('\n', '')
    length = N // 4
    string = string + string[:length]
    s = set()
    for j in range(length, len(string)):
        s.add(string[j - length:j])
    arr = sorted(list(s), reverse = True)
    result = int(arr[K-1], 16)
    print(f'#{i} {result}')