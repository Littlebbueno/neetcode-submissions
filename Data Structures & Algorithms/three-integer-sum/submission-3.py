class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = []
        nums.sort()
        size = len(nums)
        index = 0
        for index in range(size):
            l, r = (index + 1), (size - 1)
            if (index - 1) >= 0:
                if nums[index] == nums[index -1]:
                    continue
            while l < r:
                soma = nums[index] + nums[r] + nums[l]
                if soma == 0:
                    item = [nums[index], nums[r], nums[l]]
                    finalList.append(item)
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                elif soma > 0:
                    r -= 1
                elif soma < 0:
                    l += 1
        return finalList
                


        

            



        
        