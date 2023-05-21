import heapq
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [(-ind, val) for ind, val in enumerate(deliveries, start = 1) if val]
    pickups = [(-ind, val) for ind, val in enumerate(pickups, start = 1) if val]
    
    heapq.heapify(deliveries)
    heapq.heapify(pickups)
    
    while deliveries or pickups:
        delcapa = cap
        distance = 0
        while deliveries and delcapa:
            dis, boxes = heapq.heappop(deliveries)
            distance = max(distance, -dis)
            if boxes == delcapa:
                delcapa = 0
            elif boxes > delcapa:
                boxes -= delcapa
                heapq.heappush(deliveries, (dis, boxes))
                delcapa = 0
            else:
                delcapa -= boxes
                
        pickcapa = cap
        while pickups and pickcapa:
            dis, boxes = heapq.heappop(pickups)
            distance = max(distance, -dis)
            if boxes == pickcapa:
                pickcapa = 0
            elif boxes > pickcapa:
                boxes -= pickcapa
                heapq.heappush(pickups, (dis, boxes))
                pickcapa = 0
            else:
                pickcapa -= boxes
        answer += distance * 2
    return answer