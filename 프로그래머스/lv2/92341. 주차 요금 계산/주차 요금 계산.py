from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    car = defaultdict(lambda : -1)
    carfee = defaultdict(int)
    
    def get_minutes(hh, mm):
        return 60 * hh + mm
    
    def get_fees(minutes):
        if minutes <= fees[0]:
            return fees[1]
        return fees[1] + (math.ceil((minutes - fees[0]) / fees[2]) * fees[3] )
    
    for record in records:
        time, carnum, status = record.split(' ')
        hh, mm = map(int, time.split(':'))
        minutes = get_minutes(hh, mm)
        if car[carnum] != -1:
            carfee[carnum] += minutes - car[carnum]
            car[carnum] = -1
        else:
            car[carnum] = minutes
    for carnum in car:
        if car[carnum] != -1:
            carfee[carnum] += get_minutes(23, 59) - car[carnum]
    
    return [get_fees(carfee[num]) for num in sorted(carfee.keys())]
    
    return answer