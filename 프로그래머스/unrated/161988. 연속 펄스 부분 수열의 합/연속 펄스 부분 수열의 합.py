class funcs:
    def getmaxnum(sequence):
        answer = 0
        result = 0
        left = 0
        for right in range(len(sequence)):
            num = sequence[right]
            result += num
            while result < 0 and left <= right:
                result -= sequence[left]
                left += 1
            answer = max(answer, result)
        return answer 
    
def solution(sequence):
    answer = 0
    # 두 가지 펄스를 곱한 결과 리스트 SeqFirstPlusOne, SeqFirstMinusOne
    # 투 포인터로 문제 해결
    SeqFirstPlusOne, SeqFirstMinusOne = [], []
    boolean = True
    for i in range(len(sequence)):
        num = sequence[i]
        SeqFirstPlusOne.append(num * (1 if boolean else -1))
        SeqFirstMinusOne.append(num * (1 if not boolean else -1))
        boolean = not boolean
    
    result1 = funcs.getmaxnum(SeqFirstPlusOne)
    result2 = funcs.getmaxnum(SeqFirstMinusOne)
    # print(result2, SeqFirstMinusOne)
    
    return max(result1, result2)