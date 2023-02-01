
def solution(want, number, discount):
    def comparing(window, wants):
        return True if window == wants else False
        
    answer = 0
    wants = []
    for prod, num in zip(want, number):
        wants += [prod] * num
    wants.sort()
    for left in range(len(discount) - 9):
        window = sorted(discount[left:left+10])
        if comparing(window, wants):
            answer += 1
    return answer