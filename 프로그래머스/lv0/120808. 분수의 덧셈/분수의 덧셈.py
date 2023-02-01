# from fractions import Fraction
# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     a = Fraction(numer1, denom1)
#     b = Fraction(numer2, denom2)
#     c = a + b
#     return c.numerator, c.denominator


import math

def solution(num1, denum1, num2, denum2):
    denominator = denum1 * denum2
    numerator = num1 * denum2 + num2 * denum1
    gcd = math.gcd(denominator, numerator)
    return [numerator//gcd, denominator//gcd]