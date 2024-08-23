# class denAndNum:
#     def __self__(self, numerator: int, denominator: int):
#         self.num = numerator
#         self.den = denominator
    
#     def __add__(self, obj: denAndNum) -> denAndNum:
        
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        def divider(expression: str) -> list:
            answer = []
            opers: tuple[str] = ('+', '-', '*')
            left, right= 0, 1
            for right in range(1, len(expression)):
                charactor = expression[right]
                if charactor in opers:
                    answer.append(Fraction(expression[left:right]))
                    answer.append(expression[right])
                    left = right + 1 
            answer.append(Fraction(expression[left:]))
            return answer
        def calc(left, right, oper):
            if oper == '+':
                return left + right
            if oper == '-':
                return left - right
            return left * right
        
        def loop_list(divided_expressions: list) -> str:
            left, right = None, None
            oper = None
            opers: tuple[str] = ('+', '-', '*')
            for idx in range(len(divided_expressions)):
                if divided_expressions[idx] in opers:
                    oper = divided_expressions[idx]
                    continue
                if not left:
                    left = divided_expressions[idx]
                else:
                    right = divided_expressions[idx]
                    left = calc(left, right, oper)
            return left
                    
        divided_expressions = divider(expression)
        result = loop_list(divided_expressions)
        if int(result) == result:
            return f'{int(result)}/1'
        return str(result)