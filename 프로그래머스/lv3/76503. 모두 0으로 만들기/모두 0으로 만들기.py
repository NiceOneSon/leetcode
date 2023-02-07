from collections import deque

def solution(a, edges):
    q = deque()
    indegree = [0] * (len(a))
    graph = [[] for i in range(len(a))]
    
    for node1, node2 in edges:
        indegree[node1] += 1
        indegree[node2] += 1
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    for i in range(len(a)):
        if indegree[i] == 0:
            continue
        if indegree[i] == 1:
            q.append(i)
            
    answer = 0
    while q:
        node1 = q.popleft()
        num = a[node1]
        indegree[node1] = 0
        check = False
        for node2 in graph[node1]:
            if indegree[node2] == 0:
                continue
            indegree[node2] -= 1
            a[node1] -= num
            a[node2] += num
            answer += abs(num)
            # print(num, node1, node2)
            num = 0
            if indegree[node2] == 1:
                q.append(node2)
                
    for val in a:
        if val:
            answer = -1
    return answer