class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = set(nums)
        if len(setList) != len(nums):
            return True
        else:
            return False