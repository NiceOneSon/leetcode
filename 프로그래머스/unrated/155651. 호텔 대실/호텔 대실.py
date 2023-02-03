def get_min(t):
        hh, mm = map(int, t.split(':'))
        return hh * 60 + mm
    
def solution(book_time):
    answer = 0
    DP = [0] * (60 * 25)
    for f, t in book_time:
        f = get_min(f)
        t = get_min(t)
        DP[f] += 1
        DP[t+10] -= 1
    tmp = 0
    for ind in range(len(DP)):
        tmp += DP[ind]
        answer = max(answer, tmp)
    return answer