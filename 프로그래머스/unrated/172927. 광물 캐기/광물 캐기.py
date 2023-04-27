def solution(picks, minerals):
    DP = []
    materials = {
        'diamond' : 25,
        'iron' : 5,
        'stone' : 1
    }
    for ind in range(len(minerals) // 5 + 1):
        tmp = [0] * 3
        for i in range(3):
            staff = 5 ** abs(i - 2)
            cnt = 0
            for j in range(5):
                if ind*5 + j >= len(minerals):
                    break
                cnt += max(materials[minerals[ind*5 + j]] // staff , 1)
            tmp[i] += cnt
        DP.append(tmp)
        
    INF = float('inf')
    
    def dfs(ind, picks, cnt):
        if ind >= len(DP):
            return cnt
        answer = INF
        skipped = 0
        for i in range(3):
            if picks[i] == 0:
                skipped += 1
                continue
            picks[i] -= 1
            answer = min(answer, dfs(ind + 1, picks, cnt + DP[ind][i]))
            picks[i] += 1
        if skipped == 3:
            return cnt
        return answer
    answer = dfs(0, picks, 0)   
    return answer