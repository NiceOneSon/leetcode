def solution(cards):
    results = set()
    cards = list(map(lambda x : x-1, cards))
    answer = [0]
    for card in cards:
        tmpind = cards[card]
        tmpnum = 1
        while tmpind != card:
            if tmpind in results:
                tmpnum = 0
                break
            tmpind = cards[tmpind]
            tmpnum += 1
        results.add(card)
        answer.append(tmpnum)
        print()
    answer.sort()
    return answer[-1] * answer[-2]