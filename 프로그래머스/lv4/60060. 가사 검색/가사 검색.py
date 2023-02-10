# len(query)
    # ind, alphabet
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    words.sort()
    reverse_words = sorted(words, key = lambda x : x[::-1])
    reverse_words = map(lambda x : x[::-1], reverse_words)
    tmp = {}
    for word in words:
        if len(word) not in tmp:
            tmp[len(word)] = [word]
        else:
            tmp[len(word)].append(word)
    words = tmp
    tmp = {}
    for word in reverse_words:
        if len(word) not in tmp:
            tmp[len(word)] = [word]
        else:
            tmp[len(word)].append(word)
    reverse_words = tmp
    for query in queries:
        if query[-1] == '?':
            if len(query) not in words:
                answer.append(0)
                continue
            ind = query.index('?')
            lind = bisect_left(words[len(query)], query.replace('?', 'a'))
            rind = bisect_right(words[len(query)], query.replace('?', 'z'))
            answer.append(rind - lind)
        else:
            if len(query) not in reverse_words:
                answer.append(0)
                continue
            ind = 0 
            for string in query:
                if string != '?':
                    break
            lind = bisect_left(reverse_words[len(query)], query.replace('?', 'a')[::-1])
            rind = bisect_right(reverse_words[len(query)], query.replace('?', 'z')[::-1])
            answer.append(rind - lind)
        
    return answer