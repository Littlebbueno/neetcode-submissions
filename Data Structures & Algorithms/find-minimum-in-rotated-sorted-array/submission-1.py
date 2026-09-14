class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        size = len(nums)
        l, r = 0, size - 1
        if size == 1:
            return nums[0]
        while l < r:
            if nums[l]<nums[r]:
                if res > nums[l]:
                    res = nums[l]
                r -= 1
            else:
                if res > nums[r]:
                    res = nums[r]
                l += 1
        return res


        
            
        