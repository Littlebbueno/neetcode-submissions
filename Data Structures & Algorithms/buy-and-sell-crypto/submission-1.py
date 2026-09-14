class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        l, r = 0, size - 1
        profit = 0
        menor = float('inf')
        for p in prices:
            if p < menor:
                menor = p
            if p - menor > profit:
                profit = p -  menor
        return profit


# [10,1,5,6,7,1]


            

