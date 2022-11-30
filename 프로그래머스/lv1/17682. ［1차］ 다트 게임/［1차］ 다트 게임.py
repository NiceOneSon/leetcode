def solution(dartResult):
    answer = []
    tmpnum = 0
    for ind in range(len(dartResult)):
        string = dartResult[ind]
        if string in '0123456789':            
            if tmpnum:
                tmpnum *= 10
            tmpnum += int(string)
            # print(tmpnum)
        else:
            # print(answer, string, tmpnum)

            if string == 'S':
                answer += [tmpnum]
                # print(answer, tmpnum)
            elif string == 'D':
                tmpnum **= 2
                answer += [tmpnum]
            elif string == 'T':
                tmpnum **= 3
                answer += [tmpnum]
            tmpnum = 0

            if string == '#':
                answer[-1] *= -1
            elif string == '*': # string == '*'
                for subind in range(len(answer) - 2, len(answer)):
                    if subind < 0:
                        continue
                    answer[subind] *= 2
            
                
    return sum(answer)