def get_min(t):
        hh, mm = map(int, t.split(':'))
        return hh * 60 + mm
    
def solution(book_time):
    answer = 0
    DP = [0] * (60 * 25)
    for f, t in book_time:
        f = get_min(f)
        t = get_min(t)
        print(f, t)
        for time in range(f, t+10):
            DP[time] += 1
        
    return max(DP)