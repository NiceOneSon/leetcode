def solution(cap, n, deliveries, pickups):
    answer = 0
    # 가장 거리가 먼 집부터 완료해 나가야함.
    deliveries = [[ind, val] for ind, val in enumerate(deliveries, start = 1) if val > 0]
    pickups = [[ind, val] for ind, val in enumerate(pickups, start = 1) if val > 0]

    def delivery(capa, arr):
        result = 0
        while capa and arr:
            ind, val = arr.pop()
            result = max(result, ind)
            if val > capa:
                arr.append([ind, val - capa])
                break
            else:
                capa -= val
        return result
    
    while deliveries and pickups:
        ind1 = delivery(cap, deliveries)
        ind2 = delivery(cap, pickups)
        answer += (max(ind1, ind2) * 2)
        
    while deliveries:
        ind = delivery(cap, deliveries)
        answer += ind * 2
        
    while pickups:
        ind = delivery(cap, pickups)
        answer += ind * 2
    
        
    return answer