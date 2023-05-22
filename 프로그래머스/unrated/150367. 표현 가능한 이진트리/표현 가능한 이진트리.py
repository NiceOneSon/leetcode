import math
def makeaTree(string):
    while math.log2(len(string) + 1) % 1 > 0:
        string = '0' + string
    return string

def check(string, left, right):
    mid = (left + right) // 2
    if len(string) <= 3:
        if len(string) == 1:
            return 1
        elif string[mid] == '1':
            return 1
        elif string == '000':
            return 0
        else:
            return -1
    left = check(string[left:mid], 0, mid)
    right = check(string[mid+1:right], 0, mid)
    if left == -1 or right == -1:
        return -1
    if left == 0 and right == 0 and string[mid] == '0':
        return 0
    if (left == 1 and string[mid] == '0') or (right == 1 and string[mid] == '0'):
        return -1
    if string[mid] == '0':
        return 0
    else:
        return 1
def solution(numbers):
    answer = []
    for number in numbers:
        string = bin(number)[2:]
        string = makeaTree(string)
        result = check(string, 0, len(string))
        if result != -1:
            answer.append(1)
        else:
            answer.append(0)
    return answer