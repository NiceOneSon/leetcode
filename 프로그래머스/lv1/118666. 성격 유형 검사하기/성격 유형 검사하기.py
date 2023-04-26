def solution(surveies, choices):
    answer = ''
    alphabet = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }
    
    for ind in range(len(surveies)):
        survey = surveies[ind]
        choice = choices[ind]
        # print(alphabet)
        if choice == 4:
            continue
        elif choice < 4:
            types = survey[0]
            alphabet[types] += 4 - choice
        else:
            types = survey[1]
            alphabet[types] += choice - 4
    # print(alphabet)
    for alphabets in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        a, b = alphabets
        if alphabet[a] >= alphabet[b]:
            answer += a
        else:
            answer += b
        
        
    return answer