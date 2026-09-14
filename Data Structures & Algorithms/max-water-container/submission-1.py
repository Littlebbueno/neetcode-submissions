class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        size = len(heights)
        l, r = 0, size - 1

        while l < r:
            prod = min(heights[l], heights[r]) * (r - l)
            if prod > res:
                res = prod
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res