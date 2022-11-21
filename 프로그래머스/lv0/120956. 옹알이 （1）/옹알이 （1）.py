def solution(babbling):
    checklist = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babb in babbling:
        left = 0
        prev = ''
        for right in range(1, len(babb)+1):
            if babb[left:right] in checklist:
                if prev == babb[left:right] :
                    break
                left = right
                prev = babb[left:right] 
        else:
            if left == right:
                answer += 1    
    return answer