from collections import defaultdict

def recur(words, left, right, depth):
    
    if left + 1 == right:
        # print('!!finish', left, right, depth, words[left][:depth+1])
        return depth
    answer = 0
    prev = words[left][:depth+1]
    start = left
    for ind in range(left+1, right):
        if prev == words[ind][:depth+1]:
            # print(f'#continue  prev : {prev}, ind : {ind}, word : {words[ind][:depth+1]}')
            continue
        else:
            # print(f'#recur  prev : {prev}, ind : {ind}, word : {words[ind][:depth+1]}')
            answer += recur(words, start, ind, min(len(prev), depth+1))
            start = ind
            prev = words[ind][:depth+1]
    else:
        answer += recur(words, start, right, depth+1)
    return answer
        
    
def solution(words):
    answer = 0
    words.sort()
    return recur(words, 0, len(words), 0)