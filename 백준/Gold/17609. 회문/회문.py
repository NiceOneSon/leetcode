
T = int(input())

def check(string):
    left, right = 0, len(string)-1
    remainL = 0
    remainR = 0
    # 왼쪽을 뺀다
    while left < right:
        if string[left] != string[right]:
            remainL += 1
            left += 1
        else:
            left += 1
            right -= 1
    
    left, right = 0, len(string)-1
    while left < right:
        if string[left] != string[right]:
            remainR += 1
            right -= 1
        else:
            left += 1
            right -= 1
    
    return min(remainL, remainR, 2)
    



for _ in range(T):
    string = input()
    result = check(string)
    print(result)