def solution(N, number):
    answer = 0
    setting = [set([int(str(N) * ind) if ind else '']) for ind in range(9)]
    
    if N == number:
        return 1
    
    for i in range(2, 9): # 4
        for j in range(1, i): # 1 2 3
            for set1 in setting[i - j]:
                for set2 in setting[j]:
                    setting[i].add(set1 + set2)
                    setting[i].add(set1 - set2)
                    setting[i].add(set1 * set2)
                    if set2 != 0:
                        setting[i].add(set1 // set2)
        else:
            if number in setting[i]:
                return i
                            
      
    return -1