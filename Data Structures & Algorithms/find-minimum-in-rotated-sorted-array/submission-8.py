class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        size = len(nums)                
        l, r = 0, size - 1
        if size == 1:                       
            return nums[0]
        while l <= r:                      
            mid = (r + l) // 2
            if nums[mid] < res:
                res = nums[mid]
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return res


        
            
        