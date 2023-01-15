import math

def getbinary(number):
    result = ''
    while number:
        result += str(number % 2)
        number //= 2
    return result[::-1]

def transform(number, ind): # return : (number, length)
    pos = ind + 1
    right_len = len(number) - pos + 1
    return '0' * (right_len - pos) + number, right_len - 1
    

def recur(number, mid, length):
    if number[mid] == '0' and (number[mid+length] == '1' or number[mid-length] == '1'):
        return True
    if length <= 1:
        return False
    
    result = False
    result |= recur(number, mid + length, length // 2)
    result |= recur(number, mid - length, length // 2)
    return result
    
def solution(numbers):
    answer = []
    for number in numbers:
        number = getbinary(number)
        result = False
        for ind in range(len(number)//2+1):
            if number[ind] == '1':
                (num, length) = transform(number, ind)
                if math.log(len(num) + 1, 2) % 1:
                    continue
                result |= not recur(num, length, length//2 + 1)
        if result:
            answer.append(1)
        else:
            answer.append(0)
    return answer