def solution(targets):
    answer = 0    
    targets.sort(key = lambda x : (x[0], x[1]))
    missile = targets[0]
    for s, e in targets[1:]:
        prevs, preve = missile
        if prevs <= s < preve:
            prevs = s
            preve = min(preve, e)
            missile = (prevs, preve)
            # print(s, e)
            continue
        else:
            missile = (s, e)
            answer += 1
    return answer + 1