class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        l, r = 0, size - 1
        profit = 0

        while l < r:
            soma = prices[r] - prices[l]
            if soma > profit:
                profit = soma
            r -= 1
            if r == l:
                l += 1
                r = size - 1

        return profit


# [10,1,5,6,7,1]


            

