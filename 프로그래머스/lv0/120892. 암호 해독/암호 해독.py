def solution(cipher, code):
    answer = ''
    for ind, c in enumerate(cipher, start = 1):
        if ind % code == 0:
            answer += c
    return answer