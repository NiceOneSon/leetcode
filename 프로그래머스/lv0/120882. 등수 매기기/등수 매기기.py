def solution(score):
    avgs = [sum(sc) / 2 for sc in score]
    score[:] = avgs
    avgs.sort(reverse = True)
    return [avgs.index(avg) + 1 for avg in score]