from bisect import bisect_left

def solution(info, query):
    answer = []
    
    hash = {'-' : 0, 'cpp' : 1, 'java' : 2, 'python' : 3,
           'backend' : 1, 'frontend' : 2,
           'junior' : 1,  'senior' : 2,
           'chicken' : 1, 'pizza' : 2
           }
    
    result = [[] for _ in range((4*3*3*3))]
    
    for infor in info:
        tmp = []
        p, j, l, i, sc = infor.split(' ')
        arr = [hash[p] * 27
              ,hash[j] * 9
              ,hash[l] * 3
              ,hash[i]
              ,int(sc)]
        lists = []
        for i in range(1 << 4):
            summation = 0
            for j in range(4):
                if i & (1 << j):
                    summation += arr[j]
            result[summation].append(arr[4])
            
    for ind in range(len(result)):
        result[ind].sort()

    for q in query:
        q = q.split(' ')
        ind = hash[q[0]] * 27 + hash[q[2]] * 9 + hash[q[4]] * 3 + hash[q[6]]
        score = int(q[7])
        answer.append(len(result[ind]) - bisect_left(result[ind], score))
    
    
    
    return answer