class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalList = []
        size = len(nums)
        nums.sort()
        i = 0
        l, r = i + 1, size - 1

        while i in range(size):
            while l < r:
                soma = nums[l] + nums[r] + nums[i]
                if soma == 0:
                    newSum = [nums[i], nums[l], nums[r]]
                    if newSum not in finalList:
                        finalList.append(newSum)
                    l += 1
                if soma > 0:
                    r -= 1
                if soma < 0:
                    l += 1
            i += 1
            l = i + 1
            r = size - 1

        return finalList
        #sorted [-4,-1,-1,0,1,2]
        i = 2
        l = 3
        r = 5
        finalList = [[-1,-1,2], [-1,0,1]]


