class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        ## Debug Area
        
        
        ##
        while i < j:
            mid = (i + j)//2
            if nums[i] == target: return i
            if nums[mid] == target: return mid
            if nums[j] == target: return j
            var1 = nums[i]
            var2 = nums[mid]
            var3 = nums[j]
            if var1 < var2:
                if var1 < target < var2:
                    j = mid
                else:
                    i = mid
            elif var1 > var2:
                if var2 < target < var3:
                    i = mid
                else:
                    j = mid
            else:
                break
        return -1