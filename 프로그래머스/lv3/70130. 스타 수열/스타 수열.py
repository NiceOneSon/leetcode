from collections import Counter

def solution(a):
    answer = 0
    if len(a) == 1:
        return 0
    
    counter = Counter(a)
    for k in counter:
        v = counter[k]
        if v * 2 <= answer:
            continue
        ind = 0
        cnt = 0
        while ind < len(a) - 1:
            if (a[ind] != k and a[ind+1] != k) or a[ind] == a[ind+1]:
                ind += 1
                continue
            cnt += 2
            ind += 2
        else:
            answer = max(answer, cnt)
    return answer
            