class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        mySet = set(nums)
        res = 0
        for num in mySet:
            if (num - 1) not in mySet:
                length = 1
                while (num + length) in mySet:
                    length += 1
                res = max(length, res)

        return res
        




