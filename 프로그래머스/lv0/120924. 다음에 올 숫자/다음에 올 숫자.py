def solution(common):
    answer = 0
    dngcha = True
    # dngbi = True
    for ind in range(2, len(common)):
        dngcha &= common[ind-1] - common[ind-2] == common[ind] - common[ind-1]
        # dngbi &= common[ind-1] / common[ind-2] == common[ind] / common[ind-1]
    if dngcha:
        return (2 * common[-1] - common[-2])
    return (common[-1] ** 2 / common[-2])