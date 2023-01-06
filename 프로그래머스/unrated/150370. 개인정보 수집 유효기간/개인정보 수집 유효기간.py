def solution(today, terms, privacies):
    def get_days(day):
        yy, mm, dd = map(int, day.split('.'))
        return yy * 28 * 12 + mm * 28 + dd
    
    contract = {}
    answer = []
    for term in terms:
        alpha, month = term.split(' ')
        days = int(month) * 28
        contract[alpha] = days
    
    today = get_days(today)
    for ind, privacy in enumerate(privacies, start = 1):
        check_day, alpha = privacy.split(' ')
        check_day = get_days(check_day)
        if contract[alpha] <= today - check_day:
            answer.append(ind)
        
    
    return answer