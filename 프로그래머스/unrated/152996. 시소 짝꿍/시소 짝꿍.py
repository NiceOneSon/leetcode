import math

def getscore(number):
    answer = 0
    while number > 1:
        number -= 1
        answer += number
    return answer

def solution(weights):
    answer = 0
    arr = [0 for i in range(4001)]
    toques = [0 for i in range(4001)]
    
    for weight in weights:
        arr[weight] += 1
    
    for weight in range(100, 1001):
        if not arr[weight]:
            continue
        answer += getscore(arr[weight])
        
        for dist in range(2, 5):
            toq = dist * weight
            answer += toques[toq] * arr[weight]
            toques[toq] += arr[weight]
            
    return answer
    
    