def solution(id_list, report, k):
    answer = []
    # 신고 당한 사람 = [신고 한 사람들]
    # 길이가 k 이상이면 신고한 사람들의 인덱스 += 1
    
    answer = [0] * len(id_list)
    index = {id_list[ind] : ind for ind in range(len(id_list))}
    result = [[] for i in range(len(id_list))]
    for string in set(report):
        A, B = string.split(' ')
        result[index[B]].append(A)
        
    for ind in range(len(result)):
        arr = result[ind]
        if len(arr) >= k:
            for person in arr:
                answer[index[person]] += 1
    return answer