def findMax(arr):
    cache = [None] * len(arr)
    # 1.
    cache[0] = arr[0]

    # 2.
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]

    return max(cache)

        
def solution(sequence):
    result = findMax([sequence[i] * (1 if i%2 else -1) for i in range(len(sequence))])
    result = max(result, findMax([sequence[i] * (-1 if i%2 else 1) for i in range(len(sequence))]))
    
    return result