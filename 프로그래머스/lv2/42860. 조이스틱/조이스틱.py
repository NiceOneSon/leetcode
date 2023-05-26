def getalpha(string):
    lind, rind = ord('A'), ord(string)
    return min(rind - lind, ord('Z') - rind + 1)

def getdistance(length, find, tind):
    find, tind = min(find, tind), max(find, tind)
    return min(tind - find, length - tind + find )

def solution(name):
    answer = 0
    
    name = list(name)
    length = len(name)
    visited = [False] * length
    visited[0] = True
    for i in range(length):
        if name[i] == 'A':
            visited[i] = True
    
    def dfs(visited, result, x):
        FLAG = False
        answer = float('inf')
        for i in range(length):
            if visited[i] == False:
                FLAG = True
                visited[i] = True
                dist = getdistance(length, x, i)
                cnt = getalpha(name[i])
                answer = min(answer, dfs(visited, result + cnt + dist, i))
                visited[i] = False
        if FLAG == False:
            return result
        return answer
    
    answer = dfs(visited, getalpha(name[0]), 0)
    return answer