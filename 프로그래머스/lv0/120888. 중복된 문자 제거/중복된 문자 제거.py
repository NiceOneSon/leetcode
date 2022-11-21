def solution(my_string):
    answer = ''
    hash = {}
    for string in my_string:
        if string in hash:
            continue
        hash[string]=True
        answer += string
    return answer