class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = float('inf'), float('inf')
        for price in prices:
            if min2 > price:
                min2 = price
                min1, min2 = min(min1, min2), max(min1, min2)
        if min1 + min2 > money:
            return money
        return money - (min1 + min2)