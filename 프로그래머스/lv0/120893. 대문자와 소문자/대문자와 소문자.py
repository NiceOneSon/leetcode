def solution(my_string):
    answer = []
    for string in my_string:
        if string == string.lower():
            answer.append(string.upper())
        else:
            answer.append(string.lower())
    return ''.join(answer)