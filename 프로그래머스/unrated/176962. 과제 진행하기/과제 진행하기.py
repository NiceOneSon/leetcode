def string2time(string):
    if len(string) <= 3:
        return int(string)
    hh, mm = string.split(':')
    return int(hh) * 60 + int(mm)

def solution(plans):
    answer = []
    plans.sort(key = lambda x : string2time(x[1]))
    tmp = []
    for sub, time, duration in plans:
        time, duration = string2time(time), string2time(duration)
        if not tmp:
            now = time
            tmp.append((duration, sub))
        else:
            while tmp:
                pduration, psub = tmp.pop()
                if now + pduration > time:
                    tmp.append((now + pduration - time, psub))
                    break
                now += pduration
                answer.append(psub)
            now = max(now, time)
            tmp.append((duration, sub))
    while tmp:
        _, sub = tmp.pop()
        answer.append(sub)
    return answer