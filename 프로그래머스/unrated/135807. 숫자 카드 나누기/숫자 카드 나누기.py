from math import gcd as get_gcd
def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    
    # def get_gcd(a, b):
    #     a, b = min(a, b), max(a, b)
    #     while b % a != 0:
    #         b, a = max(b % a, b), min(b % a, b)
    #     return a
    
    def get_answer(arrA, arrB):
        tmp = None
        for A in arrA:
            if tmp == None:
                tmp = A
            else:
                tmp = get_gcd(tmp, A)
        
        # if tmp == 1:
        #     return 0
        answer = tmp
        for B in arrB:
            if answer == get_gcd(tmp, B): # 나눠 진다는 것
                return 0
        return answer
        
    
    return max(get_answer(arrayA, arrayB), get_answer(arrayB, arrayA))
            