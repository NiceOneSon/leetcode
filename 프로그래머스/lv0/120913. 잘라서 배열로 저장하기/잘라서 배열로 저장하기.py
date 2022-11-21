def solution(my_str, n):
    answer = []
    left, right = 0, n
    while left < len(my_str):
        answer.append(my_str[left:right])
        left = right
        right += n

    return answer