def solution(array, n):
    array.sort()
    
    answer = float('inf')
    
    for arr in array:
        if abs(answer - n) > abs(arr - n):
            answer = arr
    return answer