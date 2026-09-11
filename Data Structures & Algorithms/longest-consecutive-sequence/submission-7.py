class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        res = 0
        for value in mySet:
            if (value - 1) not in mySet:
                size = 1
                i = 1
                while value + i in mySet:
                    size += 1
                    i += 1
                res = max(res, size)
        return res
                
        