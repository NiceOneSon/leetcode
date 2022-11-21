def solution(numlist, n):
    result = [[abs(n - val), val] for val in numlist]
    result.sort(key = lambda x : (x[0], -x[1]))
    return [x[1] for x in result]