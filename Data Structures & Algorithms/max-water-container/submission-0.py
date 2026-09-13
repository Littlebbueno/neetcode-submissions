class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        maxArea = 0
        l, r = 0, size - 1
        while l < r:
            actualArea = (r - l) * min(heights[l], heights[r])
            if actualArea > maxArea:
                maxArea = actualArea
            if heights[l] > heights[r]:
                r -= 1
                continue
            else:
                l += 1
        return maxArea
            


## [1, 7, 2, 5, 4, 7, 3, 6]



