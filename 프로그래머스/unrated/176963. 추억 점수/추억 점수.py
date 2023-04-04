def solution(name, yearning, photos):
    hash = {}
    answer = []
    for _name, _score in zip(name, yearning):
        hash[_name] = _score
    
    for photo in photos:
        tmp = 0
        for _name in photo:
            if _name in hash:
                tmp += hash[_name]
        answer.append(tmp)
    
    return answer