def solution(n, build_frame):
    answer = []
    def check():
        pillar = 0
        beam = 1
        for x, y, prod in answer:
            if prod == pillar:
                if y == 0 or [x-1, y, beam] in answer or [x, y, beam] in answer or [x, y-1, pillar] in answer:
                    continue
                else:
                    return False
            else:
                if [x, y-1, pillar] in answer or [x+1, y-1, pillar] in answer or ([x-1, y, beam] in answer and [x+1, y, beam] in answer):
                    continue
                return False
        return True
    
    for x, y, prod, act in build_frame:
        if act == 1:
            # print(1, x,y,prod,act)
            # print(check())
            answer.append([x, y, prod])
            if not check():
                answer.remove([x, y, prod])
        else:
            answer.remove([x, y, prod])
            if not check():
                
                answer.append([x, y, prod])
                
    return sorted(answer)