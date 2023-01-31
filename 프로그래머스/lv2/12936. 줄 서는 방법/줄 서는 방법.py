from math import factorial


def solution(n, k):
    answer = []
    arr = list(range(1, n+1))
    while k > 1:
        for i in range(len(arr)):
            fact = factorial(len(arr)-1)
            if fact * i < k:
                ind = i
        answer.append(arr[ind])
        del arr[ind]
        k -= fact * ind
    else:
        return answer + arr
