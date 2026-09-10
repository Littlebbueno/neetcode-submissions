import math

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        flagCompleted = False
        for index, value in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index2 == index:
                    continue
                else:
                    if (value + value2) == target:
                        pair.append(min(index,index2))
                        pair.append(max(index,index2))
                        flagCompleted = True
                        break
            if flagCompleted == True:
                break
        return pair
