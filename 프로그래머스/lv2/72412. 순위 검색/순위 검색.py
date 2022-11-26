from bisect import bisect_left

def solution(infos, querys):
    answer = []
    dictionary = {
        '-' : 0, 'cpp' : 1, 'java' : 2, 'python' : 3,
        'backend' : 1, 'frontend' : 2,
        'junior' : 1, 'senior' : 2,
        'chicken' : 1, 'pizza' : 2
    }
    
    arr = [[] for i in range(4*3*3*3)]
    
    for info in infos:
        program, posi, peri, els, score = info.split(' ')
        score = int(score)
        program = dictionary[program] * (3**3)
        posi = dictionary[posi] * (3**2)
        peri = dictionary[peri] * (3)
        els = dictionary[els]
        cols = [program, posi, peri, els]
        for num in range(1<<4):
            col = 0
            for ind in range(4):
                if num & 1 << ind:
                    col += cols[ind]
            arr[col].append(score)
        
    for row in arr:
        if row:
            row.sort()
    
    for query in querys:
        program, posi, peri, els = query.split(' and ')
        els, score = els.split(' ')
        score = int(score)
        program = dictionary[program] * (3**3)
        posi = dictionary[posi] * (3**2)
        peri = dictionary[peri] * (3)
        els = dictionary[els]
        cols = program + posi + peri + els
        answer.append(len(arr[cols]) - bisect_left(arr[cols], score))
    
    return answer