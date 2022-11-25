def solution(polynomial):
    poly = polynomial.split(' ')
    result = [0, 0]
    for element in poly:
        if element == '+':
            continue
        if element[-1] == 'x':
            element = element.replace('x', '')
            result[0] += int('1' if not element else element)
        else:
            result[1] += int(element)
            
    answer = ''
    if result[0]:
        if result[0] != 1:
            answer += '{}x'.format(result[0])
        else:
            answer += 'x'
    if result[1]:
        if answer:
            answer += ' + '
        answer += '{}'.format(result[1])
    return answer