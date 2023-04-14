def solution(sequence, k):
    left = 0
    total = 0
    answer = []
    length = float('inf')
    for right in range(len(sequence)):
        total += sequence[right]
        while total > k:
            total -= sequence[left]
            left += 1
        if total == k and right - left < length:
            length = right - left
            answer = (left, right)
    
    return answer