import heapq

def solution(food_times, k):
    length = len(food_times)
    q = [(val, ind) for ind, val in enumerate(food_times)]
    heapq.heapify(q)
    DP = [False] * length
    looped = 0
    while q:
        val, ind = heapq.heappop(q)
        tmp = [ind]
        while q and q[0][0] == val:
            val, ind = heapq.heappop(q)
            tmp.append(ind)
        val -= looped
        cnt = len(tmp)
        if k - length * val < 0:
            k %= length
            i = 0
            k += 1
            while i < len(DP) and k:
                check = DP[i]    
                if check:
                    i += 1
                    continue
                k -= 1
                i += 1
            else:
                return i
        else:
            k -= length * val
            length -= cnt
            looped += val
        for ind in tmp:
            DP[ind] = True
    return -1