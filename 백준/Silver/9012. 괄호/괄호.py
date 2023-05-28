N = int(input())

def check(string):
    cnt = 0
    for s in string:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    return False

for _ in range(N):
    string = input()
    result = check(string)
    print('YES' if result else 'NO')