class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        l, r = 0, size - 1
        if size == 1:                           
            if target == nums[0]:                  
                return 0                             
        while l < r:                               
            mid = (r + l) // 2                               
            if target == nums[l]: return l
            if target == nums[r]: return r            
            if target == nums[mid]: return mid
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1     
        return -1