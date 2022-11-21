def solution(array):
    array = sorted([[val, ind] for ind, val in enumerate(array)])
    return array[-1]